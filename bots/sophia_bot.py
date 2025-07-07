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
        return f"Jake thought the graveyard was just an old place—silent, forgotten. But when the moon rose, the silence turned into whispers.The cracked headstones seemed to shift, leaning closer as he walked. Suddenly, cold fingers grabbed his ankle from the dirt, dragging him toward an open grave filled with rotting hands clawing from below.The air reeked of decay as the dead rose, their eyes empty but burning with hunger. Jake tried to run, but the ground swallowed his screams, pulling him under the earth where the lost whispered, “Stay with us… forever.”{self.name}"
