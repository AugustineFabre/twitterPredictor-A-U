import json

def store_tweets(tweets,filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(playlist, f, indent=4)
