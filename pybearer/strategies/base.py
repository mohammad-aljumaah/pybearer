from abc import ABC, abstractmethod
from typing import Any
from ..models import Credential

class AuthStrategy(ABC):
    """
    This is the base class for all strategies.
    Strategies are the way PyBearer handles authentication
    e.g, JWT, Session, etc.

    Strategies:
        - JWT
        - Session
        - Basic Auth
        - Token
        - OAuth
        - API Key

    Abstract Methods:
        - issue
        - revoke
        - verify

    Last Updated: 2026-03-14
    """

    def __init__(self, secret: str):
        self.secret = secret


    @abstractmethod
    def issue(self, user: Any) -> Credential:
        pass

    @abstractmethod
    def verify(self, token: str) -> Any:
        pass

    @abstractmethod
    def revoke(self, token: str) -> None:
        pass

