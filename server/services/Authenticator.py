"""
"""

# IMPORTS
import bcrypt
import secrets

from exceptions import NoCreditsRemaining, IncorrectPassword, InvalidVerificationCode


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
        return secrets.token_hex(25)
    
    def generate_verification_code(self):
        """
        """
        return secrets.token_hex(3)
    
    def verify_verification_code(self, code, user_code):
        """
        """
        if code != user_code or not user_code:
            raise InvalidVerificationCode
        return True
    
