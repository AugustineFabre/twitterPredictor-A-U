from tweet_collect.twitter_connection_setup import *
from tweepy.streaming import StreamListener

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True


def collect_by_streaming(candidate_name):


    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener = listener)
    stream.filter(track=[candidate_name])



#collect_by_streaming('Emmanuel Macron')
#collect_by_streaming('Marine Le Pen')
