import os
import json
import flag
import requests

class Media:
    def __init__(self, location):
        self.location = location

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
