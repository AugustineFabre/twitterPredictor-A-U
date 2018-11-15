import json
# on a avec la fonction collect une liste de dictionnaire
# on transforme cette liste en liste de liste
def liste(tweet):
    L=[]
    for D in tweet:
        L1=[]
        for clé in d.keys():
            L1.append("'clé' : D[clé]")
        L.append(L1)
    return L


def store_tweets(tweets,filename):
    # tweets est une liste de liste
    with open('filename'.json, 'w', encoding='utf-8') as f:
        tweet_json=json.dump(tweets, f, indent=4)
    print tweet_json




