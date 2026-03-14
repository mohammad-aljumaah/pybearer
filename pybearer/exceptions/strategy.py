from .base import PyBearerError

class StrategyError(PyBearerError):
    """
    Base exception for authentication strategy errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'STRATEGY_ERROR'
    )


class InvalidStrategyError(StrategyError):
    """
    Raised when an unsupported authentication strategy is requested.

    Last Updated: 2026-03-14
    """

    error_code = (
        'INVALID_STRATEGY'
    )