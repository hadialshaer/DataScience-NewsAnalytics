from pymongo import MongoClient
from camel_tools.ner import NERecognizer
from camel_tools.tokenizers.word import simple_word_tokenize

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB
db = client['Almayadeen']  # Select the 'Almayadeen' database
collection = db['articles']  # Select the 'articles' collection

# Load the pre-trained Named Entity Recognizer (NER)
ner = NERecognizer.pretrained()

# Function to extract named entities from Arabic text
def extract_entities(full_text):
    """
    Extract named entities from a given Arabic text.
    Returns a dictionary with recognized entities categorized by type.
    """
    tokens = simple_word_tokenize(full_text)  # Tokenize the text
    entity_predictions = ner.predict([tokens])  # Predict expects a list of tokenized sequences
    entities = entity_predictions[0]  # Flatten the predicted entities list

    # Structure the entities by type dynamically
    entity_dict = {}
    for token, tag in zip(tokens, entities):
        if tag.startswith('B-') or tag.startswith('I-'):  # Only named entities
            entity_type = tag[2:]  # Extract entity type (e.g., ORG, PERSON, LOCATION)
            entity_dict.setdefault(entity_type, []).append(token)

    return entity_dict

# Fetch all articles with cursor handling and batch size
articles = collection.find(no_cursor_timeout=True).batch_size(100)  # Fetch articles with batch size

try:
    for article in articles:
        try:
            content = article.get('full_text', '').strip()  # Get the full text of the article
            if not content:  # Skip empty articles
                continue

            local_entities = extract_entities(content)  # Extract entities from the article's text

            if local_entities:  # Only update if entities were found
                collection.update_one(
                    {'_id': article['_id']},
                    {'$set': {'entities': local_entities}}  # Set the 'entities' field
                )
                print(f'Updated article {article["_id"]} with entities: {local_entities}')
        except Exception as e:
            print(f"Error processing article {article['_id']}: {str(e)}")  # Log the error
finally:
    articles.close()  # Ensure cursor is closed even if an error occurs