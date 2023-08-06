from functools import singledispatch
from typing import Any

import numpy as np

from .core import TatamiNumericPointer
from .utils import map_order_to_bool

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"


@singledispatch
def tatamize(x: Any, order: str = "C") -> TatamiNumericPointer:
    """Converts python matrix representations to tatami.

    Args:
        x (Any): Any matrix-like object.
        order (str): dense matrix representation, ‘C’, ‘F’,
            row-major (C-style) or column-major (Fortran-style) order.

    Raises:
        NotImplementedError: if x is not supported

    Returns:
        TatamiNumericPointer: a pointer to tatami object.
    """
    raise NotImplementedError(
        f"tatamize is not supported for objects of class: {type(x)}"
    )


@tatamize.register
def _tatamize_numpy(x: np.ndarray, order: str = "C") -> TatamiNumericPointer:
    order_to_bool = map_order_to_bool(order=order)
    return TatamiNumericPointer.from_dense(x.shape[0], x.shape[1], x, order_to_bool)
