"""
"""

# IMPORTS
from models.Scrape import Scrape
from models.User import User

from exceptions import InvalidAPIKey, InvalidEmailAddress, EmailAddressAlreadyInUse, UserNotFound


# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    def create_user(self, email, password, name, verification_code):
        """
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse
        user = User(email=email, password=password, name=name, verification_code=verification_code, is_verified=False, requests_available=20)
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    def get_user_by_id(self, user_id):
        """
        """
        user = self.db.session.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound
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
    
    def verify_user(self, user, api_key):
        """
        """
        user.is_verified = True
        user.verification_code = None
        user.api_key = api_key
        self.db.session.commit()
        return user
    
    def update_verification_code(self, user, verification_code):
        """
        """
        user.verification_code = verification_code
        self.db.session.commit()
        return user
    
    def update_password(self, user, password):
        """
        """
        user.password = password
        user.verification_code = None
        self.db.session.commit()
        return user
