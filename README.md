# Tic-Tac-Toe

A simple text-based Tic-Tac-Toe game built with Python.

This project was developed as part of my Python learning journey, with a focus on practicing functions, dictionaries, sets, loops, input validation, and game logic.

## Features

* Two-player gameplay
* Text-based interface
* 3×3 game board
* Player 1 uses `X`
* Player 2 uses `O`
* Input validation
* Prevents players from choosing occupied positions
* Detects horizontal, vertical, and diagonal wins
* Detects draws
* Handles invalid and non-numeric input
* Displays the game board after each valid move

## How to Play

1. Run the Python program.
2. Player 1 starts with `X`.
3. Player 2 uses `O`.
4. Enter a number from `1` to `9` to select a position.

The board positions are:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Players take turns selecting an available position.

The first player to complete a row, column, or diagonal wins.

If all nine positions are occupied without a winner, the game ends in a draw.

## Project Structure

```text
tic-tac-toe/
│
├── main.py
└── README.md
```

## Technologies

* Python 3
* Python Standard Library

## Concepts Practiced

This project helped me practice:

* Functions and parameters
* Return values
* Dictionaries
* Sets
* Dictionary comprehension
* Loops
* Conditional statements
* Input validation
* Exception handling with `try` / `except`
* Game-state management
* Set operations with `issubset()`
* Organizing logic into reusable functions

## What I Learned

The main focus of this project was not just making the game work, but breaking the problem into smaller responsibilities.

Instead of putting the entire game inside one large loop, different parts of the game were separated into functions such as board creation, move validation, move recording, winner detection, draw detection, and player switching.

This made the game logic easier to understand, test, and maintain.

## Future Improvements

Possible future improvements include:

* Adding a single-player mode against the computer
* Adding difficulty levels
* Improving the terminal interface
* Keeping a game score between rounds
* Allowing players to restart without restarting the program

## Getting Started

Clone the repository and run `main.py` with Python 3.

```bash
python main.py
```
