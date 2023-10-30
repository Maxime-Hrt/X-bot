import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

_API_KEY = os.getenv('API_KEY')
_API_SECRET = os.getenv('API_KEY_SECRET')
_BEARER_TOKEN = os.getenv('BEARER_TOKEN')
_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
_ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(_BEARER_TOKEN, _API_KEY, _API_SECRET, _ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(_API_KEY, _API_SECRET, _ACCESS_TOKEN, _ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
