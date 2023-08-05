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

  def __init__(self, cc: ChatCompletion, max_context_length: int = -1):
    self._cc = cc
    self._session = self._cc._init_session.clone()
    self.max_context_length = max_context_length
    self.messages = []
    self._messages_start = 0

  def _on_before_new_message(self):
    if self.max_context_length != -1 and self._session.tokens_used >= self.max_context_length:
      tokens_counter = self._cc._init_session.tokens_used
      self._messages_start = len(self.messages)
      while tokens_counter < self.max_context_length:
        self._messages_start -= 1
        tokens_counter += self.messages[self._messages_start].tokens_counter

      self._session.set_state(self._cc._init_session.clone_state())
      for message in self.messages[self._messages_start:]:
        chain = self._cc._chain_by_role[message.role]
        chain.call(self._session, args={"content": message.content})

  def stream(
    self,
    role: Role,
    content: Optional[str] = None,
  ) -> Generator[Response, None, Message]:
    self._on_before_new_message()

    chain = self._cc._chain_by_role[role]
    if content is None:
      tokens_counter = 0
      content = ""
      for resp in chain.stream(self._session, args={"content": content}):
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
      for resp in chain.stream(self._session):
        yield resp
        if isinstance(resp, RespInject):
          tokens_counter += resp.tokens_counter
      message = Message(
        role=role, content=content, tokens_counter=tokens_counter
      )

    self.messages.append(message)
    return message

  def call(
    self,
    role: Role,
    content: Optional[str] = None,
  ) -> Message:
    generator = self.stream(role, content)
    try:
      while True:
        next(generator)
    except StopIteration as stop:
      return stop.value
