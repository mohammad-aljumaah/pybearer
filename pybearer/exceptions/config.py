from .base import PyBearerError

class ConfigurationError(PyBearerError):
    """
    Configuration Error:
        This is the base class for all configuration errors.
        Meaning that the configuration is not valid.

    Last Updated: 2026-03-13
    """
    error_code = (
        'CONFIGURATION_ERROR'
    )