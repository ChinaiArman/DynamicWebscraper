"""
EndpointUsage.py
This module contains the data class to represent an endpoint usage in the database.

Disclaimer
----------
This file was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
from db_config import db


# ENDPOINT USAGE CLASS
class EndpointUsage(db.Model):
    """
    A data class to represent an endpoint usage in the database.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    __tablename__ = 'endpoint_usage'

    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(1000), nullable=False)
    method = db.Column(db.String(10), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def to_dict(self) -> dict:
        """
        Return the dictionary representation of the endpoint usage.

        Args
        ----
        None

        Returns
        -------
        dict: The dictionary representation of the endpoint usage.
        """
        return {
            'id': self.id,
            'endpoint': self.endpoint,
            'method': self.method,
            'count': self.count
        }
        
