from .base import PyBearerError

class ConfigurationError(PyBearerError):
    """
    Base exception for PyBearer configuration errors.

    Last Updated: 2026-03-14
    """

    category_error = error_code = (
        'CONFIGURATION_ERROR'
    )


class LoadUserNotConfiguredError(ConfigurationError):
    """
    Raised when the `load_user` hook is not configured.

    Last Updated: 2026-03-14
    """

    error_code = (
        'LOAD_USER_NOT_CONFIGURED'
    )


class VerifyPasswordNotConfiguredError(ConfigurationError):
    """
    Raised when the `verify_password` hook is not configured.

    Last Updated: 2026-03-14
    """

    error_code = (
        'VERIFY_PASSWORD_NOT_CONFIGURED'
    )