from enum import Enum

class StrategyEnum(Enum):
    """
    Enum of supported authentication strategies.

    Last Updated: 2026-03-14
    """

    JWT = 'jwt'
    SESSION = 'session'
    TOKEN = 'token'
    BASIC = 'basic'


class TokenModelEnum(Enum):
    """
    Enum of supported token models.

    Last Updated: 2026-03-14
    """

    ACCESS = 'access'
    ACCESS_REFRESH = 'access_refresh'
    APIKEY = 'apikey'

