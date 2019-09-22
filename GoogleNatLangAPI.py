# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys
if sys.version_info < (3,):
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

# Instantiates a client
client = language.LanguageServiceClient()

def GetSentiment(t):   # Return sentiment of submitted text
    # Convert submitted text to unicode (required by API)
    text = u(t)
    result = []
    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    #result = '{}, {}'.format(sentiment.score, sentiment.magnitude)
    result.append(sentiment.score)
    result.append(sentiment.magnitude)
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
