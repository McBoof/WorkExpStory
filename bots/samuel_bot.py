"""
Samuel's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class SamuelBot(BaseBot):
    """
    Samuel's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Samuel's bot."""
        super().__init__("Samuel")
    
    def get_sentence(self):
        """
        Generate Samuel's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: Samuel's contribution to the story
        """
        return f"Long live  {self.name}king of kings as he rules the world with an iron fist. and leads his people to victory against the many offenders and their allies."
