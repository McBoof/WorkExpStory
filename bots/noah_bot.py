from base_bot import BaseBot

import requests


def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        position = data['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']

        return "the ISS is currently at: " + str(latitude) + str(longitude)


class NoahBot(BaseBot):
    def __init__(self):
        super().__init__("Noah")

    def get_sentence(self):
        sentance = "I am NoahBot : "
        sentance = sentance + str(get_iss_location())
        return sentance

