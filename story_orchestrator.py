"""
Story Orchestrator
Coordinates the storytelling process by calling each bot in sequence.
"""

from bots import ALL_BOTS

class StoryOrchestrator:
    """
    Orchestrates the collaborative storytelling process.
    Manages the sequence of bot contributions and assembles the final story.
    """
    
    def __init__(self):
        """Initialize the story orchestrator."""
        self.bots = []
        self._initialize_bots()
    
    def _initialize_bots(self):
        """Initialize all bot instances."""
        for bot_class in ALL_BOTS:
            try:
                bot_instance = bot_class()
                self.bots.append(bot_instance)
                print(f"✅ Initialized {bot_instance}")
            except Exception as e:
                print(f"❌ Failed to initialize {bot_class.__name__}: {e}")
    
    def create_story(self):
        """
        Create a collaborative story by calling each bot in sequence.
        
        Returns:
            list: A list of sentences contributed by each bot
        """
        story_sentences = []
        
        print(f"\n🤖 Gathering contributions from {len(self.bots)} bots...")
        
        for i, bot in enumerate(self.bots, 1):
            try:
                sentence = bot.get_sentence()
                if sentence:
                    story_sentences.append(sentence)
                    print(f"  {i}. {bot.name}: {sentence}")
                else:
                    print(f"  {i}. {bot.name}: (no contribution)")
            except Exception as e:
                error_msg = f"Error from {bot.name}: {e}"
                story_sentences.append(error_msg)
                print(f"  {i}. {error_msg}")
        
        return story_sentences
    
    def get_bot_count(self):
        """
        Get the number of active bots.
        
        Returns:
            int: Number of initialized bots
        """
        return len(self.bots)
    
    def get_bot_names(self):
        """
        Get the names of all active bots.
        
        Returns:
            list: List of bot names
        """
        return [bot.name for bot in self.bots]
