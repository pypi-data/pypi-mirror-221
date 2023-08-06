import gc
from typing import Callable, Dict, TypeVar

import langdash.chains as chains
from langdash.llm import LLM
from langdash.llm_session import T_LLM, LLMSession


def _llama_cpp_callback(*a, **k):
  from .models.llama_cpp import LlamaCppModel
  return LlamaCppModel(*a, **k)


def _rwkv_cpp_callback(*a, **k):
  from .models.rwkv_cpp import RwkvCppModel
  return RwkvCppModel(*a, **k)


def _transformers_callback(*a, **k):
  from .models.transformers import TransformersModel
  return TransformersModel(*a, **k)


def _ctransformers_callback(*a, **k):
  from .models.ctransformers import CTransformersModel
  return CTransformersModel(*a, **k)


def _sentence_transformers_callback(*a, **k):
  from .models.sentence_transformers import SentenceTransformersModel
  return SentenceTransformersModel(*a, **k)


MODEL_CALLBACKS = {
  "llama_cpp": _llama_cpp_callback,
  "rwkv_cpp": _rwkv_cpp_callback,
  "transformers": _transformers_callback,
  "ctransformers": _ctransformers_callback,
  "sentence_transformers": _sentence_transformers_callback,
}

T_ModelInternal = TypeVar("T_ModelInternal")


class Langdash:
  """
  Core Langdash instance.
  """
  _models: Dict[str, LLM]

  def __init__(self):
    self._models = {}
    self._cached_models = {}

  def _get_model_internal(
    self, model: T_LLM, default: Callable[[T_LLM], T_ModelInternal]
  ) -> T_ModelInternal:
    if model in self._cached_models:
      return self._cached_models[model]
    gc.collect()
    self._cached_models[model] = default(model)
    return self._cached_models[model]

  def register_model(self, name: str, model: LLM):
    """
    Register a new language model to the Langdash instance.
    
    Args:
      name (str): The name of the model.
      model (LLM): The LLM object.
    """
    if name in self._models:
      raise KeyError(f"model '{name}' already exists")
    self._models[name] = model

  def session_for_model(self, model: str, **kwargs) -> LLMSession:
    """
    Create a new session for a given model.
    
    Args:
      model (str): The name of the model to be used.
      default_infer_args (InferArgs):
        Default arguments for the inference.
      token_healing (bool):
        Whether to enable token healing. Defaults to `True`.
      event_handlers (Optional[LLMGenerationSessionEvents]):
        Optional event handlers for prompt events. Defaults to `None`.
      initial_prompt (Optional[Union[str, int, List[int]]]):
        Optional initial prompt to be injected. Defaults to `None`.
    
    Returns:
      The session object.
    """
    session = self._models[model].session(ld=self, **kwargs)

    if kwargs.get("initial_prompt"):
      session.inject(kwargs["initial_prompt"])

    return session

  def chain(self, **kwargs) -> chains.LDChain:
    """
    Chain a list of nodes together.

    Args:
      nodes (List[Union["LDNode", str]]):
        A list of nodes or constant text nodes (represented by strings) to chain together.
      args (TypeDict):
        A dictionary of argument types for the chain function.
      returns (TypeDict):
        A dictionary of return value types for the chain function.

    Returns:
      The chain of nodes.
    """
    return chains.LDChain(self, **kwargs)

  def text(self, text, **kwargs):
    """
    Creates a raw text node.
    
    Args:
      text (str): The raw text.
      add_special_tokens (bool):
        Whether to treat text as containing special tokens or not.
        Defaults to `False`.
      
    Returns:
      The text node.
    """
    return chains.LDText(self, text=text, **kwargs)

  def format_args(self, text, **kwargs):
    """
    Creates a format argument node.
    
    Args:
      text (str): The format text.
      
    Returns:
      The format text node.
    """
    return chains.LDFormatArg(self, text=text, **kwargs)

  def arg(self, arg, **kwargs):
    """
    Creates a new argument node with the specified argument.
    
    Args:
      arg (str): The argument.
      padleft (str):
        The padding string to use for the left side of the argument.
      padright (str):
        The padding string to use for the right side of the argument.
    
    Returns:
      The argument node.
    """
    return chains.LDArg(self, arg=arg, **kwargs)

  def returns(self, returns, end, **kwargs):
    """
    Create a new return node for the specified return value.

    Args:
      returns (str): The name of the return value.
      end (InferEndSequence):
        Where to stop the inference. See `LLMGenerationSession#infer` for more details.
      padleft (str):
        The left padding value for the return. If the generated string starts with
        `padleft` then it will be stripped.
        
        Defaults to empty string.
      infer_args (Optional[InferArgs]):
        Optional inference arguments for generation. Defaults to `None`.
      end_is_token (bool):
        If true, then the end string will be interpreted as a token. Defaults to `False`.
      logit_preprocessors (Optional[List[LogitPreprocessor]]):
        Optional list of logit preprocessor functions to be
        called before sampling. Defaults to `None`.

    Returns:
      The return node.
    """
    return chains.LDReturns(self, returns=returns, end=end, **kwargs)

  def choice(self, returns, choices, **kwargs):
    """
    Creates a new choice node with the specified choices.
    
    Args:
      returns (str): The name of the return value.
      choices (Union[str, List[str]]):
        Either the list of choice strings or the name of the argument
        containing the list.
      padleft (str):
        Left padding for every choice string. Defaults to empty string.
      padright (str):
        Right padding for every choice string. Defaults to empty string.
    
    Returns:
      The choice node.
    """
    return chains.LDChoice(self, returns=returns, choices=choices, **kwargs)

  def repeat(self, **kwargs):
    """
    Creates a new repetition node that repeats a subchain.
    
    Args:
      subchain (LDChain):
        The subchain to be repeated.
      append_source (str):
        The return variable of the subchain, extracted into the parent chain's `append_target` list.
      append_target (str):
        The append target variable of the parent chain.
      end (str):
        Token used to mark the end of the repetition. This token will not be injected as a prompt after the loop.
      max_len (int):
        Maximum number of repetitions. `-1` means the chain will repeat until the next most likely token is `end`.
      end_threshold (float):
        Minimum probability of end token for the repetition to end.
    
    Returns:
      The repeat node.
    """
    return chains.LDRepeat(self, **kwargs)

  @staticmethod
  def model_from_type(type: str, *args, **kwargs) -> LLM:
    """
    Create an instance of a builtin model with specified type name.

    Additional arguments will be passed to the model constructor. Alternatively,
    a keyword argument with the name `config` of type `LLMConfig` can be passed
    to specify config parameters.
    
    Args:
      type (str): The type of the model.
    
    Returns:
      The model.
    """
    model_cb = MODEL_CALLBACKS.get(type)
    if model_cb:
      return model_cb(*args, **kwargs)
    else:
      raise KeyError(f"model {type} doesn't exist")
