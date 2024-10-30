"""
"""

# IMPORTS
from exceptions import NoCreditsRemaining


# AUTHENTICATOR CLASS
class Authenticator:
    """
    """
    def __init__(self):
        """
        """
        pass

    def is_scrape_available(self, user):
        """
        """
        if user.requests_available <= 0:
            raise NoCreditsRemaining
        return True
