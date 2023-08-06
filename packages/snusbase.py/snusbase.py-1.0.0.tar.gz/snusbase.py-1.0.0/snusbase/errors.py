class SnusException(Exception):
    """Base class for exceptions."""

    pass


class NoResponse(SnusException):
    """The API didn't return anything or got no response."""

    pass
