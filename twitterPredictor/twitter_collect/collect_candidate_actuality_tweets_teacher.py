import os
from tweet_collect.twitter_connection_setup import twitter_setup
from tweepy.error import RateLimitError

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    file_name_keywords = 'keywords_candidate_' + str(num_candidate) + '.txt'
    file_name_hashtags = 'hashtag_candidate_' + str(num_candidate) + '.txt'
    path_keywords = os.path.join(file_path, file_name_keywords)
    path_hashtags = os.path.join(file_path, file_name_hashtags)

    try:
        keywords = open(path_keywords).readlines()
        hashtags = open(path_hashtags).readlines()
        print('The loaded keywords : {}'.format(keywords))
        print('The loaded hashtags : {}'.format(hashtags))

        return keywords+hashtags

    except IOError:
        print('The file cannot be opened, please check the given path / condidate number')


def get_tweets_from_candidates_search_queries(queries, twitter_api):
    '''
    Now we'll do a terme based seach for each query and hashtag and return the queries
    '''

    results = []
    try:
        for query in queries:
            query_result = twitter_api.search(query, language="french", rpp=100)
            results.append(query_result)
    except RateLimitError:
        print('An error occurred during the query, please check the API')

    return results

############## Testing #################
if __name__ == "__main__": # If we execute this file
    queries_0 = get_candidate_queries(0, '../CandidateData')
    api_instance = twitter_setup()
    query_results_0 = get_tweets_from_candidates_search_queries(queries_0, api_instance)
    for tweet in query_results_0[0]:
        print('-> {}\n'.format(tweet.text))
