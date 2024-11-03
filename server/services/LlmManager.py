"""
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
    """
    def __init__(self):
        """
        """
        self.proxy = LLM_PROXY

    def query(self, question: str, context: str) -> dict:
        """
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

    