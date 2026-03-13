class PyBearerError(Exception):
    """
    PyBearer Error:
        This is the base class for all PyBearer errors

    Attributes:
        message (str): The error message

    Last Updated: 2026-03-13
    """

    error_code = 'PYBEARER_ERROR'

    def __init__(self, message: str | None = None):
        self.message = message or "An unknown PyBearer error occurred"
        super().__init__(self.message)

    def __str__(self):
        return f"PyBearer ERROR:\n[{self.error_code}] {self.message}"