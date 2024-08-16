import requests  # For sending requests to the web
from bs4 import BeautifulSoup  # For parsing and manipulating HTML and XML documents
from typing import List  # For hinting,help with code clarity, readability
from requests import RequestException


class SitemapParser:
    """
    This class handles the parsing of the sitemap index and the extraction of article URLs.
    """

    def __init__(self, sitemap_index_url: str):  # Serves as a constructor for the class, also here we use the hinting
        """
        Initializes an instance of the SitemapParser class with the URL of the main sitemap index.

        :param sitemap_index_url: The URL of the sitemap index that contains links to monthly sitemaps.

        This URL is stored as an instance variable (self.sitemap_index_url) so that it can be used later in other
        methods.
        """
        self.sitemap_index_url = sitemap_index_url  # Store the sitemap index URL for later use

    def fetch_sitemap_index(self) -> List[str]:  # -> List[str]: To indicate that the function returns a list of strings
        """
        Fetches the sitemap index and retrieves the URLs of the monthly sitemaps.

        :return: A list of URLs pointing to the monthly sitemaps.
        """
        try:
            response = requests.get(self.sitemap_index_url)  # Send an HTTP GET request to the sitemap index URL
            if response.status_code == 200:
                # If the request is successful, parse the XML content
                soup = BeautifulSoup(response.content, 'lxml')  # Parse the XML response content, using lxml parser
                urls_loc_tags = soup.find_all('loc')  # Find all <loc> tags in the XML content
                sitemap_urls = []  # Initialize an empty list to store the sitemap URLs
                for loc in urls_loc_tags:  # Loop through the <loc> tags to extract the URLs and add them to the list
                    sitemap_urls.append(loc.text.strip())
                return sitemap_urls  # Return the list of sitemap URLs
            else:
                # If the request fails, print an error message and return an empty list
                print(f"Failed to retrieve sitemap index. Status code: {response.status_code}")
                return []
        except RequestException as e:
            print(f"Failed to retrieve sitemap. Error: {e}")
            return []

    @staticmethod
    def fetch_article_urls(monthly_sitemap_url: str) -> List[str]:
        """
        Fetches a monthly sitemap and extracts the URLs of articles.

        :param monthly_sitemap_url: The URL of the monthly sitemap to be parsed.
        :return: A list of article URLs extracted from the sitemap.
        """
        try:
            response = requests.get(monthly_sitemap_url)  # Send an HTTP GET request to the monthly sitemap URL
            if response.status_code == 200:
                # If the request is successful, parse the XML content
                soup = BeautifulSoup(response.content, 'lxml')  # Parse the XML response content
                monthly_url_loc_tags = soup.find_all('loc')  # Find all <loc> tags in the XML content
                article_urls = []  # Initialize an empty list to store the article URLs
                for loc in monthly_url_loc_tags:  # Loop through the <loc> tags to extract the URLs and add them to list
                    article_urls.append(loc.text.strip())
                return article_urls  # Return the list of article URLs
            else:
                # If the request fails, print an error message and return an empty list
                print(f"Failed to retrieve sitemap. Status code: {response.status_code}")
                return []
        except RequestException as e:
            print(f"Failed to retrieve sitemap. Error: {e}")
            return []

    @staticmethod
    def extract_year_month_from_url(url: str) -> (int, int):
        """
        Extracts the year and month from a sitemap URL.

        :param url: The URL of the sitemap which contains the year and month.
        :return: A tuple containing the year and month as integers.
        """
        # Split the URL based on the hyphens
        parts = url.split('-')
        year = int(parts[-2])
        month = int(parts[-1].split('.')[0])
        return year, month
