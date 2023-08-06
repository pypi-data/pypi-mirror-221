from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Self

from pydantic.fields import Field, FieldInfo


class MarshalField:
    """
    Basic boilerplate class for all pydantic-marshals' models' fields.
    This is an interface, and it requires implementing all methods to function
    and to be used in :py:class:`pydantic_marshals.models.base.MarshalModel`
    """

    def __init__(self, alias: str | None = None) -> None:
        """
        :param alias: same as Field(alias=...), can be None for no alias
        """
        self.alias = alias

    @classmethod
    def convert(cls, *source: Any) -> Self | None:
        """
        Convert something into a field.
        If conversion is not possible, this method should return None
        """
        raise NotImplementedError

    def generate_name(self) -> str:
        """
        Generates the name for the field, used in
        :py:meth:`pydantic_marshals.models.base.MarshalModel.generate_model`
        """
        raise NotImplementedError

    def generate_type(self) -> type:
        """
        Generates the type annotation for the field, used in
        :py:meth:`pydantic_marshals.models.base.MarshalModel.generate_model`
        """
        raise NotImplementedError

    # TODO type with TypedDict? Use _FieldInfoInputs?
    def generate_field_data(self) -> Iterator[tuple[str, Any]]:
        """
        Generates field data (kwargs for :py:func:`pydantic.fields.Field`),
        and returns it in the for of an Iterator,
        compatible with the ``dict[str, Any]`` constructor

        Kwarg names and types can be found in
        :py:class:`pydantic.fields._FieldInfoInputs`
        """
        yield "alias", self.alias

    def generate_field(self) -> tuple[type, FieldInfo]:
        """
        Generates field info for the field, used in
        :py:meth:`pydantic_marshals.models.base.MarshalModel.generate_model`
        """
        return (
            self.generate_type(),
            Field(**dict(self.generate_field_data())),
        )
