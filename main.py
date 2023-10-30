import subprocess
from ninjas.country import NinjasCountry
from twitter_api import post_tweet_with_reply


subprocess.call(["python", "setup.py"])

tweets = NinjasCountry().homicide_rate()
tweet_ids = post_tweet_with_reply(tweets)
print(tweet_ids)
