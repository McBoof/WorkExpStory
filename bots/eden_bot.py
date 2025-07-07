"""
Eden's Bot Implementation
Contributes one sentence to the collaborative story.
"""

from base_bot import BaseBot
import random 

class EdenBot(BaseBot):
    """
    Eden's storytelling bot.
    Customize the get_sentence() method to contribute your unique sentence!
    """
    
    def __init__(self):
        """Initialize Eden's bot."""
        super().__init__("Eden")
    
    def get_sentence(self):
        actions = ["woke up early", "found a mysterious map", "felt a strange feeling", "read the headlines", "took a bite of his breakfast", "said hello to his mother", "fell down the stairs", "walked into a lamppost"]
        names = ["Eden", "Noah", "Kate", "Katie", "He", "Samuel", "Sophia", "William", "Willow", "Zac", "Zak", "Jon"]

        return f"{self.name} {actions[random.randint(0,len(actions)-1)]} and {names[random.randint(0,len(names)-1)]} {actions[random.randint(0,len(actions)-1)]}"
