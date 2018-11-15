from codingweeks.twitterPredictor.twitter_collect.twitter_connection_setup import *

from codingweeks.tweet_collection2.credentials import *

api = twitter_setup()


def get_replies_to_candidate(candidatename):
    candidat = api.get_user(candidatename) #从网址域名得username
    candidat_id = candidat.id
    print(candidat_id)
    retweets_0 = api.retweets(candidat_id, count=100)
    print(retweets_0)

def get_replies_to_candidate1():
    marine = api.get_user('EmmanuelMacron')
    marine_id = marine.id
    print(marine_id)
    retweets_1 = api.retweets(marine_id, count=100)
    print(retweets_1)

get_replies_to_candidate('EmmanuelMacron')
get_replies_to_candidate('MLP_officiel')

