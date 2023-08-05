from typing import Sequence

import torch
from torch.nn import functional as F

from langdash.infer import InferArgs


def _sample_greedy(probs: torch.Tensor) -> torch.Tensor:
  argmax = torch.argmax(probs)
  probs[:] = 0.
  probs[argmax] = 1.
  return probs


@torch.jit.script
def _sample_top_p(probs: torch.Tensor, top_p: float) -> torch.Tensor:
  assert 0.0 <= top_p <= 1.0, "top_p must be in [0.0, 1.0]"
  sorted_probs = torch.sort(probs, descending=True)[0]
  cumulative_probs = torch.cumsum(sorted_probs, dim=-1)
  cutoff = float(sorted_probs[torch.argmax((cumulative_probs > top_p).long())])
  probs[probs < cutoff] = 0
  return probs


@torch.jit.script
def _sample_top_k(probs: torch.Tensor, top_k: int, top_p: float):
  assert 0 <= top_k <= probs.shape[0], "top_k must be in [0, len]"
  assert 0.0 <= top_p <= 1.0, "top_p must be in [0.0, 1.0]"
  sorted_probs, indices = torch.sort(probs, descending=True)
  probs[indices[top_k:]] = 0.

  if top_p > 0.:
    mag = torch.sum(sorted_probs)
    probs /= mag
    sorted_probs /= mag

    cumulative_probs = torch.cumsum(sorted_probs, dim=-1)
    cutoff = float(
      sorted_probs[torch.argmax((cumulative_probs > top_p).long())]
    )
    probs[probs < cutoff] = 0.

  return probs


@torch.jit.script
def _sample_typical(
  probs: torch.Tensor, logits: torch.Tensor, mass: float
) -> torch.Tensor:
  # https://github.com/huggingface/transformers/compare/main...cimeister:typicalsampling:typical-pr
  assert 0.0 <= mass <= 1.0, "typical mass must be in [0.0, 1.0]"
  normalized = -torch.log(probs)
  ent = torch.nansum(normalized * probs, dim=-1, keepdim=True)

  shifted_scores = torch.abs(logits - ent)
  sorted_scores, sorted_indices = torch.sort(shifted_scores, descending=False)
  sorted_logits = logits.gather(-1, sorted_indices)
  cumulative_probs = sorted_logits.softmax(dim=-1).cumsum(dim=-1)

  indices = (cumulative_probs < mass).sum()
  probs[shifted_scores > sorted_scores[indices]] = 0.
  return probs


def _output_probs(
  logits: torch.Tensor, args: InferArgs, ctx: Sequence[int]
) -> torch.Tensor:
  # apply repetition penalty
  if args.rep_penalty != 1.0:
    rep_penalty = args.rep_penalty
    assert 0.0 <= rep_penalty, "rep_penalty must be in [0.0, inf]"
    for _, tok in zip(range(args.max_rep_ctx), reversed(ctx)):
      if logits[tok] < 0.0:
        logits[tok] *= rep_penalty
      else:
        logits[tok] /= rep_penalty

  probs = logits_to_probs(logits)

  if args.temperature == 0.0:
    probs = _sample_greedy(probs)
  else:
    if args.top_k > 0:
      probs = _sample_top_k(probs, args.top_k, args.top_p)
    else:
      if args.typical_mass > 0.0:
        probs = _sample_typical(probs, logits, args.typical_mass)
      if args.top_p > 0.0:
        probs = _sample_top_p(probs, args.top_p)
    if args.temperature != 1.0:
      probs = probs.pow(1.0 / args.temperature)

  return probs


def sample(logits: torch.Tensor, args: InferArgs, ctx: Sequence[int]) -> int:
  """
  Sample from a distribution of tokens specified by *logits*.
  
  Args:
    logits (torch.FloatTensor): Logits to sample from.
    args (InferArgs): Sampling arguments.
    ctx (Sequence[int]): Sequence of tokens generated so far.
  
  Returns:
    The token sampled.
  """
  probs = _output_probs(logits, args, ctx)
  return int(torch.multinomial(probs, num_samples=1, generator=args.rng)[0])


def logits_to_probs(logits: torch.Tensor):
  """ Converts logit tensor to probability tensor using softmax. """
  return F.softmax(logits, dim=-1)
