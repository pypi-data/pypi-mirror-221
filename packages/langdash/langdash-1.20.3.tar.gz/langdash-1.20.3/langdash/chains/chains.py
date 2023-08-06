import copy
import re
import typing
import warnings
from collections import OrderedDict
from dataclasses import dataclass
from typing import (
  TYPE_CHECKING, Any, Dict, FrozenSet, Generator, List, Optional, Set, Tuple
)
from typing import Type as _Type
from typing import TypeVar, Union, cast

from langdash.response import (
  RespChoice, RespInferEnd, RespInject, Response, RespReturns, RespSubchain
)
from langdash.infer import InferEndSequence

from .nodes import (
  LDArg, LDChoice, LDFormatArg, LDNode, LDRepeat, LDReturns, LDText
)
from .typing import Type, TypeDictOrDataclass, TypeDictView, _to_typedict

if TYPE_CHECKING:
  from langdash.core import Langdash
  from langdash.llm_session import LLMGenerationSession, LLMState

RE_FIRST_CONST = re.compile(r"^((?:[^{]|{{)+)")
RE_IDENT = re.compile(r"^({[a-zA-Z_][a-zA-Z0-9_]*})")
RE_FORMAT_ARG = re.compile(r"^({[^}]+})")

LDNodeGenerator = Generator[Response, None, None]
LDNodeArgs = Dict[str, Any]
LDNodeArgsFrozen = FrozenSet[Tuple[str, Any]]


class LDChain:
  """ Class used to represent language chains """

  def __init__(
    self,
    ld: "Langdash",
    nodes: List[Union["LDNode", str]],
    args: TypeDictOrDataclass = {},
    returns: TypeDictOrDataclass = {},
  ):
    self._ld = ld
    self._args = _to_typedict(args)
    self._returns = _to_typedict(returns)
    assert len(nodes) > 0, "at least one node must be given to chain"
    self._nodes = self._preprocess_nodes(nodes)

  def cached(self, model: str, **model_kwargs) -> "LDChainCached":
    """
    Cache the chain for a specific model
    
    Args:
      model (str): The model name
      
    Returns:
      The cached chain
    """
    return LDChainCached(
      model=model,
      model_kwargs=model_kwargs,
      _ld=self._ld,
      _args=self._args,
      _returns=self._returns,
      _nodes=self._nodes,
    )

  def arg_type(self, name: str) -> Optional[Type]:
    """
    Return the type of the argument.
    """
    return self._args.get(name)

  def arg_items(self) -> TypeDictView:
    """
    Returns the item view of the argument dictionary.
    """
    return self._args.items()

  def return_type(self, name: str) -> Optional[Type]:
    """
    Return the type of the return variable.
    """
    return self._returns.get(name)

  def return_items(self) -> TypeDictView:
    """
    Returns the item view of the return variable dictionary.
    """
    return self._returns.items()

  def _preprocess_nodes(
    self,
    nodes: List[Union["LDNode", InferEndSequence]],
  ) -> List["LDNode"]:
    pp_nodes: List[Optional[LDNode]] = []

    def _preprocess_format_arg(node: LDFormatArg):
      text = node._text
      while text:
        matches = RE_FIRST_CONST.match(text)
        skip = 0
        if matches:
          skip = len(matches.group(0))
          pp_nodes.append(self._ld.text(matches.group(0)))
        else:
          matches = RE_IDENT.match(text)
          if matches:
            ident = matches.group(0)[1:-1]
            skip = len(matches.group(0))
            pp_nodes.append(self._ld.arg(ident))
          else:
            matches = RE_FORMAT_ARG.match(text)
            if matches:
              fmt = matches.group(0)
              skip = len(matches.group(0))
              pp_nodes.append(self._ld.format_args(fmt))
            else:
              pp_nodes.append(self._ld.format_args(text))
              break
        text = text[skip:]

    # create pp_nodes
    for node in nodes:
      if isinstance(node, LDNode):
        pp_nodes.append(node)
      elif isinstance(node, LDFormatArg):
        _preprocess_format_arg(node)
      else:
        pp_nodes.append(self._ld.text(node))

    # variable/type checking
    for i, node in enumerate(nodes):
      if isinstance(node, LDArg):
        if node._arg not in self._args:
          raise ValueError(f"'{node._arg}' not found in argument declaration")

      elif isinstance(node, LDChoice):
        if node._returns not in self._returns:
          raise ValueError(
            f"'{node._returns}' not found in return declaration"
          )
        if node._return_idx:
          if i != len(nodes) - 1:
            raise ValueError(
              f"expected LDChoice node with return_idx to be in last position (index is {i})"
            )
          if self._returns[node._returns] is not int:
            raise TypeError(f"return type of '{node._returns}' should be int")

      elif isinstance(node, LDRepeat):
        if node._append_target not in self._returns:
          raise ValueError(
            f"'{node._append_target}' not found in return declaration"
          )
        rettype = self._returns[node._append_target]
        if (rettype is not list) and (typing.get_origin(rettype) is not list):
          raise TypeError(
            f"return type of '{node._append_target}' should be a list"
          )

      elif isinstance(node, LDReturns):
        if node._returns not in self._returns:
          raise ValueError(
            f"'{node._returns}' not found in return declaration"
          )
        if node._maybe_from_args and node._returns not in self._args:
          raise ValueError(
            f"'{node._returns}' not found in argument declaration"
          )

    # fuse text nodes
    for i in range(len(pp_nodes)):
      pp_node_i = pp_nodes[i]
      if isinstance(pp_node_i, LDText) and isinstance(pp_node_i._text, str):
        for j in range(i + 1, len(pp_nodes)):
          pp_node_j = pp_nodes[j]
          if not isinstance(pp_node_j, LDText):
            break
          if not isinstance(pp_node_j._text, str):
            break
          pp_node_i._text += pp_node_j._text
          pp_node_j = None

    # filter
    pp_nodes = [node for node in pp_nodes if node is not None]

    return cast(List[LDNode], pp_nodes)

  def _node_pass(self, session: "LLMGenerationSession", args: LDNodeArgs):
    yield from iter(self._nodes)

  def _load_session(
    self, ctx: Union[str, "LLMGenerationSession"]
  ) -> "LLMGenerationSession":
    from langdash.llm_session import LLMGenerationSession
    if isinstance(ctx, LLMGenerationSession):
      return cast(LLMGenerationSession, ctx)
    else:
      session = self._ld.session_for_model(ctx)
      assert isinstance(
        session, LLMGenerationSession
      ), "context must be LLMGenerationSession"
      return session

  def _stream(self, session: "LLMGenerationSession", args: LDNodeArgs = {},) \
    -> Generator[Response, None, None]:
    for node in self._node_pass(session, args):
      if isinstance(node, (LDReturns, LDChoice)):
        yield RespReturns(key=node._returns)
      yield from node(session, args)

  def stream(self, ctx: Union[str, "LLMGenerationSession"], **kwargs) \
    -> Generator[Response, None, None]:
    """
    Stream data generated from the LLM within the specified session.
    
    Args:
      session (Union[str, "LLMGenerationSession"]):
        The name of the model, or an existing LLM generation session.
      args (LDNodeArgs):
        Arguments to pass to the chain. This will be used by any argument or format nodes.
    
    Returns:
      Generator yielding response events.
    """
    return self._stream(session=self._load_session(ctx), **kwargs)

  def _call(
    self,
    session: "LLMGenerationSession",
    args: LDNodeArgs = {},
    return_session: bool = False,
  ) -> Union["LDResult", Tuple["LDResult", "LLMGenerationSession"]]:
    result = LDResult()

    for node in self._node_pass(session, args):
      generator = node(session, args)

      if isinstance(node, LDReturns):
        text = ""
        for resp in generator:
          if isinstance(resp, RespInferEnd):
            text = resp.running_infer
            result.completion_tokens += resp.tokens_counter
        result.returns[node._returns] = self._returns[node._returns](text)

      elif isinstance(node, LDChoice):
        resp = next(generator)
        if isinstance(resp, RespInferEnd):
          result.completion_tokens += resp.tokens_counter
          result.returns[node._returns] = self._returns[node._returns](
            resp.running_infer
          )
        elif isinstance(resp, RespChoice):
          result.completion_tokens += resp.tokens_counter
          result.returns[node._returns] = resp.choice
        else:
          assert False

      elif isinstance(node, LDRepeat):
        text = ""
        result_list = []

        if node._append_source is not None:
          # simple repeat chain
          for resp in generator:
            assert (isinstance(resp, RespSubchain))
            resp_subchain = resp.resp_subchain
            if isinstance(resp_subchain, RespInferEnd):
              result_list.append(resp_subchain.running_infer)
              result.completion_tokens += resp_subchain.tokens_counter
            elif isinstance(resp_subchain, RespInject):
              result.prompt_tokens += resp_subchain.tokens_counter
        else:
          # TODO
          raise NotImplementedError("node._append_source is None")

        rettype = self._returns[node._append_target]
        if rettype is list:
          result.returns[node._append_target] = result_list
        else:
          result.returns[node._append_target] = list(map(rettype, result_list))
      else:
        for resp in generator:
          if isinstance(resp, RespInject):
            result.prompt_tokens += resp.tokens_counter
          else:
            raise NotImplementedError(resp.__class__.__name__)

    if return_session:
      return result, session
    return result

  def call(self, ctx: Union[str, "LLMGenerationSession"], **kwargs):
    """
    Returns data generated from the LLM within the specified session.
    
    Args:
      ctx (Union[str, "LLMGenerationSession"]):
        The name of the model, or an existing LLM generation session.
      args (LDNodeArgs):
        Arguments to pass to the chain. This will be used by any argument or format nodes.
      return_session (bool):
        Whether or not to return the generation session after generation.
    
    Returns:
      The result, or a tuple with (result, session).
    """
    return self._call(session=self._load_session(ctx), **kwargs)


@dataclass
class _LDChainCacheState:
  state: "LLMState"
  skip_nodes: int


_LDChainCacheStoreDict = OrderedDict[FrozenSet[Tuple[str, Any]],
                                     _LDChainCacheState]


@dataclass(frozen=True)
class LDChainCacheStore:
  _dict: _LDChainCacheStoreDict
  _model: str
  _model_kwargs: dict


class LDChainCached(LDChain):

  arguments_to_cache: Optional[Set[str]]

  def __init__(self, model: str, model_kwargs: dict, **kwargs):
    for k, v in kwargs.items():
      setattr(self, k, v)

    self._model = model
    self._model_kwargs = model_kwargs

    # track the first index where the argument is first used
    _arg_first_used_at = {k: -1 for k in self._args.keys()}
    # track the first index where any argument is used
    self._any_arg_first_use = 0
    for idx, node in enumerate(self._nodes):
      if isinstance(node, LDArg) and _arg_first_used_at[node._arg] == -1:
        _arg_first_used_at[node._arg] = idx
      if isinstance(
        node, (LDArg, LDFormatArg)
      ) and self._any_arg_first_use == 0:
        self._any_arg_first_use = idx
    # set min(_arg_first_used_at.values) == self._any_arg_first_use
    for k, v in _arg_first_used_at.items():
      if v == -1:
        _arg_first_used_at[k] = self._any_arg_first_use

    self._arg_first_used_at: Dict[str, int] = _arg_first_used_at
    self._arg_first_used_at_ordered: List[str] = list(
      _arg_first_used_at.keys()
    )
    self._arg_first_used_at_ordered.sort(key=lambda k: _arg_first_used_at[k])
    self.arguments_to_cache = None

    # cache session per argument use
    self._state_cache: _LDChainCacheStoreDict = OrderedDict()
    if len(self._args) == 0:
      self.max_states_to_cache = 1
    else:
      self.max_states_to_cache = min(len(self._args) + 2, 8)

    self._skip_nodes = 0

  # State cache functions

  def load_cache_store(self, cache_store: LDChainCacheStore):
    """
    Loads the cache store from previous inference time.
    
    .. warning::
      This function expects that the model data of the parent `Langdash`
      instance does not change across session. If it does, a `UserWarning`
      is emitted.
    
    Args:
      cache_store (LDChainCacheStore): The cache store.
    
    Raises:
      ValueError: If the model name of the cache store doesn't match.
    """
    if self._model != cache_store._model:
      raise ValueError("model mismatch for LDChainCacheStore")
    if self._model_kwargs != cache_store._model_kwargs:
      warnings.warn(
        "model kwargs does not match LDChainCacheStore, unexpected behavior might occur"
      )
    self._state_cache = cache_store._dict

  def save_cache_store(self) -> LDChainCacheStore:
    """ Saves the cache store into an object. """
    return LDChainCacheStore(
      _dict=copy.deepcopy(self._state_cache),
      _model=self._model,
      _model_kwargs=copy.deepcopy(self._model_kwargs)
    )

  def _set_state_cache(
    self, key: FrozenSet[Tuple[str, Any]], value: _LDChainCacheState
  ):
    self._state_cache[key] = value
    self._update_state_cache(key)
    if len(self._state_cache) > self.max_states_to_cache:
      self._state_cache.popitem(last=True)

  def _update_state_cache(self, key: FrozenSet[Tuple[str, Any]]):
    self._state_cache.move_to_end(key, last=False)

  def _get_state_cache(
    self, key: FrozenSet[Tuple[str, Any]]
  ) -> _LDChainCacheState:
    self._update_state_cache(key)
    return self._state_cache[key]

  def _arg_subset_sorted_by_idx(self, args: LDNodeArgs):
    current_subset: LDNodeArgs = {}
    yield current_subset
    for arg in self._arg_first_used_at_ordered:
      current_subset[arg] = args[arg]
      yield current_subset

  # Inference functions

  def _node_pass(self, session: "LLMGenerationSession", args: LDNodeArgs):
    last_state_key: Optional[_LDChainCacheState] = None
    for i in range(self._skip_nodes, len(self._nodes)):
      node = self._nodes[i]
      yield node
      if isinstance(node, LDText) and last_state_key is not None:
        # should already be non-null after inject
        last_state_key.state = session.clone_state()  # type: ignore
        last_state_key.skip_nodes = (i + 1)
      elif isinstance(node, LDArg) and self.max_states_to_cache > 0:
        if self.arguments_to_cache is not None and node._arg not in self.arguments_to_cache:
          last_state_key = None
          continue

        # Do not update the cache if argument is injected the second time
        cached_idx = self._arg_first_used_at[node._arg]
        if i > cached_idx:
          last_state_key = None
          continue

        # TODO: there might be a faster way of doing this
        # if the frozenset from _arg_subset_sorted_by_idx is used
        current_keys = frozenset(
          (k, v)
          for k, v in args.items()
          if self._arg_first_used_at[k] <= cached_idx
        )

        if current_keys not in self._state_cache:
          self._set_state_cache(
            current_keys,
            _LDChainCacheState(
              # should already be non-null after inject
              state=session.clone_state(),  # type: ignore
              skip_nodes=(cached_idx + 1)
            )
          )
        else:
          self._update_state_cache(current_keys)
        last_state_key = self._state_cache[current_keys]
      else:
        last_state_key = None

  def _create_new_session(self) -> "LLMGenerationSession":
    ctx = self._ld.session_for_model(self._model, **self._model_kwargs)
    from langdash.llm_session import LLMGenerationSession
    assert isinstance(
      ctx, LLMGenerationSession
    ), "context must be LLMGenerationSession"
    return ctx

  def _load_gen_session(
    self, args: Optional[LDNodeArgs] = None
  ) -> "LLMGenerationSession":
    session = self._create_new_session()

    if frozenset() not in self._state_cache:
      text_node = self._nodes[0]

      if isinstance(text_node, LDText):
        session.inject(text_node._text)
        self._set_state_cache(
          frozenset(),
          _LDChainCacheState(
            # should already be non-null after inject
            state=session.clone_state(),  # type: ignore
            skip_nodes=1
          )
        )
        self._skip_nodes = 1

      return session

    if args is None:
      old_state_cache = self._get_state_cache(frozenset())
      self._skip_nodes = old_state_cache.skip_nodes
      session.set_state(old_state_cache.state)
      return session
    else:
      for subset in self._arg_subset_sorted_by_idx(args):
        subset_frozen = frozenset(subset.items())
        if subset_frozen not in self._state_cache:
          break
        old_state_cache = self._get_state_cache(subset_frozen)

      session.set_state(old_state_cache.state)
      self._skip_nodes = old_state_cache.skip_nodes
      return session

  def stream(self, **kwargs):
    return super()._stream(
      session=self._load_gen_session(args=kwargs.get("args")), **kwargs
    )

  def call(self, **kwargs):
    return super()._call(
      session=self._load_gen_session(args=kwargs.get("args")), **kwargs
    )


T_ReturnsClass = TypeVar('T_ReturnsClass')


@dataclass
class LDResult:
  """
  Class for storing the results of inference.
  
  Attributes:
    returns: Mapping of return keys to return values
    prompt_tokens: Number of tokens injected to the language model
    completion_tokens: Number of tokens generated by the language model
  """

  returns: Dict[str, Any]
  prompt_tokens: int
  completion_tokens: int

  def __init__(self):
    self.returns = {}
    self.prompt_tokens = 0
    self.completion_tokens = 0

  def into(self, cls: _Type[T_ReturnsClass]) -> T_ReturnsClass:
    return cls(**self.returns)
