import random


class RouletteWheel:
    def __init__(self):
        self.pockets = list(range(37))
        self.colors = {
            0: 'green',
            1: 'red',
            2: 'black',
            3: 'red',
            4: 'black',
            5: 'red',
            6: 'black',
            7: 'red',
            8: 'black',
            9: 'red',
            10: 'black',
            11: 'black',
            12: 'red',
            13: 'black',
            14: 'red',
            15: 'black',
            16: 'red',
            17: 'black',
            18: 'red',
            19: 'red',
            20: 'black',
            21: 'red',
            22: 'black',
            23: 'red',
            24: 'black',
            25: 'red',
            26: 'black',
            27: 'red',
            28: 'black',
            29: 'black',
            30: 'red',
            31: 'black',
            32: 'red',
            33: 'black',
            34: 'red',
            35: 'black',
            36: 'red'
        }

    def spin(self):
        return random.choice(self.pockets)


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bets = []

    def place_bet(self, bet_amount, bet_type, bet_value):
        self.bets.append(Bet(bet_amount, bet_type, bet_value))


class Bet:
    def __init__(self, amount, bet_type, value):
        self.amount = amount
        self.bet_type = bet_type
        self.value = value


class Game:
    def __init__(self):
        self.wheel = RouletteWheel()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def play_round(self):
        winning_number = self.wheel.spin()
        print(f"The winning number is {winning_number}")

        for player in self.players:
            for bet in player.bets:
                if bet.bet_type == 'number' and bet.value == winning_number:
                    player.balance += bet.amount * 36
                elif bet.bet_type == 'color' and self.wheel.colors[winning_number] == bet.value:
                    player.balance += bet.amount * 2
                elif bet.bet_type == 'even' and winning_number % 2 == 0 and winning_number <= 18:
                    player.balance += bet.amount * 2
                elif bet.bet_type == 'odd' and winning_number % 2 != 0 and winning_number > 18:
                    player.balance += bet.amount * 2
                else:
                    player.balance -= bet.amount

    def print_player_balances(self):
        for player in self.players:
            print(f"{player.name}'s balance: {player.balance}")


if __name__ == "__main__":
    game = Game()
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        player_name = input(f"Enter the name of player {i + 1}: ")
        player_balance = int(
            input(f"Enter the starting balance for {player_name}: "))

        player = Player(player_name, player_balance)
        game.add_player(player)

        print(f"Available bet types: 'number' (press 1) or 'color' (press 2) or 'even' (press 3)or 'odd' (press 4)")
        bet_type_choice = input(
            f"Choose a bet type for {player_name}: ")

        if bet_type_choice == '1':
            bet_type = 'number'
            bet_value = input(f"Enter the bet value for {player_name}: ")
        elif bet_type_choice == '2':
            bet_type = 'color'
            bet_value = input(
                f"Which color will you choose? {player_name} (Red or Black) : ")
        elif bet_type_choice == '3':
            bet_type = 'even'

        elif bet_type_choice == '4':
            bet_type = 'odd'

        player.place_bet(player_balance, bet_type, bet_value)

    game.play_round()
    game.print_player_balances()
