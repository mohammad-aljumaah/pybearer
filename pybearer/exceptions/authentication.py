from .base import PyBearerError

class AuthenticationError(PyBearerError):
    """
    Base exception for authentication failures.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'AUTHENTICATION_ERROR'
    )


class UserNotFoundError(AuthenticationError):
    """
    Raised when no user is found for the provided identifier.

    Last Updated: 2026-03-14
    """

    error_code = (
        'USER_NOT_FOUND'
    )

class InvalidCredentialsError(AuthenticationError):
    """
    Raised when credential verification fails.

    Last Updated: 2026-03-14
    """

    error_code = (
        'INVALID_CREDENTIALS'
    )
