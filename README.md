# Tuple Out Dice Game

## Description
The Tuple Out Dice Game is a simple two-player dice game implemented in Python. Players take turns rolling dice to score points, with the objective of being the first to reach 20 points. However, players must avoid "tuple out" rolls (all three dice showing the same number), which result in scoring 0 points for that turn.

This game is interactive, allowing players to decide whether to reroll unfixed dice during their turn.

---

## Rules
1. Each player takes turns rolling three dice.
2. If all three dice show the same value (e.g., `[3, 3, 3]`), the player "tuples out" and scores **0 points** for that turn.
3. If two dice match, they are **fixed** and cannot be rerolled.
4. Players may choose to reroll unfixed dice as many times as they like during their turn.
5. When a player chooses to stop rerolling, their turn ends, and their score for that turn is the sum of all three dice.
6. The game ends as soon as one player reaches or exceeds 20 points.

---

## Features
- Interactive gameplay where players decide whether to reroll unfixed dice.
- Proper handling of "tuple out" rolls, scoring 0 points for all matching dice.
- Alternating turns between two players until one reaches the target score.
- Real-time display of current scores after each turn.

---

## Requirements
- Python 3.x installed on your system.

---

## How to Run
1. Clone this repository or download the `main.py` file.
2. Open a terminal and navigate to the folder containing `main.py`.
3. Run the game by executing:
   ```bash
   python main.py
