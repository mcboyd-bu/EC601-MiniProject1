import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def Get_twitter(hashtag, time):
    tag = '#' + hashtag + ' -filter:retweets'
    text = []
    for tweet in tweepy.Cursor(api.search, q=tag, tweet_mode='extended', lang='en',until=time).items(30):
        text.append(tweet.full_text)
    return text



