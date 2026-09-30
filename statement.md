# Problem Statement

The project aims to create a classic command-line Tic-Tac-Toe game where a user can choose to play against another human or face off against a computer opponent.

The game demonstrates core Python concepts such as functions, `while` and `for` loops, conditional statements, list indexing, random element selection, and user input validation.

## Scope of the Project

The project includes:

* Multiple game modes (Player vs. Player and Player vs. Computer).
* Dynamic 3x3 grid generation and display.
* Turn-based gameplay alternating between "X" and "O".
* Automated computer moves using random selection.
* Real-time win condition and draw detection.
* Input validation for invalid characters, out-of-bounds numbers, and occupied spaces.
* A replay prompt to allow continuous matches.

The game is designed as a command-line application.

## Target Users

* Python beginners
* Programming students learning game logic
* Students practicing list manipulation and conditionals
* People interested in simple terminal-based board games

## High-Level Features

1. **Multi-Mode Support** – Users can choose between a two-player local mode or playing against an automated computer.
2. **Dynamic Board** – The 3x3 grid updates and prints cleanly to the console after every valid move.
3. **Computer Opponent** – The computer scans the board for available spaces and randomly selects a valid square.
4. **Win/Draw Evaluation** – The system constantly checks against eight predefined winning combinations and board fullness to declare a victor or a tie.
5. **Robust Input Validation** – Prevents the game from crashing by catching non-integer inputs, out-of-bounds numbers (outside 1-9), and attempts to overwrite existing moves.
6. **Replayability** – Upon game completion, players are prompted to play again or exit cleanly.