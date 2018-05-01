import tweepy
import time
import urllib.request
from subprocess import call
from credentials import *


# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


while True:
    with open('since_id.txt') as i:
        since_id = i.readline().strip()
    result = api.mentions_timeline(since_id)

    # Left in for debug purposes. Really not necessary to the script.
    with open('latestMentions.txt', 'w') as f:
        for row in result:
            f.write("%s\n" % str(row))

    # For each tweet...
    for tweet in result:
        
        # Find new ID to update since_id
        since_id = tweet.id
        with open('since_id.txt', 'w') as o:
            o.write(str(since_id))

        # Grab image URL and download
        if 'media' in tweet.entities:
            for image in tweet.entities['media']:
                urllib.request.urlretrieve(image['media_url'], '/home/cody/pythonproject/TwT/image.jpg')
        
            # Call image processor
            call(["python", "label_image.py", "--graph=/tmp/output_graph.pb", "--labels=/tmp/output_labels.txt", "--input_layer=Placeholder", "--output_layer=final_result", "--image=/home/cody/pythonproject/TwT/image.jpg"])
                  
            # Reply

    time.sleep(12)
