import sys
import flag
from twitter.twitter import Twitter
from lib.file_functions import generate_pattern, custom_split, get_file_paths
from media.media import Media
from lib.country import get_country_code

# TODO:
#   Reply with the location of the photo & Maps link
#   Run on a Server
#   Save daily analytics on an excel sheet
# FIXME:
#   Fix the issue with the file names
#   Handle error with unrecognized location


location = 'El Nido'
media = Media(location, Twitter())
media.post()