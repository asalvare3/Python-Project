import tweepy
import time
from credentials import *

'''
class MyStreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
            # returning non-False reconnects the stream, with backoff.
    
    def on_status(self, status):
        print(status.text)
'''

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#stream = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=stream)

while True:
    since_id = 0
    result = api.mentions_timeline()
    print(result)
    time.sleep(12)
