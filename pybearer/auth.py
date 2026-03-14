from unittest import case

from .exceptions import (
    PyBearerNotImplementedError,
    # Configuration Errors
    LoadUserNotConfiguredError,
    VerifyPasswordNotConfiguredError,
    # Authentication Errors
    UserNotFoundError,
    InvalidCredentialsError,
    # Strategy Errors
    InvalidStrategyError,
    # Token Model Errors
    InvalidTokenModelError,
)
from .models import Credential
from .strategies.base import AuthStrategy
from .types import UserProtocol
from .enums import StrategyEnum, TokenModelEnum

class PyBearer:
    """
    Core authentication manager for PyBearer.

    PyBearer handles authentication workflows by delegating
    user validation to developer-defined hooks and using
    authentication strategies (JWT, session, token, etc.)
    to generate and verify authentication credentials.

    Developers must configure the following hooks:

    - load_user(identifier) -> returns a user object
    - verify_password(user, password) -> returns bool

    Example:
        auth = PyBearer(secret="secret", strategy="jwt")

        auth.load_user = lambda identifier: db.get_user(identifier)
        auth.verify_password = lambda user, password: verify(password, user.hash)

    Last Updated: 2026-03-14
    """

    def __init__(self, secret: str, strategy: str, model: str | None = 'access'):
        self.secret = secret

        strategy_enum = StrategyEnum(strategy.lower())
        self.strategy = self._get_strategy(strategy)

        if strategy_enum == StrategyEnum.BASIC:
            self.model = None
        else:
            self.model = self._get_token_model(model)


        # Developer Hooks
        self.load_user = None
        self.verify_password = None


    def _get_strategy(self, strategy: str) -> AuthStrategy:
        """
        Resolve and initialize the authentication strategy.

        Parameters
        ----------
        strategy : str
            The name of the authentication strategy to use.
            Supported values: "jwt", "session", "token", "basic".

        Returns
        -------
        AuthStrategy
            An instance of the selected authentication strategy.

        Raises
        ------
        InvalidStrategyError
            If the provided strategy name is not supported.

        PyBearerNotImplementedError
            If the strategy exists but has not been implemented yet.

        Last Updated: 2026-03-14
        """


        try:
            strategy = StrategyEnum(strategy.lower())

        except ValueError:
            raise InvalidStrategyError(
                f"Invalid strategy '{strategy}'. "
                f"Available strategies: {[s.value for s in StrategyEnum]}."
            )

        match strategy:

            case StrategyEnum.JWT:
                raise PyBearerNotImplementedError("JWT strategy is not implemented yet.")

            case StrategyEnum.SESSION:
                raise PyBearerNotImplementedError("Session strategy is not implemented yet.")

            case StrategyEnum.TOKEN:
                raise PyBearerNotImplementedError("Token strategy is not implemented yet.")

            case StrategyEnum.BASIC:
                raise PyBearerNotImplementedError("Basic strategy is not implemented yet.")



    def _get_token_model(self, model: str) -> TokenModelEnum:
        """
        Resolve and initialize the token model.

        Parameters
        ----------
        model : str | None
            The credential model to use.

        Returns
        -------
        TokenModel
            Instance of the selected token model.

        Last Updated: 2026-03-14
        """

        if model is None:
            raise InvalidTokenModelError(
                "Token model must be specified."
            )

        try:

            model = TokenModelEnum(model.lower())

        except ValueError:
            raise InvalidTokenModelError(
                f"Invalid model '{model}'. "
                f"Available models: {[m.value for m in TokenModelEnum]}."
            )

        match model:

            case TokenModelEnum.ACCESS:
                raise PyBearerNotImplementedError("Access token model is not implemented yet.")

            case TokenModelEnum.ACCESS_REFRESH:
                raise PyBearerNotImplementedError("Refresh token model is not implemented yet.")

            case TokenModelEnum.APIKEY:
                raise PyBearerNotImplementedError("API key token model is not implemented yet.")



    def login(self, identifier: str, password: str) -> Credential:
        """
        Authenticate a user and generate authentication credentials.

        The login process performs the following steps:

        1. Load the user using the configured `load_user` hook.
        2. Verify the password using the configured `verify_password` hook.
        3. Delegate credential generation to the selected authentication strategy.

        Parameters
        ----------
        identifier : str
            Unique user identifier (e.g., username, email, phone).

        password : str
            The user's password.

        Returns
        -------
        Any
            Authentication credentials returned by the selected strategy
            (e.g., token, session ID).

        Raises
        ------
        LoadUserNotConfiguredError
            If the `load_user` hook is not configured.

        VerifyPasswordNotConfiguredError
            If the `verify_password` hook is not configured.

        UserNotFoundError
            If no user is found for the provided identifier.

        InvalidCredentialsError
            If password verification fails.

        Last Updated: 2026-03-14
        """

        if self.load_user is None:
            raise LoadUserNotConfiguredError("Attribute 'load_user' is not configured.")

        if self.verify_password is None:
            raise VerifyPasswordNotConfiguredError("Attribute 'verify_password' is not configured.")

        user = self.load_user(identifier)

        if user is None:
            raise UserNotFoundError("No user found for the provided identifier.")

        if not self.verify_password(user, password):
            raise InvalidCredentialsError("Credential verification failed.")

        return self.strategy.issue(user)


    def verify(self, token: str):
        """
        Verify authentication credentials using the selected strategy.
        """
        return self.strategy.verify(token)


    def revoke(self, token: str):
        """
        Revoke authentication credentials using the selected strategy.
        """
        return self.strategy.revoke(token)
