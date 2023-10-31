from twitter.twitter import Twitter

# twitter = Twitter(client)
# twitter.post_with_media("Test image", "/Users/maxime_hrt/Downloads/DALL·E Indonesian woman sewing.png")

image_path = "PATH_TO_IMAGE"
twitter = Twitter()
twitter.post_with_media("Test image", image_path)
