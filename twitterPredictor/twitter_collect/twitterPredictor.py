import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

def transform_to_dataFrame(tweets):      ## prends en objet liste des tweets 
    tweet=tweets[0]   ## récupération informations relatives au premier tweet de la liste 
    tweet_data=pd.DataFrame({ 'A' : pd.Timestamp('tweet[date]'),
                              'B' : pd.Categorical(['tweet[message]']),
                              'C' : pd.Categorigal(['tweet[retweet]']),
                              'D' : 'tweet[auteur]' })  ## ajout date/auteur/retweet/message du tweet dans le dataframe 
    for tweet in tweets[1:]:                            ## parcours des tweets 
        tweet_transform=pd.DataFrame({ 'A' : pd.Timestamp('tweet[date]'),
                                       'B' : pd.Categorical(['tweet[message]']),
                                       'C' : pd.Categorigal(['tweet[retweet]']),
                                       'D' : 'tweet[auteur]' }) ## conversion du tweet en dataframe 
        pieces=[tweet_data,tweet_transform]
        tweet_data=pd.concact(pieces) ## concaténation du dataframe formé par le tweet et du dataframe contenant les autres tweets 
    return tweet_data


    





                
                    
        
        
                                

