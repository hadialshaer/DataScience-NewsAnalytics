import requests  # For sending requests to the web
from bs4 import BeautifulSoup  # For parsing and manipulating HTML and XML documents
import json  # For working with JSON data
from requests import RequestException

import Article  # Import the Article class from the Article module


class ArticleScraper:
    """
    This class handles the scraping of individual articles from their URLs.
    """

    @staticmethod
    def scrape_article(article_url: str) -> 'Article':
        """
        Scrapes an article from the given URL and returns an Article object with extracted metadata and content.

        :param article_url: The URL of the article to be scraped.
        :return: An Article object containing the scraped data.
        """

        # Send an HTTP GET request to retrieve the article HTML
        try:
            response = requests.get(article_url)
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.content, 'lxml')

                # Extract metadata from the <script> tag with type="text/tawsiyat"
                script_tag = soup.find('script', {'id': 'tawsiyat-metadata', 'type': 'text/tawsiyat'})
                # Extract the content of the script tag as a string (or an empty string if the tag is not found)
                metadata = script_tag.string if script_tag is not None else '{}'
                # Convert metadata from JSON string to dictionary to better access the data
                metadata_dict = json.loads(metadata)

                # Extract post ID from <meta> tag
                postid_meta = soup.find('meta', {'name': 'postid'})
                # Extract the content attribute of the meta tag (or None if the tag is not found)
                postid = postid_meta['content'] if postid_meta else None

                # Extract title and other metadata from metadata_dict if available
                title = metadata_dict.get('title')
                keywords = metadata_dict.get('keywords', [])
                thumbnail = metadata_dict.get('thumbnail')
                video_duration = metadata_dict.get('video_duration')
                word_count = metadata_dict.get('word_count')
                lang = metadata_dict.get('lang')
                published_time = metadata_dict.get('published_time')
                last_updated = metadata_dict.get('last_updated')
                description = metadata_dict.get('description')
                author = metadata_dict.get('author')
                classes = metadata_dict.get('classes', [])

                # Initialize an empty list to store paragraphs of full text
                paragraphs = []
                # Define target classes for full text
                target_classes = ["lg_para summary", "p-content", "lg_para"]

                # Loop through the target classes to find paragraphs with the specified classes
                for class_name in target_classes:
                    if class_name == "p-content":
                        content_div = soup.find('div', class_=class_name)
                        found_paragraphs = content_div.find_all('p', recursive=False) if content_div else []
                    else:
                        found_paragraphs = soup.find_all('p', class_=class_name)

                    for p in found_paragraphs:
                        # Extract the text directly, stripping whitespace
                        text = p.get_text(strip=True)
                        if text:
                            paragraphs.append(text)

                # Join the paragraphs into a single string with newlines
                full_text = '\n'.join(paragraphs)

                # Create and return an Article object
                article = Article.Article(
                    url=article_url,
                    postId=postid,
                    title=title,
                    keywords=keywords,
                    thumbnail=thumbnail,
                    video_duration=video_duration,
                    word_count=word_count,
                    lang=lang,
                    published_time=published_time,
                    last_updated=last_updated,
                    description=description,
                    author=author,
                    classes=classes,
                    full_text=full_text
                )
                return article
            else:
                # If the request fails, print an error message and return None
                print(f"Failed to retrieve article. Status code: {response.status_code}")
                return None
        except RequestException as e:
            print(f"Failed to retrieve sitemap. Error: {e}")
            return []
