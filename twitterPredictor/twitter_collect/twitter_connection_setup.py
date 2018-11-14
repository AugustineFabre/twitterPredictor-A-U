import tweepy
from codingweeks.tweet_collection.credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    from tweepy.api import API

    #authentification and access using keys:
    authentification=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET )
    authentification.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

    #return API with authentification
    api=tweepy.API(authentification)
    return api

def test_twitter_setup():
    api=twitter_setup()
    if api== <tweepy.api.API object at 0x00000171582A7DA0>:
        return "test réussi"
    else:
        return "échec"


