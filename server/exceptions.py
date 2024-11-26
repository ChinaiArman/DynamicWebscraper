"""
exceptions.py
This module contains custom exceptions for the DynamicWebscraper application.
"""

# IMPORTS
import os
import json


# CONSTANTS
with open(os.getenv('USER_STRINGS_FILEPATH'), 'r') as file:
    USER_STRINGS = json.load(file)


# EXCEPTIONS
class InvalidAPIKey(Exception):
    """
    An error occurred if the API key is invalid.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['InvalidAPIKey']):
        """
        Constructor for InvalidAPIKey class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class NoCreditsRemaining(Exception):
    """
    An error occurred if the user has no credits remaining.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['NoCreditsRemaining']):
        """
        Constructor for NoCreditsRemaining class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class InvalidEmailAddress(Exception):
    """
    An error occurred if the email address is invalid.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['InvalidEmailAddress']):
        """
        Constructor for InvalidEmailAddress class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)
    
class IncorrectPassword(Exception):
    """
    An error occurred if the password is incorrect.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['IncorrectPassword']):
        """
        Constructor for IncorrectPassword class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class EmailAddressAlreadyInUse(Exception):
    """
    An error occurred if the email address is already in use.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['EmailAddressAlreadyInUse']):
        """
        Constructor for EmailAddressAlreadyInUse class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class UserNotFound(Exception):
    """
    An error occurred if the user is not found.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['UserNotFound']):
        """
        Constructor for UserNotFound class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class InvalidOneTimeCode(Exception):
    """
    An error occurred if the one-time code is invalid.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['InvalidOneTimeCode']):
        """
        Constructor for InvalidOneTimeCode class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class ImpermissibleUserRequest(Exception):
    """
    An error occurred if the request is not allowed.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['ImpermissibleUserRequest']):
        """
        Constructor for InpermissibleRequest class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class FetchRequestFailed(Exception):
    """
    An error occurred if the fetch request failed.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['FetchRequestFailed']):
        """
        Constructor for FetchRequestFailed class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)

class LLMRequestFailed(Exception):
    """
    An error occurred if the LLM request failed.
    """
    def __init__(self, message=USER_STRINGS['exceptions']['LLMRequestFailed']):
        """
        Constructor for LLMRequestFailed class.

        Args
        ----
        message (str): Exception message.
        """
        self.message = message
        super().__init__(self.message)