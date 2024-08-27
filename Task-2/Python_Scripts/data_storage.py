import os  # To allow us to interact with the operating system
import pymongo  # To allow us to interact with MongoDB
import json  # To allow us to work with JSON data

# Connects to MongoDB and inserts data into the 'articles' collection of the 'almayadeen' database.

# Connect to the MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Almayadeen"]
collection = db["articles"]

# Directory where the JSON files are saved
directory = r"C:\Users\Voldemort\PycharmProjects\AlmayadeenScraping\data_articles"

# Loop through each file in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        # Load and insert JSON data
        articles = json.load(file)

        # Ensure data is a list of dictionaries before inserting
        if isinstance(articles, list):
            # Iterate through each article to fix the keywords issue
            # Loop through each article in the list

            for article in articles:
                # Check if the 'keywords' field is present and is a string
                if 'keywords' in article and isinstance(article['keywords'], str):
                    # Create an empty list to store the cleaned keywords
                    keywords_list = []

                    # Split the comma-separated string into individual keywords
                    # and remove any extra spaces around each keyword
                    for keyword in article['keywords'].split(','):
                        cleaned_keyword = keyword.strip()  # Remove extra spaces
                        keywords_list.append(cleaned_keyword)  # Add the cleaned keyword to the list

                    # Update the 'keywords' field with the list of cleaned keywords
                    article['keywords'] = keywords_list


            collection.insert_many(articles)  # Insert the articles into the MongoDB collection
            print(f'Inserted data from {filename} Successfully')
        else:
            print(f'File {filename} does not contain a list of documents.')
