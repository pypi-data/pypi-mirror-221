from math import inf
from typing import (
  TYPE_CHECKING, Any, Generator, List, Optional, Protocol, Tuple, Type, Union
)

import langdash.sampling as sampling
from langdash.infer import InferArgs
from langdash.response import RespInfer, RespInferEnd, Response

from .._tokenizer.tokenizer import BufferedToken

if TYPE_CHECKING:
  import torch

  from langdash.logit_preprocessors import LogitPreprocessor


class TensorBasedGenerationSession(Protocol):
  _model: Any
  _logits: Optional["torch.Tensor"]
  _next_token: Optional[Tuple[int, str]]

  def _get_logit_preprocessor(
    self, T: Type["LogitPreprocessor"]
  ) -> "LogitPreprocessor":
    ...

  def _eval(self, token: int) -> "torch.Tensor":
    ...

  def tokenize(self, text: str, add_special_tokens: bool = False) -> List[int]:
    ...

  def decode(self, tokids: List[int]) -> str:
    ...


class TensorBasedInferMixin:
  _model: Any
  _logits: Optional["torch.Tensor"]
  _next_token: Optional[Tuple[int, str]]

  def _calculate_infer_end(
    self: TensorBasedGenerationSession,
    end: Optional[Union[str, int, List[str], List[int]]],
    end_is_token: bool = False,
  ) -> Tuple[Optional[Union[str, int, List[str], List[int]]], bool]:
    if isinstance(end, str):
      if len(end) == 0:
        return self._model.eos_token, True
      elif end_is_token:
        endtoks = self.tokenize(end)
        if len(endtoks) != 1:
          raise ValueError(f"'{end}' converts to more than 1 token")
        return endtoks[0], True
      else:
        return end, False
    elif isinstance(end, list):
      if end_is_token:
        infer_end: List[int] = []
        for endval in end:
          if isinstance(endval, str):
            if endval == "":
              infer_end.append(self._model.eos_token)
            else:
              endtoks = self.tokenize(endval)
              if len(endtoks) != 1:
                raise ValueError(f"'{endval}' converts to more than 1 token")
              infer_end.append(endtoks[0])
          else:  # int
            infer_end.append(endval)
        return infer_end, True
      else:
        return end, False
    elif isinstance(end, int):
      return end, True
    else:
      return end, False  # None

  def _infer(
    self: TensorBasedGenerationSession,
    end: Optional[Union[str, int, List[str], List[int]]],
    args: InferArgs,
    end_is_token: bool = False,
    logit_preprocessors: Optional[List[Type["LogitPreprocessor"]]] = None,
  ) -> Generator[Response, None, None]:
    generated = ""
    buffered_tokens: Optional[BufferedToken] = None
    ctx: List[int] = []
    tokens_counter = 0

    if args.min_new_tokens > 0:
      end_is_token = True

    infer_end, end_is_token = TensorBasedInferMixin._calculate_infer_end(
      self, end, end_is_token
    )

    if self._logits is None:
      if self._next_token is not None:
        self._logits = self._eval(self._next_token[0])
        self._next_token = None
      else:
        raise ValueError(
          "Initial prompt is not provided. Please inject a prompt into the model before generation."
        )

    for i in range(args.max_new_tokens):
      strip_left: Optional[str] = None

      assert self._logits is not None

      if i == 0 and self._next_token is not None:
        for logits_tokid in self._model.tokenizer.tokens_starting_with(
          self._next_token[0]
        ):
          self._logits[logits_tokid] = -inf

        if self._logits.isinf().all():
          # we don't need to heal tokens because no token that begins with _next_token
          self._logits = self._eval(self._next_token[0])
        else:
          strip_left = self._next_token[1]

        self._next_token = None

      if end_is_token and args.min_new_tokens > 0 and i < args.min_new_tokens:
        if isinstance(infer_end, int):
          self._logits[infer_end] = -inf
        elif isinstance(infer_end, list):
          for token in infer_end:
            self._logits[infer_end] = -inf
        else:
          raise NotImplementedError(f"unexpected type: {type(infer_end)}")

      if logit_preprocessors is not None:
        for pp in logit_preprocessors:
          self._get_logit_preprocessor(pp)(ctx, self._logits)

      tokid = sampling.sample(self._logits, args, ctx)
      ctx.append(tokid)
      tokens_counter += 1

      if end_is_token:
        if isinstance(infer_end, int):
          if tokid == infer_end:
            break
        elif isinstance(infer_end, list):
          if tokid in infer_end:
            break

      tokstr: Optional[str] = None

      if buffered_tokens is None:
        tokstr_or_buffered = self._model.tokenizer.decode_once(tokid)

        if isinstance(tokstr_or_buffered, str):
          tokstr = tokstr_or_buffered
        else:
          buffered_tokens = tokstr_or_buffered
      else:
        tokstr = buffered_tokens.add_token_id(tokid)

      if tokstr is not None:
        if strip_left and tokstr.startswith(strip_left):
          tokstr = tokstr[len(strip_left):]

        self._next_token = (tokid, tokstr)

        generated += tokstr
        if not end_is_token:
          assert isinstance(infer_end, (str, list))  # str or List[str]
          if generated.endswith(infer_end):
            generated = generated[:-len(infer_end)]
            break

        yield RespInfer(tokid=tokid, tokstr=tokstr, running_infer=generated)

        buffered_tokens = None

      self._logits = self._eval(tokid)

    if buffered_tokens:
      tokens_counter += len(buffered_tokens)
      tokstr = buffered_tokens.flush()
      generated += tokstr
      yield RespInfer(tokid=tokid, tokstr=tokstr, running_infer=generated)

    yield RespInferEnd(running_infer=generated, tokens_counter=tokens_counter)


class TensorBasedInferWithSessionMixin:

  def _infer(self: TensorBasedGenerationSession, *a, **k):
    self._model.enter_session(self)
    yield from TensorBasedInferMixin._infer(self, *a, **k)
