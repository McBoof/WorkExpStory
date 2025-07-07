"""
Nathan's Bot Implementation
Contributes one sentence to the collaborative story.
"""
import random
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
        actions = ["woke up early", "found a mysterious map", "felt a strange feeling", "read the headlines", "took a bite of his breakfast", "said hello to his mother", "fell down the stairs", "walked into a lamppost"]
        names = ["Eden", "Noah", "Kate", "Katie", "He", "Samuel", "Sophia", "William", "Willow", "Zac", "Zak", "Jon"]
        endings = ["die", "disappear", "get eaten", "win the lottery", "go to space", "eat some food"]
        times = ["that very second", "today", "tomorrow", "next week", "in 85 years", "in who knows how long", "while trying to save"+ random.choice(names)]

        characters = ["Eden", "Noah", "Kate", "Katie", "Samuel", "Sophia", "William", "Willow", "Zac", "Jon"]
        locations = ["in the haunted forest", "at the old lighthouse", "inside the abandoned castle", "on the mountain peak", "beneath the city streets"]
        emotions = ["fear", "hope", "despair", "determination", "curiosity", "anger"]

        character = random.choice(characters)
        location = random.choice(locations)
        emotion = random.choice(emotions)

        if emotion in ["fear", "despair"]:
            outcome = f"faced their darkest nightmare {location}, where even {character}’s courage faltered."
        elif emotion == "hope":
            outcome = f"found a glimmer of hope {location}, sparking a fire in their heart."
        else:
            outcome = f"embraced {emotion}, preparing for the challenges that lay ahead {location}."




        
        return (
            f"{self.name} {random.choice(actions)}, and knew that {random.choice(names)} would {random.choice(endings)} {random.choice(times)}./n"
            f"{self.name} whispered a prophecy: 'When {character} arrives {location}, "
            f"they must harness {emotion} or risk losing everything.' "
            f"And in that moment, the world held its breath."
        )
