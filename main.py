from twitter import Twitter
from ninjas.country import NinjasCountry
from setup import client


tweets = NinjasCountry().population()
twitter = Twitter(client)
tweet_ids = twitter.post_tweet_with_reply(tweets)
