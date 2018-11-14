import tweepy
from twitter_collect.twitter import *

def collect():
    connexion = twitterPredictor.twitter_collect.twitter_connection_setup.twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


