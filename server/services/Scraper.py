"""
"""

# IMPORTS
import requests
from bs4 import BeautifulSoup
import time
import random

from exceptions import FetchRequestFailed

# SCRAPER CLASS
class Scraper:
    """
    A class to scrape a website and return the text content.

    Disclaimer
    ----------
    This class was created with the assistance of AI tools (GitHub Copilot and ChatGPT). All code created is original and has been reviewed and understood by a human developer.
    """
    def __init__(self, headers=None, timeout=10):
        """
        Initialize the Scraper class.

        Args
        ----
        headers (dict): The headers to use for the session
        timeout (int): The timeout for the session

        Disclaimer
        ----------
        This function was created with the assistance of AI tools (ChatGPT). All code created is original and has been reviewed and understood by a human developer
        """
        self.session = requests.Session()
        self.timeout = timeout

        self.session.headers.update(headers or {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        })

    def scrape(self, url: str) -> str:
        """
        Scrape a website of a given URL by removing all HTML tags and returning the text content.

        Args
        ----
        url (str): The URL to scrape.

        Returns
        -------
        str: The text content of the URL.

        Raises
        ------
        FetchRequestFailed: If the request to the URL fails.

        Disclaimer
        ----------
        This function was created with the assistance of AI tools (GitHub Copilot and ChatGPT). All code created is original and has been reviewed and understood by a human developer.
        """
        try: 
            time.sleep(random.randint(1, 3))
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            for data in soup(['style', 'script']):
                data.decompose()
            return ' '.join(soup.stripped_strings)
        except Exception as e:
            raise FetchRequestFailed(f"Failed to fetch URL: {url} - {str(e)}") 
            