from pymongo import MongoClient
from camel_tools.sentiment import SentimentAnalyzer # For analyzing sentiment of Arabic text

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Almayadeen']
collection = db['articles']

# Load the pre-trained sentiment analyzer
analyzer = SentimentAnalyzer.pretrained()

# Function to analyze sentiment of Arabic text
def analyze_arabic_sentiment(full_text):
    """
    This function takes an Arabic text as input and returns the sentiment of the text.
    """
    # Analyze the sentiment of the text
    sentiment = analyzer.predict(full_text)
    return sentiment


# Fetch all articles and analyze sentiment
articles = collection.find()
for article in articles:
    content = article.get('full_text', '') # Get the full text of the article
    local_sentiment = analyze_arabic_sentiment(content) # Analyze the sentiment of the article

    # Update the article with the sentiment
    collection.update_one({'_id': article['_id']}, {'$set': {'sentiment': local_sentiment}})
    print(f'Updated article {article["_id"]} with sentiment: {local_sentiment}')