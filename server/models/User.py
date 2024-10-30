"""
"""

# IMPORTS
from db_config import db


# USER DATA CLASS
class User(db.Model):
    """
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    requests_available = db.Column(db.Integer, default=20)
    reset_code = db.Column(db.String(6), nullable=True)
    api_key = db.Column(db.String(50), nullable=True)
    last_scrape = db.Column(db.DateTime, nullable=True)

    scrapes = db.relationship('Scrape', back_populates='user')

    def __repr__(self):
        """
        """
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'is_verified': self.is_verified,
            'requests_available': self.requests_available,
            'reset_code': self.reset_code,
            'api_key': self.api_key,
            'last_scrape': self.last_scrape
        }
