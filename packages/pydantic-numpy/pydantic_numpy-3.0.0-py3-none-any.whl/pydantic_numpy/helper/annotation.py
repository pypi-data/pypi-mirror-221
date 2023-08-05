from collections.abc import Sequence
from pathlib import Path
from typing import Any, Callable, ClassVar, Optional, Union

import numpy as np
import numpy.typing as npt
from numpy.lib.npyio import NpzFile
from numpy.typing import DTypeLike
from pydantic import FilePath, GetJsonSchemaHandler, PositiveInt
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from typing_extensions import Annotated

from pydantic_numpy.helper.validation import (
    create_array_validator,
    read_and_verify_numpy_file,
)


class NpArrayPydanticAnnotation:
    dimensions: ClassVar[Optional[PositiveInt]]

    data_type: ClassVar[DTypeLike]
    strict_data_typing: ClassVar[bool]

    @classmethod
    def factory(cls, *, data_type: DTypeLike, dimensions: Optional[int], strict_data_typing: bool = False) -> type:
        """
        Create an instance NpArrayPydanticAnnotation that is configured for a specific dimension and dtype.

        The signature of the function is data_type, dimension and not dimension, data_type to reduce amount of
        code for all the types.

        Parameters
        ----------
        data_type: DTypeLike
        dimensions: Optional[int]
            Number of dimensions determine the depth of the numpy array.
        strict_data_typing: bool
            If True, the dtype of the numpy array must be identical to the data_type. No conversion attempts.

        Returns
        -------
        NpArrayPydanticAnnotation
        """
        if strict_data_typing and not data_type:
            msg = "Strict data typing requires data_type (DTypeLike) definition"
            raise ValueError(msg)

        return type(
            (
                f"Np{'Strict' if strict_data_typing else ''}{dimensions or 'N'}DArray"
                f"{data_type.__name__.capitalize() if data_type else ''}PydanticAnnotation"
            ),
            (cls,),
            {"dimensions": dimensions, "data_type": data_type, "strict_data_typing": strict_data_typing},
        )

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Callable[[Any], core_schema.CoreSchema],
    ) -> core_schema.CoreSchema:
        np_array_validator = create_array_validator(cls.dimensions, cls.data_type, cls.strict_data_typing)
        np_array_schema = core_schema.no_info_plain_validator_function(np_array_validator)

        return core_schema.json_or_python_schema(
            python_schema=core_schema.chain_schema(
                [
                    core_schema.union_schema(
                        [
                            core_schema.chain_schema(
                                [
                                    core_schema.is_instance_schema(Path),
                                    core_schema.no_info_plain_validator_function(read_and_verify_numpy_file),
                                ]
                            ),
                            core_schema.is_instance_schema(np.ndarray),
                            core_schema.chain_schema(
                                [
                                    core_schema.is_instance_schema(Sequence),
                                    core_schema.no_info_plain_validator_function(lambda v: np.asarray(v)),
                                ]
                            ),
                        ]
                    ),
                    np_array_schema,
                ]
            ),
            json_schema=np_array_schema,
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda arr: np.array2string(arr), when_used="json"
            ),
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, _core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return handler(
            dict(
                type=(
                    f"np.ndarray[{_int_to_dim_type[cls.dimensions] if cls.dimensions else 'Any'}, "
                    f"{np.dtype[cls.data_type.__name__] if _data_type_resolver(cls.data_type) else cls.data_type}]"
                ),
                strict_data_typing=cls.strict_data_typing,
            )
        )


def np_array_pydantic_annotated_typing(
    data_type: DTypeLike = None, dimensions: Optional[int] = None, strict_data_typing: bool = False
):
    return Annotated[
        Union[
            FilePath,
            np.ndarray[
                _int_to_dim_type[dimensions] if dimensions else Any,
                np.dtype[data_type] if _data_type_resolver(data_type) else data_type,
            ],
        ],
        NpArrayPydanticAnnotation.factory(
            data_type=data_type, dimensions=dimensions, strict_data_typing=strict_data_typing
        ),
    ]


def _data_type_resolver(data_type: DTypeLike):
    return data_type is not None and issubclass(data_type, np.generic)


def _read_and_verify_numpy_file(v: FilePath) -> npt.NDArray:
    result = np.load(v)

    if isinstance(result, NpzFile):
        files = result.files
        if len(files) > 1:
            msg = (
                f"The provided file path is a multi array NpzFile, which is not supported; "
                f"convert to single array NpzFiles.\n"
                f"Path to multi array file: {result}\n"
                f"Array keys: {', '.join(result.files)}"
            )
            raise ValueError(msg)
        result = result[files[0]]

    return result


_read_and_verify_numpy_file_validator = core_schema.no_info_plain_validator_function(_read_and_verify_numpy_file)
_int_to_dim_type = {1: tuple[int], 2: tuple[int, int], 3: tuple[int, int, int]}
