from typing import Protocol, runtime_checkable, Any

@runtime_checkable
class UserProtocol(Protocol):
    """
    Minimal user contract required by PyBearer.
    """

    id: Any

