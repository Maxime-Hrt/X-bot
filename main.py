import tweepy
from db import DB
from twitter.twitter import Twitter
from media.media import Media

# TODO:
#   Reply with the location of the photo & Maps link
#   Run on a Server
#   Save daily analytics on an excel sheet
#   Use the SerpAPI to get the popular destinations
# FIXME:
#   Fix the issue with the file names
#   Handle error with unrecognized location

# from serpapi import GoogleSearch
#
# params = {
#   "engine": "google",
#   "q": "Palawan Destinations",
#   "api_key": os.getenv('SERP_API_KEY'),
# }
#
# search = GoogleSearch(params)
# results = search.get_dict()
# popular_destinations = results["popular_destinations"]
# print(popular_destinations)

# location = 'El Nido'
# media = Media(location, Twitter())
# media.post()

# twitter = Twitter()
# for tweet in tweepy.Cursor(twitter.client_v1.search_tweets, "Twitter", count=100).items():
#     print(tweet.id)


# db = DB()
# task_1 = (1719782336533831913, 'San Marino', 'San Marino', "01/11/2023")
# db.add_tweet(task_1)

# twitter = Twitter()
# tweet = twitter.post('Hello World')
# tweet_id = tweet.data.get('id')
# db.add_tweet((tweet_id, "Paris", "France", "03/11/2023"))
# db.delete_tweet_by_location("Paris")
