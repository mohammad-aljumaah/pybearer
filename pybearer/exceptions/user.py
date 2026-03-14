from .base import PyBearerError

class UserError(PyBearerError):
    """
    Base exception for user-related errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'USER_ERROR'
    )