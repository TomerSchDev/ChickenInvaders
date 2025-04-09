# Chicken-Invaders-Clone

A Python-based clone of the classic arcade game Chicken Invaders. Defend Earth from waves of intergalactic chickens!

## Overview

This project aims to recreate the fun and engaging gameplay of Chicken Invaders using Python and a suitable game development library (like Pygame). Players control a spaceship at the bottom of the screen and must shoot down hordes of descending chickens while dodging their eggs and other projectiles.

## Features (Planned/Potential)

* **Wave-Based Gameplay:** Chickens will attack in distinct waves with increasing difficulty.
* **Player Control:** Smooth movement of the player's spaceship along the bottom of the screen.
* **Shooting Mechanism:** Ability to fire projectiles upwards to defeat the chickens.
* **Chicken Behavior:** Different types of chickens with varying movement patterns and attack styles.
* **Chicken Projectiles:** Chickens will fire eggs or other projectiles at the player.
* **Power-ups:** Collectible items that grant the player temporary advantages (e.g., faster shooting, wider shots, shields).
* **Scoring System:** Keep track of the player's score based on the number of chickens defeated.
* **Multiple Levels/Stages:** Progress through increasingly challenging levels with new chicken formations and attack patterns.
* **Boss Battles:** Encounter challenging boss chickens at the end of certain levels.
* **Sound Effects and Music:** Enhance the gaming experience with appropriate sound effects and background music.
* **Graphical Assets:** Visual elements for the spaceship, chickens, projectiles, and background.
* **Collision Detection:** Accurate detection of collisions between player projectiles and chickens, as well as chicken projectiles and the player.
* **Game Over Condition:** Determine when the game ends (e.g., player losing all lives).
* **User Interface:** Display score, lives, and other relevant game information.

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Pygame (Recommended):** Install the Pygame library, a popular choice for 2D game development in Python:
    ```bash
    pip install pygame
    ```
    *(Note: Other libraries like `arcade` or `Kivy` could also be used, but this README will assume Pygame.)*

### How to Run

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [repository_url]
    cd Chicken-Invaders-Clone
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt  # If a requirements.txt file exists
    ```

3.  **Run the main game script:**
    ```bash
    python main.py
    ```
    * Replace `main.py` with the actual name of the main game file.

### Project Structure (Example using Pygame)
hicken-Invaders-Clone/
├── assets/
│   ├── images/          # Images for spaceship, chickens, projectiles, etc.
│   ├── sounds/          # Sound effects
│   └── music/           # Background music
├── src/
│   ├── main.py          # Main game loop and initialization
│   ├── player.py        # Player spaceship class
│   ├── chicken.py       # Chicken enemy class
│   ├── projectile.py    # Projectile class (player and enemy)
│   ├── wave.py          # Class to manage chicken waves
│   ├── powerup.py       # Power-up item class
│   ├── game_state.py    # Class to manage the overall game state
│   ├── ui.py            # (Optional) Class for user interface elements
│   └── ... (other game logic modules)
├── README.md
├── requirements.txt    # List of project dependencies
Markdown

# Chicken-Invaders-Clone

A Python-based clone of the classic arcade game Chicken Invaders. Defend Earth from waves of intergalactic chickens!

## Overview

This project aims to recreate the fun and engaging gameplay of Chicken Invaders using Python and a suitable game development library (like Pygame). Players control a spaceship at the bottom of the screen and must shoot down hordes of descending chickens while dodging their eggs and other projectiles.

## Features (Planned/Potential)

* **Wave-Based Gameplay:** Chickens will attack in distinct waves with increasing difficulty.
* **Player Control:** Smooth movement of the player's spaceship along the bottom of the screen.
* **Shooting Mechanism:** Ability to fire projectiles upwards to defeat the chickens.
* **Chicken Behavior:** Different types of chickens with varying movement patterns and attack styles.
* **Chicken Projectiles:** Chickens will fire eggs or other projectiles at the player.
* **Power-ups:** Collectible items that grant the player temporary advantages (e.g., faster shooting, wider shots, shields).
* **Scoring System:** Keep track of the player's score based on the number of chickens defeated.
* **Multiple Levels/Stages:** Progress through increasingly challenging levels with new chicken formations and attack patterns.
* **Boss Battles:** Encounter challenging boss chickens at the end of certain levels.
* **Sound Effects and Music:** Enhance the gaming experience with appropriate sound effects and background music.
* **Graphical Assets:** Visual elements for the spaceship, chickens, projectiles, and background.
* **Collision Detection:** Accurate detection of collisions between player projectiles and chickens, as well as chicken projectiles and the player.
* **Game Over Condition:** Determine when the game ends (e.g., player losing all lives).
* **User Interface:** Display score, lives, and other relevant game information.

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Pygame (Recommended):** Install the Pygame library, a popular choice for 2D game development in Python:
    ```bash
    pip install pygame
    ```
    *(Note: Other libraries like `arcade` or `Kivy` could also be used, but this README will assume Pygame.)*

### How to Run

1.  **Clone the repository (if applicable):**
    ```bash
    git clone [repository_url]
    cd Chicken-Invaders-Clone
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt  # If a requirements.txt file exists
    ```

3.  **Run the main game script:**
    ```bash
    python main.py
    ```
    * Replace `main.py` with the actual name of the main game file.


## Core Game Mechanics (Conceptual)

1.  **Initialization:** Set up the game window, load assets, initialize game objects (player, initial chicken wave).
2.  **Game Loop:** Continuously process events (user input, game logic), update game state, and render graphics.
3.  **Player Input:** Handle keyboard or mouse input for player movement and shooting.
4.  **Object Updates:** Update the position and state of all game objects (player, chickens, projectiles, power-ups).
5.  **Collision Detection:** Check for collisions between different game objects and handle the consequences (e.g., destroying a chicken, player taking damage).
6.  **Scoring:** Increment the score when chickens are defeated.
7.  **Wave Management:** Introduce new waves of chickens after the current wave is cleared. Increase difficulty over time.
8.  **Game Over:** Determine when the player has lost all lives and display the game over screen.

## Further Development

* **More Chicken Types:** Implement chickens with different sizes, speeds, attack patterns, and health.
* **Varied Power-ups:** Add a wider range of power-ups with different effects.
* **Boss Levels:** Design challenging boss encounters with unique attack patterns.
* **Multiplayer Mode:** Allow two players to cooperate in defending against the chicken invasion.
* **Improved Graphics and Sound:** Enhance the visual and auditory experience.
* **Level Design:** Create more intricate and challenging level layouts.
* **Difficulty Levels:** Implement different difficulty settings to cater to various skill levels.
* **Saving and Loading:** Allow players to save their progress and resume the game later.

## License

MIT License

## Author
Tomer Schwartz
