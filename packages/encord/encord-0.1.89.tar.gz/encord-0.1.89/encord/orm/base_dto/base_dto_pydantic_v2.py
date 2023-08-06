from typing import Any, Dict, Type, TypeVar

# TODO: invent some dependency version dependent type checking to get rid of this ignore
from pydantic import ConfigDict  # type: ignore[attr-defined]
from pydantic import BaseModel, ValidationError

from encord.exceptions import EncordException
from encord.objects.utils import _snake_to_camel
from encord.orm.base_dto.base_dto_interface import BaseDTOInterface, T


class BaseDTO(BaseDTOInterface, BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True, alias_generator=_snake_to_camel)

    @classmethod
    def from_dict(cls: Type[T], d: Dict[str, Any]) -> T:
        try:
            return cls.model_validate(d)  # type: ignore[attr-defined]
        except ValidationError as e:
            raise EncordException(message=str(e)) from e

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump(by_alias=True)  # type: ignore[attr-defined]


DataT = TypeVar("DataT")


class GenericBaseDTO(BaseDTOInterface, BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True, alias_generator=_snake_to_camel)

    @classmethod
    def from_dict(cls: Type[T], d: Dict[str, Any]) -> T:
        try:
            return cls.model_validate(d)  # type: ignore[attr-defined]
        except ValidationError as e:
            raise EncordException(message=str(e)) from e

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump(by_alias=True)  # type: ignore[attr-defined]
