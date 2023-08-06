import weakref
from typing import Any, List, Optional

import ctransformers  # type: ignore
import torch
from ctransformers.llm import LLM as CTransformersLLM  # type: ignore
from ctransformers.llm import LLMState as CTransformersState

import langdash.sampling as sampling
from langdash.llm import LLM
from langdash.llm_config import LLMConfig
from langdash.llm_session import (
  LLMGenerationSession, LLMGenerationSessionForRawText
)

from ._mixins.tensor_based_infer_mixin import TensorBasedInferWithSessionMixin
from ._tokenizer.bytes_dict_tokenizer import BytesDictTokenizer
from ._tokenizer.hf_tokenizer import HFTokenizer
from ._tokenizer.tokenizer import Tokenizer


class CTransformersWrapper:
  model: CTransformersLLM
  tokenizer: Tokenizer
  vocab: List[bytes]
  last_called_session: Optional[weakref.ref]
  eos_token: int

  def __init__(
    self, model_path: str, tokenizer: Optional[Any] = None, *args, **kwargs
  ):
    self.model = ctransformers.AutoModelForCausalLM.from_pretrained(
      model_path, **kwargs
    )
    if tokenizer is not None:
      self.tokenizer = HFTokenizer(tokenizer)
    else:
      mapping = [
        self.model.token_id_to_str(tokid)
        for tokid in range(self.model.vocab_size)
      ]
      self.tokenizer = BytesDictTokenizer(
        lambda text, **_k: self.model.tokenize(text),
        lambda tokens: self.model.detokenize(tokens), mapping
      )
    self.eos_token = self.model.eos_token_id
    self.last_called_session = None

  def eval(self, tokens: List[int]) -> torch.Tensor:
    self.model.eval(tokens)
    return torch.tensor(self.model.logits)

  def enter_session(self, session: "CTransformersSession"):
    if self.last_called_session is None:
      self.last_called_session = weakref.ref(session)
      return
    last_called_session = self.last_called_session()
    if session == last_called_session:
      return
    elif last_called_session is not None:
      if self.model.eval_logits:
        last_called_session._logits = self.load_logits_from_model()
        last_called_session._state = self.model.save_state()
      else:
        last_called_session._logits = None
        last_called_session._state = None
    if session._state is not None:
      self.model.set_state(session._state)
    self.last_called_session = weakref.ref(session)

  def load_logits_from_model(self) -> torch.Tensor:
    return torch.Tensor(self.model.eval_logits[-1])

  def clone_state(self, session: "CTransformersSession") -> CTransformersState:
    self.enter_session(session)
    if self.model.eval_logits:
      return self.model.clone_state()
    else:
      return None

  def set_state(
    self, session: "CTransformersSession", state: Optional[CTransformersState]
  ):
    self.enter_session(session)
    self.model.reset()
    if state is not None:
      self.model.set_state(state)

  def get_context_length(self) -> int:
    # self.enter_session(self)
    return self.model.context_length


class CTransformersSession(
  TensorBasedInferWithSessionMixin,
  LLMGenerationSessionForRawText["CTransformersModel", CTransformersState],
):
  """
  Session for ctransformers model.
  """

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    def load_model(llm: CTransformersModel):
      return CTransformersWrapper(
        model_path=llm._model_path, **llm._model_kwargs
      )

    self._model = self._ld._get_model_internal(self._llm, load_model)

    self._logits = None
    self._state = None
    self._next_token = None

  def _eval(self, token: int):
    return self._model.eval([token])

  def _eval_mult(self, tokens: List[int]):
    return self._model.eval(tokens)

  def tokenize(self, text: str, add_special_tokens: bool = False) -> List[int]:
    return self._model.tokenizer.encode(
      text, add_special_tokens=add_special_tokens
    )

  def decode(self, tokids: List[int]) -> str:
    return self._model.tokenizer.decode(tokids)

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

  def set_state(self, state: Optional[CTransformersState]):
    if state is None:
      self._model.set_state(self, None)
      self._logits = None
      LLMGenerationSession._reset_state(self)
    else:
      self._model.set_state(self, state)
      self._logits = self._model.load_logits_from_model()

  def clone_state(self) -> Optional[CTransformersState]:
    return self._model.clone_state(self)

  @property
  def context_length(self) -> int:
    return self._model.get_context_length(self)

  def get_vocab(self):
    return self._model.tokenizer.get_vocab()

  def tokenize_special(self, text: str) -> Optional[int]:
    if text == "</s>":
      return self._model.eos_token
    return None

  # Wrapper for public functions to flush the old session states

  def inject(self, *a, **k):
    self._model.enter_session(self)
    return LLMGenerationSessionForRawText.inject(self, *a, **k)

  def flush_token(self, *a, **k):
    self._model.enter_session(self)
    return LLMGenerationSessionForRawText.inject(self, *a, **k)


class CTransformersModel(LLM[CTransformersSession]):
  """
  ctransformers model.
  """

  _model_path: str
  _model_kwargs: dict

  Session = CTransformersSession

  def __init__(self, model_path: Optional[str] = None, **model_kwargs):
    if "config" in model_kwargs:
      if not isinstance(model_kwargs["config"], LLMConfig):
        raise TypeError("config argument must be LLMConfig")

      config = model_kwargs["config"]
      del model_kwargs["config"]

      self._model_kwargs = {}
      self._model_kwargs["config"] = ctransformers.hub.AutoConfig(
        config=ctransformers.llm.Config(
          batch_size=config.batch_size,
          threads=config.threads,
          context_length=config.context_length,
          gpu_layers=config.gpu_layers,
        )
      )
      self._model_kwargs.update(model_kwargs)
      model_path = config.model
    else:
      self._model_kwargs = model_kwargs

    if not isinstance(model_path, str):
      raise TypeError("model path must be string")
    self._model_path = model_path

  def session(self, **kwargs):
    return CTransformersSession(self, **kwargs)
