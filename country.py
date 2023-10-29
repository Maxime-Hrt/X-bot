import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_url = 'https://api.api-ninjas.com/v1/country?name=United States'
response = requests.get(api_url, headers={'X-Api-Key': os.getenv('NINJAS_KEY')})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print('Error:', response.status_code, response.text)
