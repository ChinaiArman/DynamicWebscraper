"""
Database.py
This module contains the Database class, which is used to interact with the MySQL database.

Disclaimer:
-----------
This file was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
from datetime import datetime

from models.Scrape import Scrape
from models.User import User
from models.EndpointUsage import EndpointUsage

from exceptions import InvalidAPIKey, InvalidEmailAddress, EmailAddressAlreadyInUse, UserNotFound, ImpermissibleUserRequest


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
        """
        self.db = db

    def create_user(self, email, password, verification_code) -> User:
        """
        Create a new user in the database.

        Args
        ----
        email (str): User email address.
        password (str): User password.
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
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse()
        user = User(email=email, password=password, verification_code=verification_code, reset_code=None, is_verified=False, requests_available=20)
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
        """
        user = self.db.session.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound()
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
        """
        user = self.db.session.query(User).filter(User.api_key == api_key).first()
        if not user:
            raise InvalidAPIKey()
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
        """
        user = self.db.session.query(User).filter(User.email == email).first()
        if not user:
            raise InvalidEmailAddress()
        return user
    
    def verify_user(self, user: User, api_key: str) -> None:
        """
        Verify a user.

        Args
        ----
        user (User): The user object.
        api_key (str): The new user API key.

        Returns
        -------
        None
        """
        user.is_verified = True
        user.verification_code = None
        user.api_key = api_key
        self.db.session.commit()
        return
    
    def update_reset_code(self, user: User, reset_code: str) -> None:
        """
        Update the reset code for a user.

        Args
        ----
        user (User): The user object.
        reset_code (str): The new reset code.

        Returns
        -------
        None
        """
        user.reset_code = reset_code
        self.db.session.commit()
        return
    
    def update_password(self, user: User, password: str) -> None:
        """
        Update the password for a user.

        Args
        ----
        user (User): The user object.
        password (str): The new user password.

        Returns
        -------
        None
        """
        user.password = password
        user.reset_code = None
        self.db.session.commit()
        return

    def get_scrapes_by_user_id(self, user_id: int) -> list:
        """
        Get scrapes by user ID.

        Args
        ----
        user_id (int): User ID.

        Returns
        -------
        scrapes (list): The list of scrapes.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        scrapes = self.db.session.query(Scrape).filter(Scrape.user_id == user_id).all()
        return scrapes
    
    def reset_api_key(self, user: User, api_key: str) -> None:
        """
        Reset a user's API key.

        Args
        ----
        user (User): The user object.
        api_key (str): The new user API key.

        Returns
        -------
        None
        """
        if not user.is_verified:
            raise ImpermissibleUserRequest()
        user.api_key = api_key
        self.db.session.commit()
        return
    
    def decrement_requests_available(self, user: User) -> None:
        """
        Decrement the number of requests available for a user.

        Args
        ----
        user (User): The user object.

        Returns
        -------
        None
        """
        user.last_request = datetime.now()
        user.requests_available -= 1
        self.db.session.commit()
        return
    
    def reset_requests(self, user: User) -> None:
        """
        Reset the number of requests available for a user.

        Args
        ----
        user (User): The user object.

        Returns
        -------
        None
        """
        user.requests_available = 20
        self.db.session.commit()
        return

    def create_scrape(self, user_id: int, url: str, prompt: str, response: str) -> Scrape:
        """
        Create a new scrape in the database.

        Args
        ----
        user_id (int): User ID.
        url (str): Scrape URL.
        prompt (str): Scrape prompt.
        response (str): Scrape response.

        Returns
        -------
        scrape (Scrape): The scrape object.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        scrape = Scrape(user_id=user_id, url=url, prompt=prompt, response=response, created_at=datetime.now())
        self.db.session.add(scrape)
        self.db.session.commit()
        return scrape

    def get_all_users(self) -> list:
        """
        Get all users.

        Args
        ----
        None

        Returns
        -------
        users (list): The list of users.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        users = self.db.session.query(User).all()
        return users

    def delete_user(self, user_id) -> None:
        """
        Delete a user.

        Args
        ----
        user (User): The user object.

        Returns
        -------
        None

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        user = self.get_user_by_id(user_id)
        self.db.session.delete(user)
        scrapes = self.get_scrapes_by_user_id(user_id)
        for scrape in scrapes:
            self.db.session.delete(scrape)
        self.db.session.commit()
        return
    
    def increment_requests(self, endpoint: str, method: str) -> None:
        """
        Increment the count for an endpoint.

        Args
        ----
        endpoint (str): The endpoint.
        method (str): The method.

        Returns
        -------
        None
        """
        usage = self.db.session.query(EndpointUsage).filter(EndpointUsage.endpoint == endpoint, EndpointUsage.method == method).first()
        if not usage:
            usage = EndpointUsage(endpoint=endpoint, method=method, count=1)
            self.db.session.add(usage)
        else:
            usage.count += 1
        self.db.session.commit()
        return
    
    def get_endpoint_usage(self) -> list:
        """
        Get the usage for all endpoints.

        Args
        ----
        None

        Returns
        -------
        usage (list): The list of endpoint usage.
        """
        usage = self.db.session.query(EndpointUsage).all()
        return [u.to_dict() for u in usage]
    
    def increment_total_requests(self, user) -> None:
        """
        Increment the total requests for a user.

        Args
        ----
        user (User): The user object.

        Returns
        -------
        None
        """
        user.num_requests += 1
        self.db.session.commit()
        return
    
    def get_scrape_by_id(self, scrape_id: int) -> Scrape:
        """
        Get a scrape by ID.
        
        Args
        ----
        scrape_id (int): Scrape ID.

        Returns
        -------
        scrape (Scrape): The scrape

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        scrape = self.db.session.query(Scrape).filter(Scrape.id == scrape_id).first()
        return scrape
    
    def delete_scrape(self, scrape_id: int) -> None:
        """
        Delete a scrape.

        Args
        ----
        scrape_id (int): Scrape ID.

        Returns
        -------
        None
        """
        scrape = self.get_scrape_by_id(scrape_id)
        self.db.session.delete(scrape)
        self.db.session.commit()
        return
    
    def update_email(self, user: User, email: str) -> None:
        """
        Update a user's email address.

        Args
        ----
        user (User): The user object.
        email (str): The new email address
        
        Returns
        -------
        None
        """
        user.email = email
        self.db.session.commit()
        return
