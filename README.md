Simple Cricket Game
This is a text-based cricket game implemented in Python, where players can choose to either bat or bowl against a computer opponent. The game allows players to score runs while trying to outsmart the computer by guessing numbers between 1 and 6.

Features:

Choose Your Role: Players can select to bat or bowl.
Interactive Gameplay: Players and the computer take turns guessing numbers to score runs.
Out Mechanic: If a player's guess matches the computer's random number, they are "out."
Score Tracking: The game keeps track of scores for both the player and the computer.
Match Outcome: The game announces the winner or if the match ends in a tie.

Requirements:

Python 3.x

Installation:

Clone the Repository:

git clone https://github.com/YathishPoojary98/simple-cricket-game.git

cd simple-cricket-game

Run the Game: Ensure you have Python installed, then run the following command:

python cricket.py

How to Play:

Start the game by choosing whether you want to bat (1) or bowl (2).
If you choose to bat, input your score by guessing a number between 1 and 6.
If you choose to bowl, input a number between 1 and 6 to try and outscore the player.
The game continues until one side is "out." The outcome of the match will be displayed at the end.

Example Game Flow:

Player selects to bat.
Player guesses a number (e.g., 4) to score runs.
The computer randomly generates a number (1-6).
If the player's guess matches the computer's number, they are out, and the computer takes its turn.
The match continues until all runs are scored or a player is out.
