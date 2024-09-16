from transformers import pipeline
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Almayadeen']
collection = db['articles']

# Load the sentiment analysis pipeline using the CAMeLBERT-DA SA model
sa_pipeline = pipeline('text-classification', model='CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment')

# Function to analyze sentiment using CAMeLBERT-DA and return the sentiment and score
def analyze_sentiment_camelbert(full_text):
    try:
        # Use the pipeline to get the sentiment analysis with truncation
        results = sa_pipeline(full_text, truncation=True, padding=True, max_length=512)

        # Extract the label and score
        sentiment_label = results[0]['label']
        sentiment_score = results[0]['score']

        sentiment_data = {
            'sentiment': sentiment_label,
            'sentiment_score': float(sentiment_score)
        }
        return sentiment_data
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return None

# Fetch all articles and update sentiment scores
try:
    articles = collection.find()
    for article in articles:
        content = article.get('full_text', '')  # Get the full text of the article
        if content.strip():  # Check if full_text is not empty
            sentiment_data = analyze_sentiment_camelbert(content)  # Analyze the sentiment of the article
            if sentiment_data:
                # Directly update the document with new sentiment data, overwriting the old value
                collection.update_one(
                    {'_id': article['_id']},
                    {'$set': sentiment_data}
                )
                print(f'Updated article {article["_id"]} with sentiment: {sentiment_data}')
            else:
                print(f"No sentiment data returned for article {article['_id']}")
        else:
            print(f"Empty content for article {article['_id']}")
except Exception as e:
    print(f"Error processing articles: {e}")
