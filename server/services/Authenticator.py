"""
"""

# IMPORTS


# AUTHENTICATOR CLASS
class Authenticator:
    """
    """
    def __init__(self):
        """
        """
        pass

    def is_valid_api_key(self, user):
        """
        """
        return user.requests_available > 0
