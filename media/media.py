import os
import sys
import json
import flag
import time
import tweepy
import requests

from serpapi import GoogleSearch
from lib.country import get_country_code
from lib.file_functions import get_file_paths, generate_pattern, custom_split


def get_photo_references(place_id):
    url = f'https://maps.googleapis.com/maps/api/place/details/json?'
    place_id_url = f'place_id={place_id}&fields=photo&key={os.getenv("PLACES_KEY")}'
    try:
        response = requests.get(url + place_id_url)
        if response.status_code == requests.codes.ok:
            photo_reference = []
            for photo in response.json()['result']['photos']:
                start_index = photo['html_attributions'][0].find(">")
                end_index = photo['html_attributions'][0].find("</")
                if start_index != -1 and end_index != -1:
                    author = photo['html_attributions'][0][start_index + 1:end_index]
                else:
                    author = None
                if photo['width'] > 1600 and photo['height'] > 1600:
                    photo_reference.append({
                        'photo': photo['photo_reference'],
                        'author': author
                    })
            return photo_reference
        else:
            return 'Error:', response.status_code, response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_places_of_interest_serpapi(place):
    params = {
        "engine": "google",
        "q": f"{place} Destinations",
        "api_key": os.getenv('SERP_API_KEY'),
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    try:
        data = results["popular_destinations"]
        return [destination.get('title') for destination in data.get('destinations')]
    except Exception as e:
        try:
            print(f"Not find \"popular destinations\": {e}")
            data = results.get('top_sights').get('sights')
            return [sight.get('title') for sight in data]
        except Exception as e:
            print(f"Not find \"top sights\": {e}")
            return None


class Media:
    def __init__(self, location, twitter):
        self.location = location
        self.twitter = twitter

    # GET the place ID by querying the location (other parameters can be added)
    def get_places_id(self):
        url = 'https://places.googleapis.com/v1/places:searchText'
        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': os.getenv('PLACES_KEY'),
            'X-Goog-FieldMask': 'places.id'
        }
        payload = {
            'textQuery': self.location,
        }
        payload_json = json.dumps(payload)
        try:
            response = requests.post(url, headers=headers, data=payload_json)
            if response.status_code == requests.codes.ok:
                return response.json()
            else:
                return 'Error:', response.status_code, response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_places_id_top(self):
        data = self.get_places_id()
        if data is not None:
            return data['places'][0].get('id')
        else:
            return {'Error': 'No photos found'}

    def get_place_info(self):
        url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
        params = {
            'input': self.location,
            'inputtype': 'textquery',
            'fields': 'formatted_address,name,geometry',
            'language': 'en',
            'key': os.getenv('PLACES_KEY')
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == requests.codes.ok:
                return response.json()
            else:
                return 'Error:', response.status_code, response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_country_name(self):
        data = self.get_place_info()
        if data is not None:
            return data['candidates'][0]['formatted_address'].split(', ')[-1]
        else:
            return {'Error': 'No photos found'}

    def download_media(self, photo_references):
        # Create a folder for the location
        if not os.path.exists(f"media/images/{self.location}"):
            os.makedirs(f"media/images/{self.location}")
        os.chdir(f"media/images/{self.location}")

        for photo_reference in photo_references:
            url = 'https://maps.googleapis.com/maps/api/place/photo'
            params = {
                'maxwidth': 1600,
                'photo_reference': photo_reference['photo'],
                'key': os.getenv('PLACES_KEY')
            }
            try:
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    filename = photo_reference['author'].replace(' ', '_')
                    with open(f"{filename}.png", 'wb') as f:
                        f.write(response.content)
                    print(f'Success downloading {filename} photo')
                else:
                    print(f'Error when download: {response.status_code}')
            except Exception as e:
                print(f'Error downloading photo {e}')
        os.chdir('../../../')

    def download_all(self):
        media_path = self.get_places_id_top()
        photo_references = get_photo_references(media_path)
        # [print(photo.get('author')) for photo in photo_references]
        self.download_media(photo_references)
        return photo_references

    def get_title(self):
        country_code = get_country_code(self.get_country_name())
        return f'{flag.flag(country_code)} {self.location}, {self.get_country_name()}'

    def post(self):
        try:
            status = self.get_title()
        except Exception as e:
            print(f"Title error: {e}")
            sys.exit(1)
        # Download all photos
        photo_reference = self.download_all()
        # Get the path of all photos
        path = f'media/images/{self.location}'
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

            tweet_id = self.twitter.post_with_media_handling_rate_limit(
                status=status,
                media_paths=media,
                tweet_id=tweet_id
            )
        # Post the authors
        authors = [f'-{photo.get("author")} \n' for photo in photo_reference]
        authors = "Photographers: \n" + ''.join(authors)
        self.twitter.post(status=authors, tweet_id=tweet_id.data.get('id'))
        print("Posted Successfully!")
