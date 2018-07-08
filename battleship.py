import random
from battleship_boards import Board


class Game:
    def __init__(self):
        self.computer_board = Board()
        self.user_board = Board()
        self.battleships_size = [5, 4, 3, 2, 2, 1, 1]
        self.allocate_computer_battleships()
        self.allocate_user_battleships()
        self.win = False
        self.optional_guesses = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'E': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'F': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'G': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'H': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'I': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                 'J': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        # self.waiting_list = []
        # self.computer_guessed_row = ''
        # self.computer_guessed_column = 0

    def allocate_computer_battleships(self):
        for battleship_size in self.battleships_size:
            result = False
            while not result:
                row = random.randint(0, 9)
                column = random.randint(0, 9)
                direction = random.choice(['vertical', 'horizontal'])
                result = self.computer_board.place_battleship(battleship_size, row, column, direction)

    def allocate_user_battleships(self):
        print("******* Locate you battleships *******")
        for battleship_size in self.battleships_size:
            result = False
            while not result:
                self.user_board.print_user_board()
                row = ''
                while row == '' or row not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                    row = input('Enter row: ').upper()
                    if row not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                        print("Please make sure to use letter between A to J")
                rows = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
                row_name = rows[row]

                column = 11
                while column > 10:
                    try:
                        column = int(input('Guess column: '))
                        if column > 10 or column < 1:
                            print("Please make sure to use a digit between 1 to 10")
                            column = 11
                    except ValueError:
                        print("Please make sure to enter a digit!")
                        column = 11
                columns = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9}
                column_name = columns[column]

                instruction = ''
                while instruction == '' or instruction not in ['H', 'V']:
                    instruction = input('Enter direction v (vertical) or h (horizontal): ').upper()
                    if instruction not in ['H', 'V']:
                        print("Please make sure to use only the letters v or h")
                    if instruction == 'H':
                        direction = 'horizontal'
                    elif instruction == 'V':
                        direction = 'vertical'
                result = self.user_board.place_battleship(battleship_size, row_name, column_name, direction)
                if not result:
                    print('This battleship cannot be placed here, try a different location')

    def play_game(self):
        print("******* Start guessing *******")
        while not self.win:
            self.computer_board.print_computer_board()
            self.user_turn()
            if not self.win:
                self.computer_turn()
                self.user_board.print_user_board()

    def user_turn(self):
        turn_ended = False
        while not turn_ended:
            guess_row = ''
            while guess_row == '' or guess_row not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                guess_row = input('Guess row: ').upper()
                if guess_row not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                    print("Please make sure to use letter between A to J")
            guess_column = 11
            while guess_column > 10:
                try:
                    guess_column = int(input('Guess column: '))
                    if guess_column > 10 or guess_column < 1:
                        print("Please make sure to use a digit between 1 to 10")
                        guess_column = 11
                except ValueError:
                    print("Please make sure to enter a digit!")
                    guess_column = 11
            guess_result = self.computer_board.guess(guess_row, guess_column)
            if guess_result == 1:
                print('You already took that shot')
            elif guess_result == 2:
                print('You missed')
                turn_ended = True
            elif guess_result == 3:
                print('You hit')
                self.computer_board.print_computer_board()
            elif guess_result == 4:
                print('You sunk my battleship!')
                self.computer_board.print_computer_board()
            elif guess_result == 5:
                turn_ended = True
                self.win = True

    def computer_turn(self):
        turn_ended = False
        while not turn_ended:
            print(self.optional_guesses)  # to delete
            guess_row = random.choice(list(self.optional_guesses.keys()))
            guess_column = random.choice(self.optional_guesses[guess_row])
            guess_result = self.user_board.guess(guess_row, guess_column)
            if guess_result == 1:  # You already took that shot
                pass
            if guess_result == 2:  # missed
                self.optional_guesses[guess_row].remove(guess_column)
                if len(self.optional_guesses[guess_row]) == 0:
                    del self.optional_guesses[guess_row]
                turn_ended = True
            elif guess_result == 3:  # hit
                self.optional_guesses[guess_row].remove(guess_column)
                if len(self.optional_guesses[guess_row]) == 0:
                    del self.optional_guesses[guess_row]
                # self.computer_guessed_row = guess_row
                # self.computer_guessed_column = guess_column
            elif guess_result == 4:  # sunk battleship
                self.optional_guesses[guess_row].remove(guess_column)
                if len(self.optional_guesses[guess_row]) == 0:
                    del self.optional_guesses[guess_row]
            elif guess_result == 5:
                turn_ended = True
                self.win = True


if __name__ == '__main__':
    game = Game()
    game.play_game()
