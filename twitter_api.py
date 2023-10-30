from setup import api, client


def create_tweet(status, tweet_id=None):
    if tweet_id is None:
        tweet = client.create_tweet(text=status)
    else:
        tweet = client.create_tweet(text=status, in_reply_to_tweet_id=tweet_id)
    return tweet


# Post a tweet, if the tweet is too long, split it into multiple tweets
def post_tweet_with_reply(tweets):
    tweet_ids = []
    for i, tweet in enumerate(tweets):
        if i == 0:
            tweet_id = create_tweet(tweet)
            tweet_ids.append(tweet_id)
        else:
            tweet_id = create_tweet(tweet, tweet_ids[i - 1].data.get('id'))
            tweet_ids.append(tweet_id)
    return tweet_ids
