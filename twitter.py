class Twitter:

    def __init__(self, account_client):
        self.account_client = account_client

    # Post a tweet
    def post(self, status, tweet_id=None):
        if tweet_id is None:
            tweet = self.account_client.create_tweet(text=status)
        else:
            tweet = self.account_client.create_tweet(text=status, in_reply_to_tweet_id=tweet_id)
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
