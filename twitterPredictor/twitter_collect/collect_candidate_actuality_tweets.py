def get_tweets_from_candidates_search_queries(queries, twitter_api):
    connexion=twitter_api
    tweet=[]
    for querie in queries:
        tweet=tweet+[connexion.search("querie",language="french",rpp=50)]
    return tweet




