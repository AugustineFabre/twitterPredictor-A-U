import pandas as pd
import json

def transform_to_dict(tweet):
    return {"tweet_textual_content": str(tweet["text"]),
            "len" : len(tweet["text"]),
            "likes": tweet["favorite_count"],
            "RTs": tweet["retweet_count"],
            "Date": tweet["created_at"]}

def transform_to_dataframe(tweets):
    dict_list = []
    for tweet in tweets:
        dict_list.append(transform_to_dict(tweet))
    data_frame = pd.DataFrame(dict_list)
    return data_frame



def myfonc():
    dict_list_0 = []
    with open('../jsonDump/tweets_condidat_0.json', 'r') as jsonfile_0:
        tweets_0 = json.load(jsonfile_0)
        for tweet_0 in tweets_0:
            dict_list_0.append(transform_to_dict(tweet_0))
        data_pd_0 = pd.DataFrame(dict_list_0)
        print(data_pd_0)

    dict_list_1 = []
    with open('../jsonDump/tweets_condidat_1.json', 'r') as jsonfile_1:
        tweets_1 = json.load(jsonfile_1)
        for tweet_1 in tweets_1:
            dict_list_1.append(transform_to_dict(tweet_1))
        data_pd_1 = pd.DataFrame(dict_list_1)
        print(data_pd_1)
    return data_pd_0, data_pd_1

#myfonc()

