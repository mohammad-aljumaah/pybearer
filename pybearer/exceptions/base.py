class PyBearerError(Exception):
    """
    Base exception for all PyBearer errors.

    Attributes
    ----------
    message : str
        Human-readable error message.

    Last Updated: 2026-03-14
    """

    category_error = 'PYBEARER_ERROR'

    error_code = 'PYBEARER_ERROR'

    def __init__(self, message: str | None = None):
        self.message = message or "An unknown PyBearer error occurred"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.category_error} [{self.error_code}] {self.message}"


class PyBearerNotImplementedError(PyBearerError):
    """
    Raised when a PyBearer feature or service is not implemented yet.

    Last Updated: 2026-03-14
    """

    error_code = (
        'NOT_IMPLEMENTED'
    )