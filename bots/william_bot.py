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

            # Part 1: Beginning
            part1 = (
                f"{character.capitalize()} {setting} lived a quiet and peaceful life, far from the troubles of the world. "
                f"They spent their days exploring, learning, and dreaming of adventure, unaware that fate had other plans."
            )

            # Part 2: Middle (Two action-conflict events)
            action1 = random.choice(self.actions)
            conflict1 = random.choice(self.conflicts)
            action2 = random.choice(self.actions)
            conflict2 = random.choice(self.conflicts)

            part2 = (
                f" One fateful morning, everything changed when they {action1} {conflict1}. "
                f"As they searched for answers, they soon {action2} {conflict2}. "
                f"Each step brought new danger, but also a glimmer of hope."
            )

            # Part 3: End
            resolution = random.choice(self.resolutions)
            part3 = (
                f" After facing countless challenges, {character.split()[1]} stood tall against the odds. "
                f"Through wisdom, bravery, and heart, they {resolution}. "
                f"The world would never forget their journey."
            )

            return part1 + part2 + part3


    def get_sentence(self):
        return self.generate_story()
