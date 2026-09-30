# Terminal Tic-Tac-Toe: A Python Command-Line Experience

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

### Table of Contents
1. [Overview of the Project](#overview-of-the-project)
2. [Objectives & Motivation](#objectives--motivation)
3. [Features & Functional Requirements](#features--functional-requirements)
4. [Non-Functional Requirements](#non-functional-requirements)
5. [System Workflow & Architecture](#system-workflow--architecture)
6. [Technologies & Tools Used](#technologies--tools-used)
7. [Steps to Install & Run the Project](#steps-to-install--run-the-project)
8. [Instructions for Testing](#instructions-for-testing)
9. [Future Enhancements](#future-enhancements)
10. [Screenshots](#screenshots)

---

### Overview of the Project
This project is a robust, command-line implementation of the classic Tic-Tac-Toe game, entirely scripted in Python. Built with simplicity and functionality in mind, it provides an interactive terminal interface where users can engage in the traditional 3x3 grid game. 

Developed as part of the **VITyarthi - Build Your Own Project** flipped course evaluation, this application demonstrates fundamental computer science concepts, including game loop mechanics, array manipulation, state management, and algorithmic win-condition checking. 

### Objectives & Motivation
The primary objective of this project is to apply theoretical programming concepts into a tangible, real-world application. By identifying the requirements for a turn-based game, this project successfully implements:
* A meaningful problem-solving structure for grid management.
* A clear, logical technical solution using standard control flow.
* A fully documented and evaluated piece of software that meets both functional and non-functional academic expectations.

---

### Features & Functional Requirements
The system comprises several major functional modules that dictate the flow of the game:

* **Dual Game Modes (Mode Selection Module):** 
  * *Local Multiplayer:* Pass-and-play style gaming where two human players take turns as 'X' and 'O'.
  * *Single Player vs. CPU:* Play against an automated computer opponent that utilizes the `random` module to make dynamic, unpredictable moves on available grid spaces.
* **Intelligent Game State Detection (Winning & Draw Modules):** 
  * The system continuously evaluates the 1D list representing the board to detect 8 possible win conditions (3 horizontal, 3 vertical, 2 diagonal).
  * It detects a draw state when all 9 slots are filled with no victor, preventing infinite loops.
* **Input Management (Player Move Module):** 
  * Safely captures user input from the terminal and maps it to the corresponding 0-indexed list position.
* **Continuous Play Loop (Replay Module):** 
  * Upon concluding a match (win, loss, or draw), the game gracefully offers a replay prompt, allowing users to restart immediately without needing to re-execute the script.

---

### Non-Functional Requirements
To ensure a high-quality user experience and maintainable code base, the following non-functional requirements were established and met:

* **Usability:** The CLI provides a clear, ASCII-based visual representation of the board after every turn. Input prompts are descriptive, and users only need basic keyboard number keys to play.
* **Reliability & Error Handling:** The system acts defensively against bad user input. It prevents application crashes by catching non-integer inputs, out-of-bounds selections (numbers outside 1-9), and prevents overwriting occupied cells.
* **Performance:** The game relies entirely on lightweight standard libraries. State checks (winning conditions) are hardcoded into an efficient tuple lookup `(Victory list)`, ensuring execution times are virtually instantaneous.
* **Maintainability:** The code is heavily modularized. Functions like `CreateBoard()`, `ShowBoard()`, and `ComputerTurn()` isolate specific logic, making it easy to debug, scale, or introduce new features later.

---

### System Workflow & Architecture
The logical workflow of the user interaction is as follows:
1. **Initialization:** The script triggers `main()`, which invokes `Mode()` to determine if the opponent is a Human or Computer.
2. **Setup:** `StartPlaying(mode)` generates a fresh 9-slot board via `CreateBoard()`.
3. **Game Loop:** 
   * `ShowBoard()` prints the current state.
   * Based on whose turn it is, either `PlayerMove()` or `ComputerTurn()` is called.
   * The board array is updated with 'X' or 'O'.
4. **Validation:** `Winning()` and `MakingBoard()` check if the recent move resulted in a win or a full board (draw).
5. **Resolution:** If the game is over, the result is printed, and `OneMoreTime()` asks the user for a replay. If yes, the loop resets. If no, the application terminates gracefully.

---

### Technologies & Tools Used
* **Programming Language:** Python 3.x (Core logic, control flow, and UI rendering)
* **Standard Libraries:** 
  * `random`: Utilized for generating unbiased, valid moves for the computer opponent by selecting from an array of currently empty board indices.
* **Version Control:** Git & GitHub (for repository management, versioning, and submission compliance).

---

### Steps to Install & Run the Project
1. **Prerequisites Verification:** Ensure you have Python 3 installed on your operating system. You can verify this by opening your terminal/command prompt and typing:
   ```bash
   python --version
   ```
2. **Clone the Repository:** Download the project files to your local machine using Git:
   ```bash
   git clone <your-repository-url-here>
   cd <repository-directory-name>
   ```
3. **Execution:** Launch the game by running the Python script directly from your terminal:
   ```bash
   python main.py
   ```
4. **Gameplay:** Read the terminal prompts. Select your game mode by entering `1` or `2`. When playing, use the numbers `1` through `9` on your keyboard to place your marker on the corresponding grid position.

---

### Instructions for Testing
To ensure all modules and constraints function exactly as intended, follow this testing checklist:

#### 1. Boundary & Input Validation
* **Action:** During a prompt for a square, enter `0`, `10`, a letter (e.g., `A`), a symbol, or press Enter without typing.
* **Expected Result:** The system should reject the input safely, print "Please enter a number from 1 to 9," and reprompt the user without crashing.

#### 2. Overwrite Protection Validation
* **Action:** Place an 'X' in square `5`. On the next turn, attempt to place an 'O' in square `5`.
* **Expected Result:** The system should state "That square already occupied. Choose another one." and allow the player to try again.

#### 3. Victory Condition Triggers
* **Action:** Play a two-player game. Successfully place markers in squares `1`, `2`, and `3` (Horizontal win). Repeat for a vertical win (e.g., `1`, `4`, `7`) and diagonal win (e.g., `1`, `5`, `9`).
* **Expected Result:** The system should immediately print the winning message and ask if the users want to play again upon the 3rd aligned marker.

#### 4. Draw State Resolution
* **Action:** Play a game deliberately filling the board so no three markers align (e.g., X on 1, 3, 4, 8, 9 and O on 2, 5, 6, 7).
* **Expected Result:** The system should detect no winner, recognize the board is full, print "The game is a draw!", and offer a replay.

#### 5. Automated Opponent (AI) Validation
* **Action:** Select Mode `2` (Play against computer). Place your first marker.
* **Expected Result:** The script should autonomously select a valid, empty index, print "Computer chooses square [N]", and render the board with an 'O' in that position.

---

### Future Enhancements
Given more time and resources, this project could be expanded with the following features:
* **Minimax Algorithm:** Upgrading the `random` module AI to a Minimax algorithm to create an "unbeatable" AI mode.
* **Graphical User Interface (GUI):** Migrating from the terminal to a visual interface using Python's `Tkinter` or `Pygame` libraries.
* **Score Tracking & Database:** Implementing a local database (SQLite) or a simple JSON file implementation to track win/loss records across multiple gaming sessions.

---

### Screenshots
*(Note: Replace the bracketed text below with actual image links/files before final submission to GitHub)*

* **Figure 1: Main Menu & Mode Selection**
  `[Insert screenshot showing the "Game modes: 1. Two players 2. Play against the computer" prompt]`
* **Figure 2: Active Gameplay & ASCII Board**
  `[Insert screenshot showing a game in progress with markers on the board]`
* **Figure 3: Input Validation & Error Catching**
  `[Insert screenshot showing the system rejecting a letter input or an occupied space]`
* **Figure 4: Victory/Draw Screen**
  `[Insert screenshot showing the final board state and the "PLAYER WINS" or "DRAW" message]`