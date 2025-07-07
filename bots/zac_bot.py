"""
Zac's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class ZacBot(BaseBot):
    """
    Zac's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Zac's bot."""
        super().__init__("Zac")
    
    def get_sentence(self):
        """
        Generate Zac's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: Zac's contribution to the story
        """
        return f"Hello my name is {self.name} And I am NOT a sigma cookie"
