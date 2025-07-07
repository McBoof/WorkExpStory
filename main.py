#!/usr/bin/env python3
"""
Collaborative Storytelling Program
Main entry point for the storytelling application.
"""

from story_orchestrator import StoryOrchestrator

def main():
    """Main function to run the collaborative storytelling program."""
    print("🌟 Welcome to the Collaborative Storytelling Program! 🌟")
    print("=" * 60)
    
    # Create and run the story orchestrator
    orchestrator = StoryOrchestrator()
    story = orchestrator.create_story()
    
    # Display the complete story
    print("\n📖 Our Collaborative Story:")
    print("-" * 40)
    for i, sentence in enumerate(story, 1):
        print(f"{i}. {sentence}")
    
    print("-" * 40)
    print(f"✨ Story complete! Generated {len(story)} sentences from {len(story)} contributors.")
    print("\nTo contribute, edit your bot class in the bots/ directory!")

if __name__ == "__main__":
    main()
