from codingweeks.twitterPredictor.twitter_collect.tweet_collect_whole import *
from codingweeks.twitterPredictor.twitter_collect.twitter_connection_setup import *
from tweepy import api

connexion = twitter_setup()
queries = get_candidate_queries()

queries_0 = queries[0]
queries_1 = queries[1]
def get_tweets_from_candidates_search_queries(queries):
    for query in queries:
        tweets = connexion.search(query,language="french",rpp=10)
        for tweet in tweets:
            print(tweet.text)


tweets_0 = get_tweets_from_candidates_search_queries(queries_0)
tweets_1 = get_tweets_from_candidates_search_queries(queries_1)


