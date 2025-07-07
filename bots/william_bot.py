"""
William's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot

class WilliamBot(BaseBot):
    """
    William's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize William's bot."""
        super().__init__("William")
    
    def get_sentence(self):
        """
        Generate William's sentence for the story.
        
        TODO: Customize this method to return your creative sentence!
        You can use self.name to reference your name in the sentence.
        
        Returns:
            str: William's contribution to the story
        """
        return f"Hello {self.name}"
