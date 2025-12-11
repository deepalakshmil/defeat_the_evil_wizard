# Defeat the Evil Wizard

Defeat the Evil Wizard is a text-based adventure game built in Python. The objective is to create a character, choose a class, and battle the Evil Wizard using attacks, special abilities, and healing strategies. Each character class has unique skills that affect combat outcomes, making every playthrough different.

This project demonstrates object-oriented programming concepts in Python, including classes, inheritance, and polymorphism, as well as basic game logic implementation.

Technology Stack

- Language: Python 3

- Concepts: Object-Oriented Programming (Classes & Inheritance)

- Modules Used: random for attack and health variability

- Gameplay: Text-based, terminal/console interface

Features

- Five character classes: Warrior, Mage, Rogue, Kael, Ninja

- Each class has two unique special abilities

- Actions include Attack, Special Ability, Heal, and View Stats

- Battle against the Evil Wizard, who regenerates health and attacks strategically

- Real-time updates of health and stats during combat

- Win or lose messages displayed at the end of the game

Installation and Running the Game

1. Clone or download the repository to your local machine.

2. Ensure Python 3 is installed.

3. Save the project files classes.py and game_logic.py in the same folder.

4. Open a terminal and navigate to the project folder.

5. Run the game with:

python game_logic.py

How to Play

1. When the game starts, you’ll see a welcome message:

Welcome to our Gaming Program

2. Choose your character class by entering the corresponding number:

1 - Warrior

2 - Mage

3 - Rogue

4 - Kael

5 - Ninja

3. Enter your character’s name.

4. During battle, choose an action each turn:

1 - Attack

2 - Use Special Ability

3 - Heal

4 - View Stats

5. The Evil Wizard will attack and regenerate health automatically after your turn.

6. Continue until either your character or the Evil Wizard is defeated.

7. At the end, the game displays who won.

Character Abilities

Each character class has two unique special abilities that can dramatically influence the outcome of the battle. Plan your strategy carefully to defeat the Evil Wizard.

Example Gameplay
Choose Your Character Class: 1
Enter Your Character's Name: Aragon

\***\* Your Turn \*\***

1. Attack
2. Use Special Ability
3. Heal
4. View Stats
   Choose an action: 1
   Aragon attacks The Dark Wizard for 25 damage!!
   The Dark Wizard has 115 remaining

Notes

- The game runs entirely in the terminal.

- Health, attack power, and regeneration are determined randomly within each class's limits.

- Try different classes and abilities to experience multiple battle outcomes.
