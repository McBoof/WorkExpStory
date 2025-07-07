from base_bot import BaseBot
import random

class WilliamBot(BaseBot):

    # Class-level lists of story components
    characters = ["a young wizard", "a brave knight", "a curious cat", "an old pirate", "a talking tree"]
    settings = ["in a mystical forest", "on a distant planet", "in an ancient castle", "at the edge of the sea", "in a hidden cave"]
    actions = ["found a magical artifact", "discovered a secret path", "fought a fearsome dragon", "befriended a stranger", "solved an ancient riddle"]
    conflicts = ["and had to escape a curse", "but was betrayed by a friend", "and encountered an evil sorcerer", "while being hunted by shadows", "and uncovered a dark secret"]
    resolutions = ["and became a hero", "and changed the fate of the world", "and found peace", "and lived happily ever after", "and restored balance to the realm"]

    def __init__(self):
        """Initialize William's bot."""
        super().__init__("William")

    def generate_story(self):
        character = random.choice(self.characters)
        setting = random.choice(self.settings)
        action = random.choice(self.actions)
        conflict = random.choice(self.conflicts)
        resolution = random.choice(self.resolutions)

        story = f"{character} {setting} {action} {conflict}, {resolution}."
        return story

    def get_sentence(self):
        return self.generate_story()
