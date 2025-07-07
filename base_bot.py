"""
Base Bot Class
Defines the interface that all story bots must implement.
"""

class BaseBot:
    """
    Base class for all story bots.
    Each bot contributes one sentence to the collaborative story.
    """
    
    def __init__(self, name):
        """
        Initialize the bot with a name.
        
        Args:
            name (str): The name of the bot contributor
        """
        self.name = "evil sigma cookie  " + name
    
    def get_sentence(self):
        """
        Generate a sentence for the story.
        This method should be overridden by each bot implementation.
        
        Returns:
            str: A sentence to add to the story
        """
        raise NotImplementedError("Each bot must implement the get_sentence() method")
    
    def __str__(self):
        """String representation of the bot."""
        return f"{self.__class__.__name__}(name='{self.name}')"
