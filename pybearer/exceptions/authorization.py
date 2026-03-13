from .base import PyBearerError

class AuthorizationError(PyBearerError):
    """
    Authorization Error:
        This is the base class for all authorization errors.
        Meaning that the user is not authorized to perform the action.

    Last Updated: 2026-03-13
    """

    error_code = (
        'AUTHORIZATION_ERROR'
    )
