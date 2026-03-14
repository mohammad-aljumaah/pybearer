from .base import PyBearerError

class TokenModelError(PyBearerError):
    """
    Base exception for authentication Token Models errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'TOKEN_MODEL_ERROR'
    )

class InvalidTokenModelError(TokenModelError):
    """
    Raised when the token model is invalid.

    Last Updated: 2026-03-14
    """

    error_code = (
        'INVALID_TOKEN_MODEL'
    )