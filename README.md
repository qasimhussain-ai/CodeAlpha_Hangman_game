# CodeAlpha_Hangman_game
Hangman Game – CodeAlpha Internship Task

A simple and fun Hangman game developed as part of the CodeAlpha internship program.
The game selects a random word, and the player must guess it letter by letter before running out of attempts.

Features

Random word selection from a predefined list

Tracks correct and incorrect guesses

Displays current progress of the hidden word

Shows remaining attempts

Prevents repeated guesses

Clean and beginner-friendly code structure

Project Structure
CodeAlpha_Hangman_game/
│── hangman.py          # Main game script
│── words.txt           # Optional list of words
│── README.md           # Project documentation

How to Run

Install Python 3.13

Clone or download the project:

git clone https://github.com/your-username/CodeAlpha_Hangman_game.git


Navigate into the folder:

cd CodeAlpha_Hangman_game


Run the game:

python hangman.py

How the Game Works

The computer randomly selects a secret word

You guess letters one at a time

Correct guesses reveal letters in the word

Incorrect guesses reduce your remaining attempts

You win by completing the word

You lose when your attempts reach zero

Sample Gameplay
Word: _ _ _ _ _
Attempts left: 6
Wrong letters:

Guess a letter: a
Good guess!

Word: a _ a _ _
Attempts left: 6
Wrong letters:

Requirements

Python 3.13

No additional libraries required

Customization

Add or modify words in words.txt

Edit the internal word list inside hangman.py

Contribution

You are welcome to contribute by:

Improving the game logic

Adding a GUI or web version

Implementing difficulty levels

Submitting pull requests

License

This project is open-source and free to use.
