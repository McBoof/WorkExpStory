"""
Nathan's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class NathanBot(BaseBot):
    """
    Nathan's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Nathan's bot."""
        super().__init__("Nathan")
    
    def get_sentence(self):
        """
        Generate Nathan's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: Nathan's contribution to the story
        """
        return f"Hello {self.name}"
