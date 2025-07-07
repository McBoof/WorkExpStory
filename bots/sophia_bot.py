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
        Generate Sophia's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: Sophia's contribution to the story
        """
        return f"Hello {self.name}"
