"""
"""

# IMPORTS
from models.Scrape import Scrape
from models.User import User

from exceptions import InvalidAPIKey, InvalidEmailAddress, EmailAddressAlreadyInUse


# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    def create_user(self, email, password, name, api_key, reset_code):
        """
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse
        user = User(email=email, password=password, name=name, api_key=api_key, reset_code=reset_code, is_verified=False, requests_available=20)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def get_user_by_api_key(self, api_key):
        """
        """
        user = self.db.session.query(User).filter(User.api_key == api_key).first()
        if not user:
            raise InvalidAPIKey
        return user

    def get_user_by_email(self, email):
        user = self.db.session.query(User).filter(User.email == email).first()
        if not user:
            raise InvalidEmailAddress
        return user
    
