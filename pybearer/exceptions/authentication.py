from .base import PyBearerError

class AuthenticationError(PyBearerError):
    """
    Authentication Error:
        This is the base class for all authentication errors.
        Meaning that the user is not authenticated.

    Last Updated: 2026-03-13
    """

    error_code = (
        'AUTHENTICATION_ERROR'
    )