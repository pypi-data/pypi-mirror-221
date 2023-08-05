from typing import Callable, Optional

import numpy as np
import numpy.typing as npt
from numpy import floating, integer
from numpy.lib.npyio import NpzFile
from pydantic import FilePath


def create_array_validator(
    dimensions: Optional[int], target_data_type: npt.DTypeLike, strict_data_typing: bool
) -> Callable[[npt.NDArray], npt.NDArray]:
    def array_validator(array: npt.NDArray) -> npt.NDArray:
        if dimensions and (array_dimensions := len(array.shape)) != dimensions:
            msg = f"Array {array_dimensions}-dimensional; the target dimensions is {dimensions}"
            raise ValueError(msg)

        if target_data_type and array.dtype.type != target_data_type:
            if strict_data_typing:
                msg = f"{array.dtype.type} does not coincide with strict type hint, {target_data_type}"
                raise AttributeError(msg)

            if issubclass(_resolve_type_of_array_dtype(target_data_type), integer) and issubclass(
                _resolve_type_of_array_dtype(array.dtype), floating
            ):
                array = np.round(array).astype(target_data_type, copy=False)
            else:
                array = array.astype(target_data_type, copy=True)

        return array

    return array_validator


def read_and_verify_numpy_file(v: FilePath) -> npt.NDArray:
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


def _resolve_type_of_array_dtype(array_dtype: npt.DTypeLike) -> type:
    if hasattr(array_dtype, "type"):
        return array_dtype.type
    else:
        return array_dtype
