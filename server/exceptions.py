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