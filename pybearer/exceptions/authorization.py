from .base import PyBearerError

class AuthorizationError(PyBearerError):
    """
    Base exception for authorization failures.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'AUTHORIZATION_ERROR'
    )
