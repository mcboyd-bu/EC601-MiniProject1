# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

def GetSentiment(t):   # Return sentiment of submitted text
    # Convert submitted text to unicode (required by API)
    text = unicode(t, "utf-8")
    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    result = 'Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude)
    return result

# The text to analyze
#text = u'Hello, world!'
#document = types.Document(
#    content=text,
#    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
#sentiment = client.analyze_sentiment(document=document).document_sentiment

#print('Text: {}'.format(text))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
