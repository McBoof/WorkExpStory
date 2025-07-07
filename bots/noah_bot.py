"""
Noah's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot
class NoahBot(BaseBot):
    def __init__(self):
        super().__init__("Noah")

    def get_sentence(self):
        return f"HEELLOO II AAMM {self.name}"
