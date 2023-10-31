import flag
import requests
from . import Ninjas, COUNTRIES


class NinjasCountry(Ninjas):

    def __init__(self):
        super().__init__('country')

    def all_info(self, variable):
        api_url = self.url + self.endpoint + '?name=' + variable
        response = requests.get(api_url, headers=self.headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return 'Error:', response.status_code, response.json()

    def homicide_rate(self):
        tweet_content = "Homicide rates per 100,000 people:\n\n"
        tweets = []
        for country in COUNTRIES:
            try:
                data = self.all_info(country)
                tweet_content += f"{flag.flag(data[0]['iso2'])} {data[0]['name']}: {data[0]['homicide_rate']}\n"
                if len(tweet_content) > 250:
                    tweets.append(tweet_content)
                    tweet_content = ""
            except Exception as e:
                print(f"Error: {e}, {country} not found.")
        return tweets

    def population(self):
        tweet_content = "Country population:\n\n"
        tweets = []
        for country in COUNTRIES:
            try:
                data = self.all_info(country)
                number = int(data[0]['population']) * 1000
                formatted_number = '{:,}'.format(number).replace(',', ' ')
                tweet_content += f"{flag.flag(data[0]['iso2'])} {data[0]['name']}: {formatted_number}\n"
                print(tweet_content)
                if len(tweet_content) > 250:
                    tweets.append(tweet_content)
                    tweet_content = ""
            except Exception as e:
                print(f"Error: {e}, {country} not found.")
        return tweets
