import sys
import flag
from twitter.twitter import Twitter
from lib.file_functions import generate_pattern, custom_split, get_file_paths
from media.media import Media
from lib.country import get_country_code

# TODO: Reply with the location of the photo & Maps link
# TODO: Improve Status -> Handle error with unrecognized location
# TODO: Run on a Server
# TODO: Save daily analytics on an excel sheet


def get_title(media_):
    country_code = get_country_code(media_.get_country_name())
    return f'{flag.flag(country_code)} {media_.location}, {media_.get_country_name()}'


# Connect to Twitter API
twitter = Twitter()
# Create Media Object
media = Media('Lisbon')
# Get the title of the tweet
try:
    status = get_title(media)
except Exception as e:
    print(f"Title error: {e}")
    sys.exit(1)
# Download all photos
photo_reference = media.download_all()
# Get the path of all photos
path = f'media/images/{media.location}'

# Get the pattern of the file names
file_path = get_file_paths(path)
pattern = generate_pattern(path)
media_path = custom_split(file_path, pattern)

# Post the photos
tweet_id = None
for i, media in enumerate(media_path):
    if tweet_id is not None:
        tweet_id = tweet_id.data.get('id')
        status = ' '

    tweet_id = twitter.post_with_media(
        status=status,
        media_paths=media,
        tweet_id=tweet_id
    )

# Post the authors
authors = [f'-{photo.get("author")} \n' for photo in photo_reference]
authors = "Photographers: \n" + ''.join(authors)
tweet_id = twitter.post(status=authors, tweet_id=tweet_id.data.get('id'))
print("Posted Successfully!")
