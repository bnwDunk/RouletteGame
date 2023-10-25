import random
import os
from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich.panel import Panel


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
        number = random.choice(self.pockets)
        color = self.colors[number]
        return number, color


class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bets = []

    def place_bet(self, bet_amount, bet_type, bet_value):
        if self.balance >= bet_amount:
            self.bets.append(Bet(bet_amount, bet_type, bet_value))
            self.balance -= bet_amount
        else:
            print(f"Insufficient balance for {self.name} to place a bet.")
            
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
        winning_number, winning_color = self.wheel.spin()
        wining_spin_text = Text(
            f"The winning number is {winning_number} and its color is {winning_color}")
        wining_spin_text.stylize("bold blue")
        player_panel = Panel(wining_spin_text, title="Winning number",
                             style="on bright_white", border_style="black", width=80)
        console.print(player_panel, justify="center")

        for player in self.players:
            for bet in player.bets:
                if bet.bet_type == 'number' and bet.value == winning_number:
                    player.balance += bet.amount * 10
                elif bet.bet_type == 'color' and self.wheel.colors[winning_number] == bet.value:
                    player.balance += bet.amount * 2
                elif bet.bet_type == 'even' and winning_number % 2 == 0 and winning_number <= 18:
                    player.balance += bet.amount * 4
                elif bet.bet_type == 'odd' and winning_number % 2 != 0 and winning_number > 18:
                    player.balance += bet.amount * 4
                else:
                    player.balance - bet.amount 

    def print_player_balances(self):
        for player in self.players:
            text_player_balances = Text(
                f"{player.name}'s balance: {player.balance}")
            text_player_balances.stylize("bold blue")
            text_box = Panel(text_player_balances, title="Player Balances",
                             style="on bright_white", border_style="black", width=80)
            console.print(text_box, justify="center")


if __name__ == "__main__":

    def clear_screen():
        os.system('clear')

    clear_screen()
    game = Game()
    console = Console()
    roulette_wheel = RouletteWheel()
    colors = roulette_wheel.colors

    text = Text("Welcome to Roulette Game \n This game will change your life.")
    text.stylize("bold blue")
    text_box = Panel(text, title="Roulette Game",
                     style="on bright_white", border_style="black", width=80)
    console.print(text_box, justify="center")

    input("Press enter to play game")

    clear_screen()

    text = Text("Add player and Balance")
    text.stylize("bold blue")
    text_box = Panel(text, title="Roulette Game",
                     style="on bright_white", border_style="black", width=80)
    console.print(text_box, justify="center")

    num_players = int(input("Enter the number of players: "))

    for i in range(num_players):
        player_name = input(f"Enter the name of player {i + 1}: ")
        player_balance = int(
            input(f"Enter the starting balance for {player_name}: "))

        player_info = Text(
            f"Player {i + 1}: {player_name} (Balance: {player_balance})")
        player_info.stylize("bold blue")
        player_panel = Panel(player_info, title="Player info",
                             style="on bright_white", border_style="black", width=80)
        console.print(player_panel, justify="center")

        player = Player(player_name, player_balance)
        game.add_player(player)

        input("Press enter to play game")
        clear_screen()

        main_table = Table(show_header=False, expand=True)
        main_table.add_column("Col1", justify="center")
        main_table.add_column("Col2", justify="center")
        main_table.add_column("Col3", justify="center")

        zero_table = Table(show_header=False, expand=True)
        zero_table.add_column("Col1", justify="center")

        bet_table = Table(show_header=True, expand=True)
        bet_table.add_column("EVEN", justify="center")
        bet_table.add_column("NUMBER", justify="center")
        bet_table.add_column("ODD", justify="center")

        zero_table.add_row(f"{0} ({colors[0]})", style="green")

        data = [
            [f"{i} ({colors[i]})", f"{i + 1} ({colors[i + 1]})",
             f"{i + 2} ({colors[i + 2]})"]
            for i in range(1, 36, 3)
        ]

        for row in data:
            formatted_row = []
            for cell in row:
                cell_text = Text(cell)
                if "(red)" in cell.lower():
                    cell_text.stylize("bold red on default")
                elif "(black)" in cell.lower():
                    cell_text.stylize("bold white on black")
                formatted_row.append(cell_text)
            main_table.add_row(*formatted_row)

        bet_table.add_row("1 to 18", "Red or Black", "19 to 36")

        console.print(zero_table)
        console.print(main_table)
        console.print(bet_table)

        text = Text(
            "'number x 10' (press 1) \n 'color x 2' (press 2) \n 'even x 4' (press 3) \n 'odd x 4' (press 4)")
        text.stylize("bold blue")
        text_box = Panel(text, title="Available bet types",
                         style="on bright_white", border_style="black", width=80)
        console.print(text_box, justify="center")

        player_info = Text(
            f"Player {i + 1}: {player_name} (Balance: {player_balance})")
        player_info.stylize("bold blue")
        player_panel = Panel(player_info, title="Player info",
                             style="on bright_white", border_style="black", width=80)
        console.print(player_panel, justify="center")

        bet_type_choice = input(
            f"Choose a bet type for {player_name}: ")

        if bet_type_choice == '1':
            bet_type = 'number'
            bet_value = input(f"What number to choose? {player_name}: ")
            bet_amount = int(input(f"How much to bet? {player_name}: "))
        elif bet_type_choice == '2':
            bet_type = 'color'
            bet_value = input(
                f"Which color will you choose? {player_name} (Red or Black): ")
            bet_amount = int(input(f"How much to bet? {player_name}: "))
        elif bet_type_choice == '3':
            bet_type = 'number'
            bet_value = 'even'
            print("It is an even number from 1-18")
            bet_amount = int(input(f"How much to bet? {player_name}: "))
        elif bet_type_choice == '4':
            bet_type = 'number'
            bet_value = 'odd'
            print("It is an odd number from 19-36")
            bet_amount = int(input(f"How much to bet? {player_name}: "))

        text = Text(
            f"Player {i + 1}: {player_name} (bet type: {bet_type}) (bet value: {bet_value}) (bet amount: {bet_amount})")
        text.stylize("bold blue")
        text_box = Panel(text, title="Bet Detail",
                         style="on bright_white", border_style="black", width=80)
        console.print(text_box, justify="center")

        input("Press enter to play game")
        clear_screen()
        player.place_bet(bet_amount, bet_type, bet_value)

    game.play_round()
    game.print_player_balances()
