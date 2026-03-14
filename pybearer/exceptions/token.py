from .base import PyBearerError

class TokenError(PyBearerError):
    """
    Base exception for token-related errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'TOKEN_ERROR'
    )