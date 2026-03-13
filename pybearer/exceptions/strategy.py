from .base import PyBearerError

class StrategyError(PyBearerError):
    """
    Strategy Error:
        This is the base class for all strategy errors.
        Meaning that the strategy is not valid.

    Last Updated: 2026-03-13
    """

    error_code = (
        'STRATEGY_ERROR'
    )