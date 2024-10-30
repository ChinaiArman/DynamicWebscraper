"""
"""

# IMPORTS
import bcrypt

from exceptions import NoCreditsRemaining, IncorrectPassword


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
    
    def encrypt_password(self, password):
        """
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def verify_password(self, password, hashed_password):
        """
        """
        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            raise IncorrectPassword
        return True
        
    def generate_api_key(self):
        """
        """
        return bcrypt.gensalt().decode('utf-8')
    
    def generate_verification_code(self):
        """
        """
        return bcrypt.gensalt().decode('utf-8')[:6]
    
