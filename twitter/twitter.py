import time
import tweepy

from .setup import get_twitter_conn_v1, get_twitter_conn_v2


class Twitter:
    def __init__(self):
        self.client_v1 = get_twitter_conn_v1()
        self.client_v2 = get_twitter_conn_v2()

    # Post a tweet - can be used to reply to a tweet
    def post(self, status, tweet_id=None):
        if tweet_id is None:
            tweet = self.client_v2.create_tweet(text=status)
        else:
            tweet = self.client_v2.create_tweet(text=status, in_reply_to_tweet_id=tweet_id)
        return tweet

    # Post a tweet, if the tweet is too long, split it into multiple tweets
    def post_tweet_with_reply(self, tweets):
        tweet_ids = []
        for i, tweet in enumerate(tweets):
            if i == 0:
                tweet_id = self.post(tweet)
                tweet_ids.append(tweet_id)
            else:
                tweet_id = self.post(tweet, tweet_ids[i - 1].data.get('id'))
                tweet_ids.append(tweet_id)
        return tweet_ids

    # Post a tweet with an image - can be used to reply to a tweet
    def post_with_media(self, status, media_paths, tweet_id=None):
        media_ids = []
        for media_path in media_paths:
            media = self.client_v1.media_upload(filename=media_path)
            media_ids.append(media.media_id)

        if tweet_id is None:
            tweet = self.client_v2.create_tweet(text=status, media_ids=media_ids)
        else:
            tweet = self.client_v2.create_tweet(text=status, media_ids=media_ids, in_reply_to_tweet_id=tweet_id)
        return tweet

    def post_with_media_handling_rate_limit(self, status, media_paths, tweet_id):
        while True:
            try:
                return self.post_with_media(
                    status=status,
                    media_paths=media_paths,
                    tweet_id=tweet_id
                )
            except tweepy.TooManyRequests as e:
                reset_time = int(e.response.headers.get('X-Rate-Limit-Reset'))
                delay = max(reset_time - time.time(), 0) + 10
                print(f"Rate limit exceeded. Waiting for {delay} seconds.")
                time.sleep(delay)
            except Exception as e:
                raise e
