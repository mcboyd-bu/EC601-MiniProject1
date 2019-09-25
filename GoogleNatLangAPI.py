# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import sys
import re
from nltk.tokenize import TweetTokenizer

# Unicode-encode the text, for both Python 2.x and 3.x
if sys.version_info < (3,):
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

# Instantiates a client
client = language.LanguageServiceClient()

# Clean the tweet text before analyzing it - borrowed from https://www.freecodecamp.org/news/how-to-make-your-own-sentiment-analyzer-using-python-and-googles-natural-language-api-9e91e1c493e/
def clean_tweet(tweet):
    if not isinstance(tweet, str):
        tweet = tweet.decode('utf-8')
    user_removed = re.sub(r'@[A-Za-z0-9]+','',tweet)
    link_removed = re.sub('https?://[A-Za-z0-9./]+','',user_removed)
    #number_removed = re.sub('[^a-zA-Z]', ' ', link_removed)
    lower_case_tweet= link_removed.lower()
    tok = TweetTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet

def GetSentiment(t):   # Return sentiment of submitted text
    # Clean submitted text
    clean_t = clean_tweet(t)
    # Convert cleaned text to unicode (required by API)
    text = u(clean_t)
    result = []
    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    #result = '{}, {}'.format(sentiment.score, sentiment.magnitude)
    result.append(t)
    result.append(clean_t)
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
