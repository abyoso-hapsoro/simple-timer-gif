import sys
from typing import Union, Tuple


def _set_traceback_limit(n: int = 1000) -> None:
    """
    Helper function to set maximum number of levels of traceback information printed when an exception occurs.

    Args:
        n (int, optional):
            Traceback limit. Defaults to 1000.
    """
    
    # sys.tracebacklimit = n
    setattr(sys, 'tracebacklimit', n)


def _reset_traceback_limit() -> None:
    """
    Safety function to reset maximum number of levels of traceback information to default.
    """
    
    # sys.tracebacklimit = 1000
    delattr(sys, 'tracebacklimit')


def validate_input(
    duration: int,
    warning: int,
    result_path: str,
    color: Union[str, Tuple[int, ...]]
) -> None:
    """
    Validate arguments passed to `main.py`
    """

    # Set no traceback — only printing the AssertionError during exceptions
    _set_traceback_limit(0)

    # Validate duration
    assert isinstance(duration, int), 'Duration must be integer.'
    assert 1 <= duration <= 999, 'Duration must be between 1 and 999 inclusive.'

    # Validate warning
    assert isinstance(warning, int), 'Warning must be integer.'
    if warning != -1:
        assert 1 <= warning <= duration - 1, 'Warning must be between 1 and duration - 1 inclusive.'
    
    # Validate result path
    if result_path:
        assert isinstance(result_path, str), 'Result path must be string.'
    
    # Validate color
    if color:
        assert type(color) in [str, tuple], 'Color must be string or RGBA tuple.'
        if isinstance(color, tuple):
            assert len(color) == 4, 'Color defined by RGBA tuple must be exactly 4 elements.'
            assert all(isinstance(c, int) for c in color), 'Color defined by RGBA tuple must have all integer elements.'
