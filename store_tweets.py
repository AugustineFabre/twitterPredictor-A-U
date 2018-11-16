from tweet_collect.twitter_connection_setup import twitter_setup
from tweet_collect.collect_candidate_actuality_tweets_teacher import get_candidate_queries, get_tweets_from_candidates_search_queries
import json
import tweepy

def serizer_tweets(tweet):
    if isinstance(tweet, tweepy.models.Status):
        return {"text": str(tweet.text),
                "id": tweet.id,
                "retweeted": tweet.retweeted,
                "retweet_count": tweet.retweet_count,
                "favorite_count": tweet.favorite_count,
                "created_at": tweet.created_at.isoformat(),
                "followers_count": tweet.user.followers_count,
                "description": str(tweet.user.description),
                "name": tweet.user.name}
    raise TypeError(repr(tweet) + " Not the same object type")

def store_tweets(queries, filename):
    json_to_dump = []
    for query in queries:
        print(query.__class__)
        for tweet in query:
            json_to_dump.append(serizer_tweets(tweet))
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_to_dump, f, indent=4)

if __name__ == "__main__":  # If we execute this file
    num_condidat = 1
    queries = get_candidate_queries(num_condidat, '../CandidateData')
    api_instance = twitter_setup()
    queries_results = get_tweets_from_candidates_search_queries(queries, api_instance)
    output_filename = '../jsonDump/tweets_condidat_'+ str(num_condidat) + '.json'
    store_tweets(queries_results, output_filename)

    num_condidat = 0
    queries = get_candidate_queries(num_condidat, '../CandidateData')
    api_instance = twitter_setup()
    queries_results = get_tweets_from_candidates_search_queries(queries, api_instance)
    output_filename = '../jsonDump/tweets_condidat_'+ str(num_condidat) + '.json'
    store_tweets(queries_results, output_filename)


#question:favorite_count:0 ?????????
