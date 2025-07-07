"""
Eden's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class EdenBot(BaseBot):
    """
    Eden's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Eden's bot."""
        super().__init__("Eden")
    
    def get_sentence(self):
        """
        Generate Eden's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: Eden's contribution to the story
        """
        return "Big man Eden"
