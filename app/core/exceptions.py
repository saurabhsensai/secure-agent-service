class UserNotFoundError(Exception):
    """Raised when a requested user does not exist."""
    pass

class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists."""
    pass

class InterruptNotFoundError(Exception):
    """Raised when a requested interrupt does not exist."""
    pass

class ThreadAccessDeniedError(Exception):
    """Raised when a user tries to access a thread they do not own."""
    pass

class ThreadNotFoundError(Exception):
    pass

class InterruptNotFoundError(Exception):
    """Raised when a requested interrupt does not exist."""
    pass


class InterruptAlreadyResolvedError(Exception):
    """Raised when attempting to resolve an already resolved interrupt."""
    pass


class InvalidInterruptStatusError(Exception):
    """Raised when an interrupt has an invalid status."""
    pass