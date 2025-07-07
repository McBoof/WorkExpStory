from base_bot import BaseBot
import time

class ZakBot(BaseBot):

    def __init__(self):

        super().__init__("Zak")

    def get_sentence(self):

        time.sleep(2)

        return f"\nMy name is {self.name}. I made the code. It was difficult to get the repository to work. But unfortunately, something went wrong. Now I can't do anything but sing this stupid song!\n"
