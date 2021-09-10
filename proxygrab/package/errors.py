class ProxyGrabError(Exception):
    """General class for handling exceptions."""


class MethodNotFound(ProxyGrabError):
    """Exception raised for errors in the input method.

    Attributes:
        method -- input method which caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        method,
        message="Method to grab proxies not in ('api', 'scrappper', 'all')",
    ):
        self.method = method
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.method} -> {self.message}"


class ProxyTypeNotFound(ProxyGrabError):
    """Exception raised for errors in the input proxy type.

    Attributes:
        ptype -- input proxy type which caused the error
        message -- explanation of the error
    """

    def __init__(
        self,
        ptype,
        message="Proxy Type not in ('http', 'https', 'socks4', 'socks5')",
    ):
        self.ptype = ptype
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ptype} -> {self.message}"


class UnknownError(ProxyGrabError):
    """Exception raised when error is unknown."""

    def __init__(
        self,
        causes=(
            "Some causes of error may be:\n"
            "1. Maybe check you internet connection?\n"
            "2. No Proxies found!\n"
            "3. Maybe your IP is Temporarily Banned!"
        ),
        message="Unknown Error!",
    ):
        self.causes = causes
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n -> {self.causes}"
