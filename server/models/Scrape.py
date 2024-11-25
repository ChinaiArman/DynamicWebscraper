"""
Scrape.py
This module contains a data class to represent a scrape in the database.

Disclaimer
----------
This file was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
from db_config import db


# SCRAPE DATA CLASS
class Scrape(db.Model):
    """
    A data class to represent a scrape in the database.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    __tablename__ = 'scrapes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    url = db.Column(db.String(1000), nullable=False)
    prompt = db.Column(db.String(1000), nullable=False)
    response = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='scrapes')

    def to_dict(self) -> dict:
        """
        Return the dictionary representation of the scrape.

        Args
        ----
        None

        Returns
        -------
        dict: The dictionary representation of the scrape.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.url,
            'prompt': self.prompt,
            'response': self.response,
            'created_at': self.created_at
        }
