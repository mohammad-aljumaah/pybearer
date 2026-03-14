from dataclasses import dataclass

@dataclass
class Credential:
    """
    Authentication credential returned by a strategy.

    Attributes
    ----------
    access_token : str
        The primary authentication credential.

    token_type : str
        Credential type, usually "Bearer".

    expires_in : int | None
        Number of seconds until expiration, if applicable.

    refresh_token : str | None
        Optional refresh token.
    """

    access_token: str
    token_type: str
    expires_in: int | None = None
    refresh_token: str | None = None

