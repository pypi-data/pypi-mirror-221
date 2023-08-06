import weakref
from typing import List, Optional

import torch
from llama_cpp import Llama, LlamaState, llama_token_to_str  # type: ignore

import langdash.sampling as sampling
from langdash.llm import LLM
from langdash.llm_config import LLMConfig
from langdash.llm_session import (
  LLMGenerationSession, LLMGenerationSessionForRawText
)

from ._mixins.tensor_based_infer_mixin import TensorBasedInferWithSessionMixin
from ._tokenizer.bytes_dict_tokenizer import BytesDictTokenizer


class LlamaWrapper:
  model: Llama
  tokenizer: BytesDictTokenizer
  last_called_session: Optional[weakref.ref]
  eos_token: int
  bos_token: int

  def __init__(self, *args, **kwargs):
    self.model = Llama(*args, **kwargs)
    mapping = [
      llama_token_to_str(self.model.ctx, tokid)
      for tokid in range(self.model.n_vocab())
    ]
    self.tokenizer = BytesDictTokenizer(
      lambda text, **_k: self.model.
      tokenize(text.encode("utf-8"), add_bos=False), lambda tokens, **_k: self.
      model.detokenize(tokens).decode("utf-8", errors="ignore"), mapping
    )
    self.last_called_session = None
    self.eos_token = Llama.token_eos()
    self.bos_token = Llama.token_bos()

  def eval(self, tokens: List[int]) -> torch.Tensor:
    self.model.eval(tokens)
    return torch.from_numpy(self.model._scores[-1, :])

  def enter_session(self, session: "LlamaCppSession"):
    if self.last_called_session is None:
      self.last_called_session = weakref.ref(session)
      return
    last_called_session = self.last_called_session()
    if session == last_called_session:
      return
    elif last_called_session is not None:
      if self.model.eval_logits:
        last_called_session._logits = self.load_logits_from_llama()
        last_called_session._state = self.model.save_state()
      else:
        last_called_session._logits = None
        last_called_session._state = None
    if session._state is not None:
      self.model.load_state(session._state)
    self.last_called_session = weakref.ref(session)

  def load_logits_from_llama(self) -> torch.Tensor:
    return torch.Tensor(self.model.eval_logits[-1])

  def clone_state(self, session: "LlamaCppSession") -> Optional[LlamaState]:
    self.enter_session(session)
    if self.model.eval_logits:
      return self.model.save_state()
    else:
      return None

  def set_state(self, session: "LlamaCppSession", state: Optional[LlamaState]):
    self.enter_session(session)
    self.model.reset()
    if state is not None:
      self.model.load_state(state)

  def get_context_length(self) -> int:
    # self.enter_session(self)
    return self.model.n_ctx()

  def _on_first_inject(self, session: "LlamaCppSession"):
    self.enter_session(session)
    self.model.reset()
    self.model.eval([self.bos_token])


class LlamaCppSession(
  TensorBasedInferWithSessionMixin,
  LLMGenerationSessionForRawText["LlamaCppModel", LlamaState],
):
  """
  Session for llama.cpp model.
  """

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    def load_model(llm: LlamaCppModel):
      return LlamaWrapper(model_path=llm._model_path, **llm._model_kwargs)

    self._model = self._ld._get_model_internal(self._llm, load_model)
    
    self.skip_bos = False
    
    self._logits = None
    self._state = None
    self._next_token = None

  def _eval(self, token: int):
    return self._model.eval([token])

  def _eval_mult(self, tokens: List[int]):
    return self._model.eval(tokens)

  def next_token_logits(self) -> torch.Tensor:
    self._model.enter_session(self)
    if self._next_token is None:
      if self._logits is None:
        raise ValueError("cannot predict next probability for empty input")
      logits = self._logits
    else:
      logits = self._eval(self._next_token[0])
    return logits

  def next_token_probs(self) -> torch.Tensor:
    return sampling.logits_to_probs(self.next_token_logits())

  def set_state(self, state: Optional[LlamaState]):
    if state is None:
      self._model.set_state(self, None)
      self._logits = None
      LLMGenerationSession._reset_state(self)
    else:
      self._model.set_state(self, state)
      self._logits = self._model.load_logits_from_llama()

  def clone_state(self) -> Optional[LlamaState]:
    return self._model.clone_state(self)

  def tokenize(self, text: str, add_special_tokens: bool = False) -> List[int]:
    return self._model.tokenizer.encode(
      text, add_special_tokens=add_special_tokens
    )

  def decode(self, tokens: List[int]) -> str:
    return self._model.tokenizer.decode(tokens)

  def _on_first_inject(self):
    if self.skip_bos:
      return
    self._model._on_first_inject(self)

  @property
  def context_length(self) -> int:
    return self._model.get_context_length(self)

  def get_vocab(self):
    return self._model.tokenizer.get_vocab()

  def tokenize_special(self, text: str) -> Optional[int]:
    if text == "<s>":
      return self._model.bos_token
    elif text == "</s>":
      return self._model.eos_token
    return None

  # Wrapper for public functions to flush the old session states

  def inject(self, *a, **k):
    self._model.enter_session(self)
    return LLMGenerationSessionForRawText.inject(self, *a, **k)

  def flush_token(self, *a, **k):
    self._model.enter_session(self)
    return LLMGenerationSessionForRawText.inject(self, *a, **k)


class LlamaCppModel(LLM[LlamaCppSession]):
  """
  llama.cpp model.
  """

  _model_path: str
  _model_kwargs: dict

  Session = LlamaCppSession

  def __init__(self, model_path: Optional[str] = None, **model_kwargs):
    """
    Creates a template for the Llama language model (using the llama.cpp library).
    """
    if "config" in model_kwargs:
      if not isinstance(model_kwargs["config"], LLMConfig):
        raise TypeError("config argument must be LLMConfig")

      config = model_kwargs["config"]
      del model_kwargs["config"]

      self._model_kwargs = {
        "n_batch": 512 if config.batch_size == -1 else config.batch_size,
        "n_threads": None if config.threads == -1 else config.threads,
        "n_ctx": 512 if config.context_length == -1 else config.context_length,
        "n_gpu_layers": config.gpu_layers,
      }
      self._model_kwargs.update(model_kwargs)
      model_path = config.model
    else:
      self._model_kwargs = model_kwargs

    if "verbose" not in self._model_kwargs:
      self._model_kwargs["verbose"] = False

    if not isinstance(model_path, str):
      raise TypeError("model path must be string")
    self._model_path = model_path

  def session(self, **kwargs):
    return LlamaCppSession(self, **kwargs)
