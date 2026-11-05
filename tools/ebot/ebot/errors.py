"""Safe errors. Messages must never include credentials or response bodies."""

from __future__ import annotations


class EbotError(Exception):
    """Base error with an operator-safe message."""


class SecretSetupError(EbotError):
    """The API key is missing or the local secret file is not acceptable."""


class ProviderHttpError(EbotError):
    """HTTP status from Massive. The body is not retained."""

    def __init__(self, code: int) -> None:
        self.code = int(code)
        super().__init__("HTTP_" + str(self.code))


class ProviderTransportError(EbotError):
    """Network failure whose message does not include the URL or key."""


class ProviderPayloadError(EbotError):
    """The response was not a usable JSON object. The body is not retained."""


class LocalCallCap(EbotError):
    """The in-process cap of five requests per run was reached."""

    def __init__(self) -> None:
        super().__init__("LOCAL_CALL_CAP")
