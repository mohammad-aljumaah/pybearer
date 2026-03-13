


class PyBearer:
    """

    Last Updated: 2026-03-13
    """
    def __init__(self, secret: str, strategy: str):
        self.secret = secret
        self.strategy = self._get_strategy(strategy)


    def _get_strategy(strategy: str):
        strategy = strategy.lower()

        match strategy:
           case "jwt":
               #return JWTStrategy()
                ...
           case "session":
               #return SessionStrategy()
               ...
           case "token":
               #return TokenStrategy()
               ...
           case "basic":
               #return BasicStrategy()
               ...
           case _:
               raise ValueError("Invalid strategy") # May be we add a custom exception

