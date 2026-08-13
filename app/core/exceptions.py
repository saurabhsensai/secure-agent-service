class UserNotFoundError(Exception):
    """Raised when a requested user does not exist."""
    pass

class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists."""
    pass


class ThreadNotFoundError(Exception):
    """Raised when a requested thread does not exist."""
    pass


class InterruptNotFoundError(Exception):
    """Raised when a requested interrupt does not exist."""
    pass