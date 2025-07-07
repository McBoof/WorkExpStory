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
        return f"Hello my name is {self.name} and here is some random story chat gpt made called the Echoes of Andaris: In the year 2498, Earth is dying. Centuries of exploitation have left the atmosphere toxic and oceans acidic. Humanity’s last hope lies in a distant exoplanet: Andaris-9, a lush, uncolonized world discovered beyond the Orion Belt Aboard the interstellar ark Eos, Captain Naima Rho leads a diverse team of scientists, engineers, and civilians—10,000 souls in stasis. Their journey takes 42 years through folded space. When they awaken, something is wrong. The planet is alive. Not biologically—consciously. Strange electromagnetic pulses distort their equipment. Drones vanish. Whispers echo in the minds of the crew. The Andarian forest reshapes itself at will. Dr. Malik, a linguist, uncovers ancient carvings predicting their arrival. It wasn’t an accident. The planet has been waiting. It begins to communicate through dreams—revealing that it’s a sentient biosphere, a world-mind once worshipped by a long-dead civilization. It offers salvation: in exchange for becoming part of it. No more machines. No more control. Unity—or extinction. Captain Rho must choose: merge with a living planet and give up humanity’s independence—or try to terraform it and risk war with a consciousness older than Earth. The crew is divided. The final message from Andaris is clear: You came seeking refuge. Now you must decide who you are. And the forest watches. PART TWO COMING OUT SOON!"
