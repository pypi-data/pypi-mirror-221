"""Filter rules basing on host and device compiler names.
"""

from alpaka_job_coverage.globals import *  # pylint: disable=wildcard-import,unused-wildcard-import
from alpaka_job_coverage.util import row_check_name, is_in_row
from typing import List, Tuple, Union
from typeguard import typechecked


@typechecked
def general_compiler_filter_typed(
    row: List[Union[Tuple[str, str], List[Tuple[str, str]]]]
) -> bool:
    """Type checked version of general_compiler_filter(). Should be only used for
    testing or tooling. The type check adds a big overhead, which slows down
    pair-wise generator by the factor 30.

    Args:
        row (List[Union[Tuple[str, str], List[Tuple[str, str]]]]): Combination
        to verify. The row can contain up to all combination fields and at least
         two items.

    Returns:
        bool: True, if combination is valid, otherwise False.
    """
    return general_compiler_filter(row)


def general_compiler_filter(row: List) -> bool:
    """Filter rules basing on host and device compiler names.

    Args:
        row (List): Combination to verify. The row can contain
        up to all combination fields and at least two items.

    Returns:
        bool: True, if combination is valid, otherwise False.
    """

    # it is not allow to use the nvcc as host compiler
    if row_check_name(row, HOST_COMPILER, "==", NVCC):
        return False

    # only the nvcc allows to combine different host and device compiler
    if (
        is_in_row(row, HOST_COMPILER)
        and is_in_row(row, DEVICE_COMPILER)
        and (
            row[param_map[DEVICE_COMPILER]][NAME] != NVCC
            and row[param_map[HOST_COMPILER]][NAME]
            != row[param_map[DEVICE_COMPILER]][NAME]
        )
    ):
        return False

    # only clang and gcc are allowed as nvcc host compiler
    if row_check_name(row, DEVICE_COMPILER, "==", NVCC) and not (
        row_check_name(row, HOST_COMPILER, "==", GCC)
        or row_check_name(row, HOST_COMPILER, "==", CLANG)
    ):
        return False

    return True
