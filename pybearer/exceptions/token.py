from .base import PyBearerError

class TokenError(PyBearerError):
    """
    Token Error:
        This is the base class for all token errors.
        Meaning that the token is not valid.

    Last Updated: 2026-03-13
    """

    error_code = (
        'TOKEN_ERROR'
    )