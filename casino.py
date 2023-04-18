def get_input(prompt, validation_func):
    while True:
        try:
            value = input(prompt)
            validated_value = validation_func(value)
            return validated_value
        except ValueError as e:
            print(e)

def get_positive_int(value):
    parsed_value = int(value)
    if parsed_value < 0:
        raise ValueError("Value must be a positive integer.")
    return parsed_value

def get_valid_choice(value, choices):
    parsed_value = int(value)
    if parsed_value not in choices:
        raise ValueError(f"Invalid input. Please enter one of the following: {', '.join(map(str, choices))}.")
    return parsed_value

def get_player():
    player = {}
    player['name'] = input("Enter player name: ")
    player['betsize'] = get_input("Enter bet size: ", get_positive_int)
    player['leap'] = get_input("Enter 1 for Greater or 2 for Master: ", lambda value: get_valid_choice(value, [1, 2]))
    player['leap'] = 'Greater' if player['leap'] == 1 else 'Master'
    player['pick'] = get_input("Enter 1 for Odd or 2 for Even: ", lambda value: get_valid_choice(value, [1, 2]))
    player['pick'] = 'Odd' if player['pick'] == 1 else 'Even'
    return player

def get_players():
    players = []
    while True:
        player = get_player()
        players.append(player)
        if not confirm("Add another player? (y/n): "):
            break
    return players

def confirm(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def calculate_payout(players, result):
    total_payout = 0
    for player in players:
        if result == player['pick']:
            player['payout'] = player['betsize'] * 2
            player['result'] = "Won"
            total_payout += player['payout']
        else:
            player['payout'] = 0
            player['result'] = "Lost"
    return players, total_payout

def display_winners(players):
    print("\nTzino Casino Winners:")
    for player in players:
        if player['result'] == "Won":
            player['payout'] -= player['payout'] * 0.1
            print(f"\n{player['name']} Payout: {player['payout']} {player['leap']}")

def start_game():
    print("\nTzino Payout Calculator v0.1")
    round_num = 1
    while True:
        print(f"\nRound {round_num}")
        players = get_players()
        result = get_input("Lottery number? Enter 1 for Odd or 2 for Even: ", lambda value: get_valid_choice(value, [1, 2]))
        result = 'Odd' if result == 1 else 'Even'
        players, total_payout = calculate_payout(players, result)
        display_winners(players)
        round_num += 1
        if not confirm("\nReset and start from the beginning? (y/n): "):
            break

if __name__ == '__main__':
    start_game()
