# Collaborative Storytelling Program

## Overview

This is a Python-based collaborative storytelling application where multiple contributors implement bot classes that each contribute one sentence to a shared story. The program uses a modular architecture with a base bot class that defines the interface, individual bot implementations for each contributor, and a story orchestrator that coordinates the storytelling process.

## System Architecture

### Architecture Pattern
- **Object-Oriented Design**: Uses inheritance with a base class (`BaseBot`) that defines the interface for all story bots
- **Plugin Architecture**: Each contributor has their own bot class that can be independently developed and modified
- **Orchestrator Pattern**: A central `StoryOrchestrator` class manages the coordination of all bots and story assembly

### Core Components
1. **Base Bot Class** (`base_bot.py`): Defines the interface that all story bots must implement
2. **Individual Bot Classes** (`bots/` directory): Each contributor's unique bot implementation
3. **Story Orchestrator** (`story_orchestrator.py`): Coordinates the storytelling process
4. **Main Entry Point** (`main.py`): Application entry point and user interface

## Key Components

### BaseBot Class
- **Purpose**: Defines the contract for all story bots
- **Key Methods**: 
  - `__init__(name)`: Initialize with contributor name
  - `get_sentence()`: Abstract method that must be implemented by each bot
- **Design Decision**: Uses inheritance to ensure consistent interface across all bots

### Individual Bot Classes
- **Location**: `bots/` directory
- **Pattern**: Each bot inherits from `BaseBot` and implements `get_sentence()`
- **Contributors**: 11 individual bots (Willow, Kate, Katie, Sophia, Zac, Zak, Eden, Nathan, Noah, Samuel, William)
- **Current State**: All bots return placeholder "Hello [Name]" messages

### Story Orchestrator
- **Purpose**: Manages the sequence of bot contributions and assembles the final story
- **Key Features**:
  - Automatically discovers and initializes all bot classes
  - Handles errors gracefully if a bot fails
  - Collects sentences from each bot in sequence
  - Provides feedback during the story creation process

### Bots Package
- **Structure**: Uses `__init__.py` to expose all bot classes
- **Registry**: Maintains `ALL_BOTS` list for easy discovery
- **Import Strategy**: Imports all bot classes to make them accessible to the orchestrator

## Data Flow

1. **Initialization**: `StoryOrchestrator` imports all bot classes from the `bots` package
2. **Bot Creation**: Each bot class is instantiated with error handling
3. **Story Generation**: Orchestrator calls `get_sentence()` on each bot in sequence
4. **Assembly**: Individual sentences are collected into a story list
5. **Output**: Complete story is displayed with numbered sentences

## External Dependencies

- **Python Standard Library Only**: No external dependencies required
- **Deployment**: Simple Python script execution (`python main.py`)

## Deployment Strategy

### Current Setup
- **Runtime**: Python 3.x
- **Execution**: Direct script execution via `python main.py`
- **No Build Process**: Pure Python with no compilation or build steps required

### Scalability Considerations
- **Adding Contributors**: New bots can be added by creating new bot files in the `bots/` directory and updating the `__init__.py` file
- **Modification**: Each contributor can independently modify their bot without affecting others
- **Error Isolation**: Bot failures don't crash the entire program

## User Preferences

Preferred communication style: Simple, everyday language.

## Changelog

Changelog:
- July 07, 2025. Initial setup