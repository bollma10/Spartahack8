# Spartahack8
This repository contains the project(s) developed by Nate Bollman and Justin Masters during MSU's Spartahack 8 on 1/28/2023-1/29/2023.

# Technologies
Our program uses Python, including the Pygame library, and Stockfish, the popular C++ based chess engine. 

# game.py
This is where the game is run. It creates a game, displays the game window with drawn chess boards, and uses user input to determine success or fail states. 

# PGN to FEN
The format of chess games in the online database we used is PGN, which is a string list of moves. We used an algorithm to convert this format to FEN, which is a string of piece positions, that we found at the following link.
https://github.com/SindreSvendby/pgnToFen/blob/master/pgntofen.py
