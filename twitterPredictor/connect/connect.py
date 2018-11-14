import tweepy
from codingweeks.tweet_collection.credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    return: the authentified API
    """
    from tweepy.api import API

    #authentification and access using keys:
    authentification=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    authentification.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    #return API with authentification
    api=tweepy.API(authentification)
    return api
def collect():
    connexion =twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)



def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

