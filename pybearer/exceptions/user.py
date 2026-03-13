from .base import PyBearerError

class UserError(PyBearerError):
    """
    User Error:
        This is the base class for all user errors.
        Meaning that the user is not valid.

    Last Updated: 2026-03-13
    """

    error_code = (
        'USER_ERROR'
    )