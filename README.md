# Python Guess U.S. States Game

## Overview
This is an interactive game built with Python and the `turtle` and `pandas` libraries. The objective is to guess all 50 U.S. states by typing their names. Correctly guessed states will appear on the map, while missed states can be reviewed at the end of the game.

## Features
- Interactive map where users can guess U.S. states.
- Immediate feedback on correct guesses.
- Saves unguessed states to a CSV file for further practice.
- Simple and educational game for learning U.S. geography.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/IsaWng/python-guess-us-states-game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd python-guess-us-states-game
   ```
3. Install dependencies:
   ```sh
   pip install pandas turtle
   ```

## How to Play
1. Run the game script:
   ```sh
   python guess.py
   ```
2. A U.S. map will appear with a prompt asking you to enter state names.
3. Type the name of a state and press Enter.
4. Correct guesses will be marked on the map.
5. When you decide to quit, a CSV file (`states_to_learn.csv`) will be created with the states you missed.

## Dependencies
- Python 3.x
- `pandas`
- `turtle` (included with Python by default)

## Contribution
Feel free to contribute by opening an issue or submitting a pull request. Suggestions and improvements are welcome!

## License
This project is licensed under the MIT License. See `LICENSE` for details.

