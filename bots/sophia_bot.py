"""
Sophia's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class SophiaBot(BaseBot):
    """
    Sophia's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Sophia's bot."""
        super().__init__("Sophia")
    
    def get_sentence(self):
        """
       story
        """
        return f"A single backpack, a fading map, and a quiet road ahead. laptops, unfamiliar, yet exciting.real, something worth remembering {self.name}"
