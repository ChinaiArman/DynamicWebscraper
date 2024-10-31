"""
"""

class InvalidAPIKey(Exception):
    """
    """
    def __init__(self, message="Invalid API key"):
        """
        """
        self.message = message
        super().__init__(self.message)

class NoCreditsRemaining(Exception):
    """
    """
    def __init__(self, message="No credits remaining"):
        """
        """
        self.message = message
        super().__init__(self.message)

class InvalidEmailAddress(Exception):
    """
    """
    def __init__(self, message="Invalid email address"):
        """
        """
        self.message = message
        super().__init__(self.message)
    
class IncorrectPassword(Exception):
    """
    """
    def __init__(self, message="Incorrect password"):
        """
        """
        self.message = message
        super().__init__(self.message)

class EmailAddressAlreadyInUse(Exception):
    """
    """
    def __init__(self, message="Email address already in use"):
        """
        """
        self.message = message
        super().__init__(self.message)

class UserNotFound(Exception):
    """
    """
    def __init__(self, message="Invalid user ID"):
        """
        """
        self.message = message
        super().__init__(self.message)

class InvalidVerificationCode(Exception):
    """
    """
    def __init__(self, message="Invalid verification code"):
        """
        """
        self.message = message
        super().__init__(self.message)