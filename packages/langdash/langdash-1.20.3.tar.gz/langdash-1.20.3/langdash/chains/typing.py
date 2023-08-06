import dataclasses
from typing import Any, Callable, Dict, ItemsView
from typing import Type as _Type
from typing import Union, cast

Type = Callable[[str], Any]
TypeDict = Dict[str, Type]
TypeDictView = ItemsView[str, Type]

TypeDictOrDataclass = Union[TypeDict, _Type]


def _to_typedict(val: TypeDictOrDataclass) -> TypeDict:
  if isinstance(val, dict):
    return val
  assert dataclasses.is_dataclass(val)
  newval = {}
  for field in dataclasses.fields(val):
    newval[field.name] = cast(Type, field.type)
  return newval


class Mapping:
  """
  Helper type for mapping string into value.
  """

  def __init__(self, mapping: Dict[str, Any]):
    self.mapping = mapping

  def __call__(self, input: str):
    return self.mapping[input]
