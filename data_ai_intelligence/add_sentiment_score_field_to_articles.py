from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

# Load the pre-trained AraBERT model for sentiment analysis
model_name = "aubmindlab/bert-base-arabertv02-twitter"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# Function to analyze sentiment and get scores
def analyze_sentiment_arabert(full_text):
    # Tokenize the input text
    inputs = tokenizer(full_text, return_tensors='pt', truncation=True, padding=True)

    # Get the model output
    with torch.no_grad():
        outputs = model(**inputs)

    # Get raw logits and apply softmax to get probabilities
    logits = outputs.logits.detach().numpy()[0]
    probabilities = softmax(logits)

    # Assuming the model outputs two classes: [negative, positive]
    return {
        'sentiment_score_negative': probabilities[0],
        'sentiment_score_positive': probabilities[1]
    }


# Example usage
text = "هذا النص يعبر عن سعادة كبيرة"
scores = analyze_sentiment_arabert(text)
print(scores)
