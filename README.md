# tick-tack-toe

This is a Python implementation of the classic Tic-Tac-Toe game using the tkinter library for the graphical user interface (GUI).
The game allows a player to play against the computer, where the player is X and the computer is O. The computer makes random moves using the random module.

Features:
Interactive GUI: Built using tkinter for a user-friendly experience.
Player vs Computer: The player (X) competes against the computer (O).
Win and Tie Detection: The game automatically detects when a player wins or if the game ends in a tie.
Reset Functionality: The board resets automatically after a win or tie, allowing for continuous play.

How It Works:
The game starts with an empty 3x3 grid.
The player clicks on a cell to place an X.
The computer randomly selects an available cell to place an O.
The game checks for a win or tie after each move.
If a win or tie is detected, a message box displays the result, and the board resets for a new game.

Functions:
1- create_board(): Initializes the 3x3 grid of buttons for the game board.
2- button_click(row, col): Handles player moves, updates the board, and triggers the computer's move.
3- check_win(): Checks if the current player has won the game.
4- reset_board(): Resets the board for a new game.
5- computer_move(): Randomly selects an available cell for the computer's move.

Dependencies:
tkinter: For creating the GUI.
random: For the computer's random move selection.
