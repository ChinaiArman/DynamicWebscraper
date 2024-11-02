"""
"""

# IMPORTS
import requests
from bs4 import BeautifulSoup

# SCRAPER CLASS
class Scraper:
    """
    A class to scrape a website and return the text content.
    """
    def __init__(self):
        """
        """
        pass

    def scrape(self, url: str) -> str:
        """
        Scrape a website of a given URL by removing all HTML tags and returning the text content.

        Args
        ----
        url (str): The URL to scrape.

        Returns
        -------
        str: The text content of the URL.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for data in soup(['style', 'script']):
            data.decompose()
        text = ' '.join(soup.stripped_strings)
        return text
    