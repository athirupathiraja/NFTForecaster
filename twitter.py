from tweepy.streaming import StreamListener
from tweepy import streaming
from tweepy import OAuthHandler
from tweepy import Stream

import twitterCredentials


class StdOutListener(StreamListener):

    def onData(self, data):
        print(data)
        return True

    def onError(self, status):
        print(status)
