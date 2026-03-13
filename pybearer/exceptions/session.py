from .base import PyBearerError

class SessionError(PyBearerError):
    """
    Session Error:
        This is the base class for all session errors.
        Meaning that the session is not valid.

    Last Updated: 2026-03-13
    """

    error_code = (
        'SESSION_ERROR'
    )

