import tweepy
import time
import urllib.request
from credentials import *

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def dwn_image(result):
    image = result.entities.get('media', [])
    if(len(image) > 0):
        # wget.download(image)
        urllib.request.urlretrieve(image, '/home/vamato9/Documents/School/Python/Python_Project/Images')
# stream = MyStreamListener()
# myStream = tweepy.Stream(auth = api.auth, listener=stream)


while True:
    since_id = 988883933889728511  # change to read from a config file
    result = api.mentions_timeline(since_id)

    with open('latestMentions.txt', 'w') as f:
        for row in result:
            f.write("%s\n" % str(row))

    # Process latest mentions
    with open('latestMentions.txt', 'r') as f:
        line = f.readline()
        line.split('Status')

        # For each tweet...
        # Find new ID to update since_id
        line = line.split(' ')
        since_id = line[12][0:-1]
        # Grab image

        # Call image processor

        dwn_image(line)

        # Reply
    time.sleep(12)
