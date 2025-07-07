import requests
from base_bot import BaseBot

class JonBot(BaseBot):

    def __init__(self):
        super().__init__("Jon")

    def get_dad_joke(self):
        url = "https://icanhazdadjoke.com/"
        headers = {
            "Accept": "application/json",
            "User-Agent": "JonBot (you@example.com)"  # customize this
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["joke"]

    def get_sentence(self):
        return self.get_dad_joke()
