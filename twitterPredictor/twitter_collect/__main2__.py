from tweet_collect.twitter_connection_setup import *
connexion = twitter_setup()

from tweet_collect.collect_candidate_tweet_activity import *
if __name__ == "__main__": # If we execute this file
    username = 'EmmanuelMacron'
    retweets_per_tweet_0 = get_retweets_of_candidate('EmmanuelMacron')
    for tweet, nb_rt in retweets_per_tweet_0.items():
        print('{}, the number of retweets are --> {}'.format(tweet, nb_rt))

if __name__ == "__main__": # If we execute this file
    username = 'MLP_official'
    retweets_per_tweet_1 = get_retweets_of_candidate('MLP_official')
    for tweet, nb_rt in retweets_per_tweet_1.items():
        print('{}, the number of retweets are --> {}'.format(tweet, nb_rt))


from tweet_collect.collect_candidate_actuality_tweets import *
collect_avec_search_tweets_0 = get_tweets_from_candidates_search_queries(queries_0)
collect_avec_search_tweets_1 = get_tweets_from_candidates_search_queries(queries_1)

from tweet_collect.collect_avec_streamfilter import *
collect_avec_stream_tweets_0 = collect_by_streaming('Emmanuel Macron')
collect_avec_stream_tweets_1 = collect_by_streaming('Marine Le Pen')