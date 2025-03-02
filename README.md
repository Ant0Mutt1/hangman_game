# Hangman Game 🎮

Welcome to the **Hangman Game** repository! This is a Python implementation of the classic word-guessing game, Hangman. The game is designed to be modular, easy to extend, and fun to play. It includes features like hints, error tracking, and a clean presentation.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)


---

## Features ✨

- **Two Game Modes**:
  - Play with hints to get clues about the hidden word.
  - Play without hints for a more challenging experience.
- **Error Tracking**: The game tracks incorrect guesses and limits the number of attempts.
- **Dynamic Word Display**: The hidden word is revealed as you guess correct letters.
- **Used Letters Register**: Keeps track of all the letters you've already guessed.
- **Clean Presentation**: The game provides a clear and user-friendly interface.

---

## Installation 🛠️

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ant0Mutt1/hangman_game.git
   cd hangman_game
   ```

2. **Ensure you have Python installed**:
   - This project requires Python 3.7 or higher. You can check your Python version by running:
     ```bash
     python --version
     ```

3. **Run the game**:
   - Navigate to the project directory and run the main script:
     ```bash
     python main.py
     ```

---

## Usage 🎯

1. **Start the Game**:
   - When you run the game, you'll be prompted to choose a game mode:
     - **Option 1**: Play with hints.
     - **Option 2**: Play without hints.

2. **Gameplay**:
   - Guess letters one at a time.
   - If you guess a correct letter, it will be revealed in the hidden word.
   - If you guess incorrectly, the hangman stage will progress.
   - You have a limited number of attempts (default is 6).

3. **Winning or Losing**:
   - If you guess the word before running out of attempts, you win!
   - If you run out of attempts, the game ends, and the correct word is revealed.

---


## Contributing 🤝

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request and describe your changes.

---

Enjoy playing Hangman! If you have any questions or suggestions, feel free to open an issue or reach out. 😊
