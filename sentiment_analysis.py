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

    # print("Text: {}".format(text))
    # print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    return sentiment.score