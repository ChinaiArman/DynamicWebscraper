"""
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
    data = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='scrapes')

    def __repr__(self) -> str:
        """
        Return the string representation of the scrape.

        Args
        ----
        None

        Returns
        -------
        str: The string representation of the scrape.

        Author: ``@ChinaiArman``
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.url,
            'prompt': self.prompt,
            'data': self.data,
            'created_at': self.created_at
        }
