import os
import requests


def get_photos(location):
    # Great wall of china => Greate%20wall%20of%20china
    formatted_loc = location.replace(' ', '%20')
    url = f'https://api.pexels.com/v1/search?query={formatted_loc}&per_page=15'
    headers = {
        'Authorization': os.getenv('PEXELS_KEY')
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'Error:', response.status_code, response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_id_large_2x(location):
    data = get_photos(location)
    photos = []
    if data is not None:
        for photo in data['photos']:
            photos.append(
                {
                    'id': photo['id'],
                    'photo': photo['src']['large2x'],
                }
            )
        return photos
    else:
        return {'Error': 'No photos found'}


def get_id_large_2x_top(location):
    data = get_photos(location)
    if data is not None:
        photo = data['photos'][0]
        return {
            'id': photo['id'],
            'photo': photo['src']['large2x'],
            'alt': photo['alt'],
        }
    else:
        return {'Error': 'No photos found'}


def download_media(url, alt):
    filename = 'media/images/' + alt.replace(' ', '_') + '.jpg'
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            with open(filename, 'wb') as file:
                file.write(response.content)
                return filename
        else:
            return 'Error:', response.status_code, response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None
