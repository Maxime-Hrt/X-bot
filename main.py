import flag
from twitter.twitter import Twitter
from lib.file_functions import split_list
from media.media import Media

# TODO: Reply with the location of the photo & Maps link (credit photographer)
# TODO: Improve Status
# TODO: Run on a Server
# TODO: Save daily analytics on an excel sheet

twitter = Twitter()
media = Media('Kawah Ijen')
media.download_all()

media_path = split_list(f'media/images/{media.location}', [1, 4, 7])
tweet_id = None
status = f'{flag.flag("ID")} {media.location}, Indonesia'
for i, media in enumerate(media_path):
    if tweet_id is not None:
        tweet_id = tweet_id.data.get('id')
        status = ' '

    print(tweet_id)
    print(status)
    tweet_id = twitter.post_with_media(
        status=status,
        media_paths=media,
        tweet_id=tweet_id
    )
