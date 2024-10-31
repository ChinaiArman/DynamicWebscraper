"""
"""

# IMPORTS
from models.Scrape import Scrape
from models.User import User

from exceptions import InvalidAPIKey, InvalidEmailAddress, EmailAddressAlreadyInUse, UserNotFound


# DATABASE CLASS
class Database:
    """
    A class to interact with the MySQL database.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    def __init__(self, db):
        """
        Constructor for Database class.

        Args
        ----
        db (SQLAlchemy): SQLAlchemy object.

        Author: ``@ChinaiArman``
        """
        self.db = db

    def create_user(self, email, password, name, verification_code) -> User:
        """
        Create a new user in the database.

        Args
        ----
        email (str): User email address.
        password (str): User password.
        name (str): User name.
        verification_code (str): User verification code.

        Returns
        -------
        user (User): The user object.

        Raises
        ------
        EmailAddressAlreadyInUse: If the email address is already in use.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.

        Author: ``@ChinaiArman``
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse
        user = User(email=email, password=password, name=name, verification_code=verification_code, is_verified=False, requests_available=20)
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    def get_user_by_id(self, user_id: int) -> User:
        """
        Get a user by ID.

        Args
        ----
        user_id (int): User ID.

        Returns
        -------
        user (User): The user object.

        Raises
        ------
        UserNotFound: If the user is not found.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.

        Author: ``@ChinaiArman``
        """
        user = self.db.session.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound
        return user

    def get_user_by_api_key(self, api_key: str) -> User:
        """
        Get a user by API key.

        Args
        ----
        api_key (str): User API key.

        Returns
        -------
        user (User): The user object.

        Raises
        ------
        InvalidAPIKey: If the API key is invalid.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.

        Author: ``@ChinaiArman``
        """
        user = self.db.session.query(User).filter(User.api_key == api_key).first()
        if not user:
            raise InvalidAPIKey
        return user

    def get_user_by_email(self, email: str) -> User:
        """
        Get a user by email address.
        
        Args
        ----
        email (str): User email address.
        
        Returns
        -------
        user (User): The user object.

        Raises
        ------
        InvalidEmailAddress: If the email address is invalid.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        
        Author: ``@ChinaiArman``
        """
        user = self.db.session.query(User).filter(User.email == email).first()
        if not user:
            raise InvalidEmailAddress
        return user
    
    def verify_user(self, user: User, api_key: str) -> User:
        """
        Verify a user.

        Args
        ----
        user (User): The user object.
        api_key (str): The new user API key.

        Returns
        -------
        user (User): The user object.

        Author: ``@ChinaiArman``
        """
        user.is_verified = True
        user.verification_code = None
        user.api_key = api_key
        self.db.session.commit()
        return user
    
    def update_verification_code(self, user: User, verification_code: str) -> User:
        """
        Update the verification code for a user.

        Args
        ----
        user (User): The user object.
        verification_code (str): The new verification code.

        Returns
        -------
        user (User): The user object.

        Author: ``@ChinaiArman``
        """
        user.verification_code = verification_code
        self.db.session.commit()
        return user
    
    def update_password(self, user: User, password: str) -> User:
        """
        Update the password for a user.

        Args
        ----
        user (User): The user object.
        password (str): The new user password.

        Returns
        -------
        user (User): The user object.

        Author: ``@ChinaiArman``
        """
        user.password = password
        user.verification_code = None
        self.db.session.commit()
        return user
