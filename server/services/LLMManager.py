"""
LLMManager.py
This module contains the LLMManager class for interacting with the Language Learning Model (LLM) server.

Disclaimer
----------
This file was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
"""

# IMPORTS
import requests
import os
from dotenv import load_dotenv

from exceptions import LLMRequestFailed


# ENVIRONMENT VARIABLES
load_dotenv()
LLM_PROXY = os.getenv('LLM_PROXY')


# LLM Manager CLASS
class LLMManager:
    """
    A class to interact with the Language Learning Model (LLM) API.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
    """
    def __init__(self):
        """
        Initialize the LLMManager class.

        Args
        ----
        None
        """
        self.proxy = LLM_PROXY

    def query(self, question: str, context: str) -> dict:
        """
        Query the LLM API with a question and context.

        Args
        ----
        question (str): The question to ask the model.
        context (str): The context to provide to the model.

        Returns
        -------
        dict: The response from the LLM API.

        Raises
        ------
        LLMRequestFailed: If the request to the LLM API fails.

        Disclaimer
        ----------
        This method was created with the assistance of AI tools (GitHub Copilot). All code created is original and has been reviewed and understood by a human developer.
        """
        data = {
            "question": question,
            "context": context
        }
        response = requests.post(f'{self.proxy}/query', json=data, verify=False)
        print(response)
        if response.status_code == 200:
            return response.json().get('answers')
        else:
            raise LLMRequestFailed()

    