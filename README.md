Tzino Payout Calculator

Tzino Payout Calculator is a simple command-line-based game that allows multiple players to place bets on the outcome of a lottery draw. The lottery result can be either "Odd" or "Even". Players can choose between two types of leap, "Greater" or "Master", although it does not affect the game's result or payouts. The calculator then displays the winners, their payouts, and their respective leap type.

How the code works
The code is organized into several functions to improve readability and maintainability:

get_input(prompt, validation_func): A helper function to obtain user input and validate it with the provided validation function.
get_positive_int(value): A validation function to check if the input value is a positive integer.
get_valid_choice(value, choices): A validation function to check if the input value is within a set of allowed choices.
get_player(): Gathers input for a single player's details (name, bet size, leap, and pick) and returns a dictionary containing the player's data.
get_players(): Calls get_player() repeatedly to obtain a list of players, until the user decides to stop adding players.
confirm(prompt): A function to get a confirmation (yes/no) from the user.
calculate_payout(players, result): Calculates the payouts for each player based on their bets and the lottery result.
display_winners(players): Displays the list of winners, their payouts, and their leap type.
start_game(): The main game loop that repeatedly calls functions to get players' input, calculates payouts, and displays winners.
When executed, the script enters an infinite loop where each iteration represents one round of the game. For each round, the script prompts users to input player data, lottery result, and calculates payouts based on the user input. If the user decides to reset the game, the script starts over from the beginning. The game exits if the user decides not to reset.

Usage
To run the Tzino Payout Calculator, simply execute the script using Python:

Copy code
python tzino_payout_calculator.py
Then follow the on-screen prompts to input player data, lottery result, and decide whether to reset the game or exit.
