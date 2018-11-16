from textblob import TextBlob

from tweet_collect import twitter_connection_setup
connexion = twitter_connection_setup.twitter_setup()

import nltk
nltk.download('punkt')

from tweet_collect.to_dataframe import *
data_pd_0, data_pd_1 = myfonc()

'''extraire le vocabulaire d'un ensemble de tweets en récupérant les mots uniques et lemmatisés. 
On pourra aussi supprimer de la liste obtenue les mots fréquents ou stop-words.'''

def correct_tweets(pd_tweets):
    for num in pd_tweets['tweet_textual_content']:
        tweet = TextBlob(num)
       # if tweet.detect_language() != 'en':
       #    tweet = tweet.translate(to='en')
        final = tweet.words
        #right = []
        #for j in final:
        #    right.append(j.lemmatize())
        right_final = []
        for word in final:
            if word != '.' and word != ',' and word != 'Il' and word != 'Je' and word != 'Elle':
                right_final.append(word)
    print(right_final)
    return right_final

final_tweets_0 = correct_tweets(data_pd_0)
final_tweets_1 = correct_tweets(data_pd_1)