from twitter.twitter import Twitter
from media.pexel import get_id_large_2x_top, download_media

twitter = Twitter()
media_path = get_id_large_2x_top('Bromo')
filename = download_media(media_path['photo'], media_path['alt'])
twitter.post_with_media(status='Stunning Mountain', media_path=filename)
