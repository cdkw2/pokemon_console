# Pokemon Battle Simulator
## Introduction
Welcome to the Pokemon Battle Simulator! This simple Python script allows you to experience exciting Pokemon battles by randomly assigning you and your opponent a Pokemon. Test your skills and see who emerges victorious!

## Getting Started
To get started, follow these steps:

1. Ensure you have Python installed on your system.
2. Download the main.py script.
3. Open a terminal or command prompt, navigate to the directory containing the script, and run it using the command: python main.py
4. The script will generate a random Pokemon for you and your opponent.
## Gameplay
The game is played in a turn-based manner:

You will be presented with a list of options during your turn, such as attacking, using an item, or switching Pokemon.
Choose your action by typing the corresponding number and pressing Enter.
Your opponent will also choose an action.
Each turn, the chosen actions will play out, and the Pokemon will use their selected moves.
The battle will continue until one Pokemon's HP reaches zero, and the other Pokemon will be declared the winner.
## Code Overview
The script is written in Python and consists of several functions:

- random_pokemon(): Generates a random Pokemon for the player and the opponent.
- attack(): Calculates the damage done by an attack based on attack and defense stats, with a chance of a critical hit.
- game_loop(): Runs the main game loop, handling the player's input and the Pokemon battle.

The script includes a list of Pokemon and their stats, as well as a list of attacks and their properties.

## Quick Note
This project was created as a 25-minute challenge, so there are several areas for improvement, such as implementing ~~actual type advantages~~, providing a choice of attacks, and enabling Pokemon switching during battles. Depending on my free time and interest, I may or may not update this project, or perhaps I will create a new one from scratch. Regardless, I hope you enjoy this simple Pokemon battle simulation!
