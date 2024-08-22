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
            collection.insert_many(articles)  # Insert the articles into the MongoDB collection
            print(f'Inserted data from {filename} Successfully')
        else:
            print(f'File {filename} does not contain a list of documents.')
