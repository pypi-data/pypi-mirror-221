from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING, Dict, Generator, List, Optional

from langdash.response import RespInferEnd, RespInject, Response

if TYPE_CHECKING:
  from langdash.chains import LDChain
  from langdash.llm_session import LLMGenerationSession


class Role(Enum):
  System = auto()
  User = auto()
  Bot = auto()


@dataclass
class Message:
  role: Role
  content: str
  tokens_counter: int


class ChatCompletion:

  def __init__(
    self,
    init_session: "LLMGenerationSession",
    chain_by_role: Dict[Role, "LDChain"],
  ):
    self._init_session = init_session
    self._chain_by_role = chain_by_role

  def session(self, **kwargs) -> "ChatCompletionSession":
    return ChatCompletionSession(self, **kwargs)


class ChatCompletionSession:

  messages: List[Message]

  def __init__(
    self,
    cc: ChatCompletion,
    max_context_length: int = -1,
    keep_only_last_state: bool = False
  ):
    self._cc = cc
    self._session = self._cc._init_session.clone()
    self.max_context_length = max_context_length
    self.messages = []
    self._messages_start = 0
    self._last_message_has_save = False
    self.keep_only_last_state = keep_only_last_state

  def _on_before_new_message(self):
    # Remove older messages
    if self.max_context_length != -1 and self._session.tokens_used >= self.max_context_length:
      tokens_used = self._cc._init_session.tokens_used
      self._messages_start = len(self.messages)
      while tokens_used < self.max_context_length:
        self._messages_start -= 1
        tokens_used += self.messages[self._messages_start].tokens_counter

      self._session.set_state(self._cc._init_session.clone_state())
      self._session.tokens_used = tokens_used
      for message in self.messages[self._messages_start:]:
        chain = self._cc._chain_by_role[message.role]
        chain.call(self._session, args={"content": message.content})

    # Keep only last state
    if self.keep_only_last_state and self._last_message_has_save:
      delattr(self.messages[-1], "_state")
      self._last_message_has_save = False

  def reset(self):
    self._session.set_state(self._cc._init_session.clone_state())
    self._session.tokens_used = self._cc._init_session.tokens_used

  def stream(
    self,
    role: Optional[Role] = None,
    content: Optional[str] = None,
    save_state: bool = False,
    load_last_state: bool = False,
  ) -> Generator[Response, None, Message]:
    self._on_before_new_message()

    state = None
    
    if load_last_state:
      last_message = self.messages.pop()
      self._session.set_state(last_message._state)
      if save_state:
        state = last_message._state
      role = last_message.role
      content = None
    else:
      if save_state:
        state = self._session.clone_state()
      if role is None:
        raise ValueError(
          "role should not be None when load_last_state is False"
        )

    chain = self._cc._chain_by_role[role]
    if content is None:
      tokens_counter = 0
      content = ""
      for resp in chain.stream(self._session):
        yield resp
        if isinstance(resp, RespInferEnd):
          content += resp.running_infer
          tokens_counter += resp.tokens_counter
        elif isinstance(resp, RespInject):
          tokens_counter += resp.tokens_counter
      message = Message(
        role=role, content=content, tokens_counter=tokens_counter
      )
    else:
      tokens_counter = 0
      for resp in chain.stream(self._session, args={"content": content}):
        yield resp
        if isinstance(resp, RespInject):
          tokens_counter += resp.tokens_counter
      message = Message(
        role=role, content=content, tokens_counter=tokens_counter
      )

    if save_state:
      message._state = state
      self._last_message_has_save = True
    else:
      self._last_message_has_save = False

    self.messages.append(message)
    return message

  def call(self, *args, **kwargs) -> Message:
    generator = self.stream(*args, **kwargs)
    try:
      while True:
        next(generator)
    except StopIteration as stop:
      return stop.value
