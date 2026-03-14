
class StrategyRegistry:

    _strategies = {}

    @classmethod
    def register(cls, name: str, strategy):

        cls._strategies[name] = strategy

    @classmethod
    def get(cls, name: str):

        return cls._strategies[name]

    @classmethod
    def available(cls):
        return list(cls._strategies.keys())