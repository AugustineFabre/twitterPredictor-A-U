from textblob import TextBlob
from textblob import Word

from twitterPredictor.twitter_collect import twitter_connection_setup
from twitterPredictor.twitter_collect.to_dataframe import *

import nltk
nltk.download('punkt')
L=['A','après','avant','avec','chez','concernant','contre','dans','de','depuis','derrière','dès','devant','durant','en','entre','envers','hormis','hors','jusque','malgré','moyennant','nonobstant','outre','par','parmi','pendant','pour','près','sans','sauf','selon','sous','suivant','sur','touchant']
def recup_mot():
    data_pd_0,data_pd_1=myfonc()
    for num in data_pd_0['tweet_textual_content']:
        tweet=TextBlob(num)
        if tweet.detect_language()!='fr':
            tweet=tweet.translate(to='fr')
        final=tweet.words
        right=[]
        for j in final:
            right.append(j.lemmatize())
        for i in range(len(right)):
            if right[i] in L:
                right.pop(i)
        print right
#on défini les tweets positifs de Emmanuel Macron et Marine Le Pen
data_pd_0,data_pd_1=myfonc()

def positivite():
    tweets=data_pd_0['tweet_textual_content']
    tweets_positif_0=[]
    tweets_negatif_0=[]
    tweets_neutre_0=[]
    for tweet in tweets:
        tweet=TextBlob(tweet)
        if tweet.sentiment.polarity>0.2: # on détermine les tweets positifs comme ayant une positivité supérieure à 0.2
            tweets_positif_0.append(tweet)
        if -0.2<tweet.sentiment.polarity<0.2:
            tweets_neutre_0.append(tweet)
        else:
            tweets_negatif_0.append(tweet)# on détermine les tweets positifs comme ayant une positivité inférieure à -0.2
    tweets_1=data_pd_0['tweet_textual_content']
    tweets_positif_1=[]
    tweets_negatif_1=[]
    tweets_neutre_1=[]
    for tweet in tweets_1:
        tweet=TextBlob(tweet)
        if tweet.sentiment.polarity>0.2:
            tweets_positif_1.append(tweet)
        if -0.2<tweet.sentiment.polarity<0.2:
            tweets_neutre_1.append(tweet)
        else:
            tweets_negatif_1.append(tweet)
    return tweets_positif_0,tweets_negatif_0,tweets_neutre_0,tweets_positif_1,tweets_negatif_1,tweets_neutre_1

tweets_positif_0,tweets_negatif_0,tweets_neutre_0,tweets_positif_1,tweets_negatif_1,tweets_neutre_1=positivite()

print("Percentage of positive tweets: {}%".format(len(tweets_positif_0)*100/len(data_pd_0['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(tweets_neutre_0)*100/len(data_pd_0['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(tweets_negatif_0)*100/len(data_pd_0['tweet_textual_content'])))



print("Percentage of positive tweets: {}%".format(len(tweets_positif_1)*100/len(data_pd_1['tweet_textual_content'])))
print("Percentage of neutral tweets: {}%".format(len(tweets_neutre_1)*100/len(data_pd_1['tweet_textual_content'])))
print("Percentage de negative tweets: {}%".format(len(tweets_negatif_1)*100/len(data_pd_1['tweet_textual_content'])))





