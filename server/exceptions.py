"""
"""

class InvalidAPIKey(Exception):
    """
    An error occurred if the API key is invalid.
    """
    def __init__(self, message="Invalid API key"):
        """
        Constructor for InvalidAPIKey class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)

class NoCreditsRemaining(Exception):
    """
    An error occurred if the user has no credits remaining.
    """
    def __init__(self, message="No credits remaining"):
        """
        Constructor for NoCreditsRemaining class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)

class InvalidEmailAddress(Exception):
    """
    An error occurred if the email address is invalid.
    """
    def __init__(self, message="Invalid email address"):
        """
        Constructor for InvalidEmailAddress class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)
    
class IncorrectPassword(Exception):
    """
    An error occurred if the password is incorrect.
    """
    def __init__(self, message="Incorrect password"):
        """
        Constructor for IncorrectPassword class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)

class EmailAddressAlreadyInUse(Exception):
    """
    An error occurred if the email address is already in use.
    """
    def __init__(self, message="Email address already in use"):
        """
        Constructor for EmailAddressAlreadyInUse class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)

class UserNotFound(Exception):
    """
    An error occurred if the user is not found.
    """
    def __init__(self, message="Invalid user ID"):
        """
        Constructor for UserNotFound class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)

class InvalidVerificationCode(Exception):
    """
    An error occurred if the verification code is invalid.
    """
    def __init__(self, message="Invalid verification code"):
        """
        Constructor for InvalidVerificationCode class.

        Args
        ----
        message (str): Exception message.

        Author: ``@ChinaiArman``
        """
        self.message = message
        super().__init__(self.message)
