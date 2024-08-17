from dataclasses import asdict  # For defining a data model using dataclasses
from typing import List  # For hinting,help with code clarity, readability
import os  # For interacting with the operating system
import json  # For working with JSON data

import Article


class FileUtility:
    """
    This class handles saving the extracted data to JSON files.
    """

    @staticmethod
    def save_articles_to_json(articles: List['Article'], year: int, month: int):
        """
        Saves a list of Article objects to a JSON file with the format articles_YYYY_MM.json.

        :param articles: A list of Article objects to be saved.
        :param year: The year of the articles.
        :param month: The month of the articles.
        """

        # Create an empty list to store dictionaries
        articles_dict = []

        # Loop through each article in the articles list
        for article in articles:
            # Convert the article object to a dictionary
            article_dict = asdict(article)
            # Add the dictionary to the list
            articles_dict.append(article_dict)

        # Generate the file path based on the year and month
        file_path = FileUtility.get_file_path(year, month)

        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the list of dictionaries to a JSON file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(articles_dict, file, ensure_ascii=False, indent=4)

    @staticmethod
    def get_file_path(year: int, month: int) -> str:
        """
        Generates the file path for saving articles based on the year and month.

        :param year: The year of the articles.
        :param month: The month of the articles.
        :return: The file path as a string.
        """
        # Format the month to two digits (e.g., 08 for August)
        month_str = f"{month:02d}"
        # Generate file name based on year and month
        file_name = f"articles_{year}_{month_str}.json"
        # Define the directory where files will be saved (adjust as needed)
        directory = r"C:\Users\Voldemort\PycharmProjects\AlmayadeenScraping\data_articles"
        # Return the full file path
        return os.path.join(directory, file_name)
