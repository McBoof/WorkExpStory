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
        return f"Eli found the map in a dusty bookstore—hand-drawn, no names, just a red dot labeled Start here. On a whim, he followed it.The road led to places not on any GPS. A tea cart in the woods. Lanterns swaying with no wind. People who knew him before he spoke.Each night, the map changed—new dot, new path. It wasn’t guiding him across land, but through himself.By the final mark, Eli didn’t need the map anymore. He had become the story it was trying to tell.{self.name}"
