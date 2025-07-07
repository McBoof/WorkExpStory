from base_bot import BaseBot


class ZakBot(BaseBot):

    def __init__(self):

        super().__init__("Zak")

    def get_sentence(self):

        return f"My name is {self.name}. I am cool"
