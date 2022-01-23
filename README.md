# cse210-02

# Hilo
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

# Rules
The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.

# Project Structure
Director
	Methods:
		start_game()
		get_input()
		show_points()
		do_updates()		
Card
	Methods:
		get_value()

# Authors
Carina Aguero\
Rob Cox\
Brianna Dayley\
Anamilena Casariego\
Eduardo Pulido
