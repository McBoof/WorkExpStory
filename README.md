# Collaborative Storytelling Program 🌟

A Python program where multiple contributors implement bot classes that each contribute one sentence to a shared story.

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd collaborative-storytelling
   ```

2. **Run the program:**
   ```bash
   python main.py
   ```

3. **See the magic happen!**
   The program will generate a collaborative story with contributions from all bots.

## 🤖 How It Works

- Each contributor has their own bot class in the `bots/` directory
- Every bot contributes exactly one sentence to the story
- The `StoryOrchestrator` calls each bot in sequence to build the complete story
- Currently, all bots say "Hello [Name]" but you can customize this!

## 🎯 Contributing Your Story

### Step 1: Find Your Bot
Navigate to the `bots/` directory and find your bot file:
- `willow_bot.py` - Willow's bot
- `kate_bot.py` - Kate's bot  
- `katie_bot.py` - Katie's bot
- `sophia_bot.py` - Sophia's bot
- `zac_bot.py` - Zac's bot
- `zak_bot.py` - Zak's bot
- `eden_bot.py` - Eden's bot
- `nathan_bot.py` - Nathan's bot
- `noah_bot.py` - Noah's bot
- `samuel_bot.py` - Samuel's bot
- `william_bot.py` - William's bot

### Step 2: Customize Your Sentence
Edit the `get_sentence()` method in your bot class:

```python
def get_sentence(self):
    """
    Generate your sentence for the story.
    
    Returns:
        str: Your contribution to the story
    """
    # Replace this with your creative sentence!
    return "Your amazing sentence here!"
