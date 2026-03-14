from .base import PyBearerError

class SessionError(PyBearerError):
    """
    Base exception for session-related errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'SESSION_ERROR'
    )

