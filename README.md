# 15-112-Term-Project
A fast paced, procedurally generated tunnel runner game built in Python featuring real-time 3D transformations, a custom physics engine, and dynamic gameplay. 

Overview: 
- RUN112 is a 2.5D tunnel runner game where players navigate through a procedurally generated tunnel, avoiding the holes and making sure the player stays on the platforms.

Key Features: 
- Procedural Generation: Infinite tunnel with dynamically generated platforms and randomly spawning obstacles
- 3D Depth Perception: Used mathematical transformations to create realistic depth and scaling effects
- Custom Physics Engine: 
    - Gravity Simulation with vertical velocity and acceleration
    - Collision detection algorithms
    - Platform rotation mechanics
    - Smooth character movement
- Progressive Difficulty: Levels increase the speed of the character and increases the amount of black holes that are generated
- Character Customization: Custom RGB color mixer to customize character as well as 7 preset color options
- Polished UI: Home screen with animated character, Settings menu for color selection, Pause functionality, Game Over screen with score tracking
- Background Music: Integrated pygame audio system


How To Play:
- Controls:
    - Left/Right Arrow Keys: Move character horizontally
    - Spacebar: Jump
    - Mouse: Navigate menus and pause
- Gameplay:
    - Start by clicking "PLAY" on the homescreen
    - Navigate through the tunnel by jumping and moving left and right, avoiding the black holes that come towards the screen
    - Jump on other platforms to rotate the tunnel and avoid the black holes
 
Project Structure:
- main.py: Initializes CMU Graphics, handles the main event loop, manages the game states, and coordinates the different classes of objects (player, tunnel, platforms, background)
- character.py: Defines the Player class, which handles movement, physics, and collision
- platforms.py: Initializes the tunnel and handles platform mechanics
- background.py: Handles UI and other visual elements

Installation Requirements: 
- Python 3.8+
- pip package manager
- cmu-graphics and pygame installation

Team Contributions:
- Genti Aliaj:
    - Ball movement physics and gravity simulation
    - 3D tunnel rendering and mathematical transformations
    - Platform rotation mechanics and collision detection
    - Procedural generation and random hole spawning
- Eileen Jung:
    - Designed home, settings, and game over screen
    - Implemented level progression system
    - Integrated music
- Gabbie Boone:
    - Color customization system
    - Pause functionality
    - Character design

We made this game for a term project for **15-112: Fundamentals of Programming and Computer Science**.
  





