"""
"""

# IMPORTS
from db_config import db


# USER DATA CLASS
class User(db.Model):
    """
    A data class to represent a user in the database.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    requests_available = db.Column(db.Integer, default=20)
    verification_code = db.Column(db.String(6), nullable=True)
    reset_code = db.Column(db.String(6), nullable=True)
    api_key = db.Column(db.String(50), nullable=True)
    last_scrape = db.Column(db.DateTime, nullable=True)

    scrapes = db.relationship('Scrape', back_populates='user')

    def __repr__(self) -> str:
        """
        Return the string representation of the user.

        Args
        ----
        None

        Returns
        -------
        str: The string representation of the user.

        Author: ``@ChinaiArman``
        """
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'is_verified': self.is_verified,
            'requests_available': self.requests_available,
            'verification_code': self.verification_code,
            'reset_code': self.reset_code,
            'api_key': self.api_key,
            'last_scrape': self.last_scrape
        }
