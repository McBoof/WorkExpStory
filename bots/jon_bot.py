from base_bot import BaseBot


class JonBot(BaseBot):

    def __init__(self):
        super().__init__("Jon")

    def get_sentence(self):
        return f"Hello Jon Was Here"
