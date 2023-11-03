import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

_API_KEY = os.getenv('API_KEY')
_API_SECRET = os.getenv('API_KEY_SECRET')
# _BEARER_TOKEN = os.getenv('BEARER_TOKEN')
_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
_ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


def get_twitter_conn_v1():
    auth = tweepy.OAuth1UserHandler(_API_KEY, _API_SECRET)
    auth.set_access_token(_ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True)


def get_twitter_conn_v2():
    client = tweepy.Client(
        consumer_key=_API_KEY,
        consumer_secret=_API_SECRET,
        access_token=_ACCESS_TOKEN,
        access_token_secret=_ACCESS_TOKEN_SECRET
    )
    return client
