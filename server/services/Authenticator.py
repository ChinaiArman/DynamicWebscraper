"""
"""

# IMPORTS
import bcrypt
import secrets

from exceptions import NoCreditsRemaining, IncorrectPassword, InvalidOneTimeCode


# AUTHENTICATOR CLASS
class Authenticator:
    """
    A class used to authenticate users, sessions, requests, and API keys.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    def __init__(self):
        """
        Initialize the Authenticator class.

        Args
        ----
        None
        """
        pass

    def is_scrape_available(self, user) -> bool:
        """
        Check if the user has any credits remaining.

        Args
        ----
        user (User): The user object.

        Returns
        -------
        bool: True if the user has credits remaining, otherwise False.

        Raises
        ------
        NoCreditsRemaining: If the user has no credits remaining.
        """
        if user.requests_available <= 0:
            raise NoCreditsRemaining()
        return True
    
    def encrypt_password(self, password: str) -> str:
        """
        Encrypt a password.

        Args
        ----
        password (str): The password to encrypt.

        Returns
        -------
        str: The encrypted password.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Verify a password.

        Args
        ----
        password (str): The password to verify.
        hashed_password (str): The hashed password to compare.

        Returns
        -------
        bool: True if the password is correct, otherwise False.

        Raises
        ------
        IncorrectPassword: If the password is incorrect.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            raise IncorrectPassword()
        return True
        
    def generate_api_key(self) -> str:
        """
        Generate a new API key.

        Args
        ----
        None

        Returns
        -------
        str: The new API key.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        return secrets.token_hex(25)
    
    def generate_one_time_code(self) -> str:
        """
        Generate a new 6 digit code.

        Args
        ----
        None

        Returns
        -------
        str: The new 6 digit code.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        return secrets.token_hex(3)
    
    def verify_code(self, code: str, user_code: str) -> bool:
        """
        Verify a one-time code.

        Args
        ----
        code (str): The one-time code to verify.
        user_code (str): The user's one-time code.

        Returns
        -------
        bool: True if the one-time code is correct, otherwise False.

        Raises
        ------
        InvalidOneTimeCode: If the one-time code is incorrect.
        """
        if code != user_code or not user_code:
            raise InvalidOneTimeCode()
        return True
