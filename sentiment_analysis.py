# Imports the Google Cloud client library
from google.cloud import language_v1
import os

def analyze_text (text):

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= 'sentiment_analysis.json'
    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    document = language_v1.Document(content=text, type_=language_v1.Document.Type.HTML)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    score = round(sentiment.score, 2)
    magnitude = round(sentiment.magnitude)
    if score >= 0.6 and magnitude >= 0.8:
        label = 'Positive'
    elif score <= -0.6 and magnitude >= 0.8:
        label = 'Negative'
    elif magnitude < 0.8:
        label = 'Neutral'
    else:
        label = 'Mixed'

    short_text = text if len(text) < 500 else text[:500] + '...'

    return (label, score, magnitude, short_text)