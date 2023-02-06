def start_game(round_num):
    players = []

    while True:
        player = {}
        player['name'] = input("Enter player name: ")

        while True:
            try:
                player['betsize'] = int(input("Enter bet size: "))
                if player['betsize'] < 0:
                    print("Bet size cannot be negative. Please enter a positive value.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for bet size.")

        while True:
            try:
                player['leap'] = int(input("Enter 1 for Greater or 2 for Master: "))
                if player['leap'] not in [1, 2]:
                    print("Invalid input. Please enter 1 for Greater or 2 for Master.")
                    continue
                player['leap'] = 'Greater' if player['leap'] == 1 else 'Master'
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")        

        while True:
            try:
                player['pick'] = int(input("Enter 1 for Odd or 2 for Even: "))
                if player['pick'] not in [1, 2]:
                    print("Invalid input. Please enter 1 for Odd or 2 for Even.")
                    continue
                player['pick'] = 'Odd' if player['pick'] == 1 else 'Even'
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        players.append(player)

        another_player = input("Add another player? (y/n) ")
        if another_player.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if another_player.lower() != 'y':
            break

    while True:
        try:
            result = int(input("Lottery number? Enter 1 for Odd or 2 for Even: "))
            if result not in [1, 2]:
                print("Invalid input. Please enter 1 for Odd or 2 for Even.")
                continue
            result = 'Odd' if result == 1 else 'Even'
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    total_payout = 0

    for player in players:
        if result == player['pick']:
            player['payout'] = player['betsize'] * 2
            player['result'] = "Won"
            total_payout += player['payout']
        else:
            player['payout'] = 0
            player['result'] = "Lost"

    print("\nTzino Casino Winners:")
    for player in players:
        if player['result'] == "Won":
            player['payout'] -= player['payout'] * 0.1
            print("\n", player['name'], "Payout:", player['payout'], player['leap'])

if __name__ == '__main__':
    print("Tzino Payout Calculator v0.1")
    round_num = 1
    while True:
        print("\nRound", round_num)
        start_game(round_num)
        round_num += 1
        reset = input("\nReset and start from the beginning? (y/n) ")
        if reset.lower() not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if reset.lower() != 'y':
            break