"""
"""

# IMPORTS
from models.Scrape import Scrape
from models.User import User

from exceptions import InvalidAPIKey


# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    def get_user_by_api_key(self, api_key):
        """
        """
        user = self.db.session.query(User).filter(User.api_key == api_key).first()
        if not user:
            raise InvalidAPIKey
        return user
