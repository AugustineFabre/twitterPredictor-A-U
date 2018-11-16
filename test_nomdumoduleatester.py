from twitter_predictor.twitter_collect import collect
from pytest import *


def test_collect():
    tweets = tweet_collect.collect()
    data =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns
    
def test_collect2():
    from twitterPredictor.py import *
    tweets = tweet_collect.collect()
    data =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns
    

    