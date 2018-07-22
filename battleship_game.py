import random
from battleship_boards import Board

row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


class Game:
    """
    Manages and represents the battleship game.
    Receive instructions from the user and computer and execute at the boards.
    """
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
        self.waiting_list = []
        self.current_battleship = []
        self.sunk_battleship_by_user_counter = 0
        self.sunk_battleship_by_computer_counter = 0

    def allocate_computer_battleships(self):
        """
        Random allocation of battleships by computer.
        Each allocation is checked to verify if it contains the required free space before placing the battleship.
        """
        for battleship_size in self.battleships_size:
            result = False
            while not result:
                row = chr(random.randint(ord('A'), ord('J')))
                column = random.randint(1, 10)
                direction = random.choice(['vertical', 'horizontal'])
                result = self.computer_board.place_battleship(battleship_size, row, column, direction)

    def allocate_user_battleships(self):
        """
        Allocation of battleships by user.
        The user provides row, column and direction in order to allocate a battleships.
        Each allocation is checked to verify if it contains the required free space before placing the battleship.
        """
        print("******* Locate you battleships *******")
        for battleship_size in self.battleships_size:
            print('Select position for {} size battleship'.format(battleship_size))
            result = False
            while not result:
                self.user_board.print_board(True)
                row = ''
                while row == '' or row not in row_letters:
                    row = input('Enter row: ').upper()
                    if row not in row_letters:
                        print("Please make sure to use letter between A to J")

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

                instruction = ''
                while instruction == '' or instruction not in ['H', 'V']:
                    instruction = input('Enter direction v (vertical) or h (horizontal): ').upper()
                    if instruction not in ['H', 'V']:
                        print("Please make sure to use only the letters v or h")
                    if instruction == 'H':
                        direction = 'horizontal'
                    elif instruction == 'V':
                        direction = 'vertical'
                result = self.user_board.place_battleship(battleship_size, row, column, direction)
                if not result:
                    print('This battleship cannot be placed here, try a different location')

    def play_game(self):
        print("******* Start guessing *******")
        while not self.win:
            self.computer_board.print_board(False)
            self.user_turn()
            if not self.win:
                self.computer_turn()
                if not self.win:
                    self.user_board.print_board(True)

    def user_turn(self):
        """
        User tries to hit computer battleships by guessing row and column.
        Checks if user wins and if the user turn has ended.
        """
        turn_ended = False
        while not turn_ended:
            guess_row = ''
            while guess_row == '' or guess_row not in row_letters:
                guess_row = input('Guess row: ').upper()
                if guess_row not in row_letters:
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
                self.computer_board.print_board(False)
            elif guess_result == 4:
                self.sunk_battleship_by_user_counter += 1
                if self.sunk_battleship_by_user_counter == 7:
                    self.computer_board.print_board(False)
                    self.you_win()
                    turn_ended = True
                    self.win = True
                else:
                    print('You sunk my battleship!')
                    self.computer_board.print_board(False)

    def computer_turn(self):
        """
        Computer tries to hit user battleships by randomly guessing row and column.
        If a 'hit' was observed the next guess will be selected from pre-defined list of adjacent allocations.
        Updates dictionary of optional row and column for next guess.
        Checks if computer wins and if the computer turn has ended.
        """
        turn_ended = False
        while not turn_ended:
            guess_direction = 'N'
            if len(self.waiting_list) == 0:
                guess_row = random.choice(list(self.optional_guesses.keys()))
                guess_column = random.choice(self.optional_guesses[guess_row])
            else:
                guess_row = self.waiting_list[0][0]
                guess_column = self.waiting_list[0][1]
                guess_direction = self.waiting_list[0][2]
                del self.waiting_list[0]
            guess_result = self.user_board.guess(guess_row, guess_column)
            self.optional_guesses[guess_row].remove(guess_column)
            if len(self.optional_guesses[guess_row]) == 0:
                del self.optional_guesses[guess_row]
            if guess_result == 1:  # computer already took that shot
                continue
            elif guess_result == 2:  # computer missed
                turn_ended = True
            elif guess_result == 3:  # computer hit
                self.current_battleship.append([guess_row, guess_column])
                if guess_row in self.optional_guesses and (guess_column - 1) in self.optional_guesses[guess_row]:
                    if guess_column != 1 and guess_direction != 'V':
                        self.waiting_list.append([guess_row, guess_column - 1, 'H'])
                if guess_row in self.optional_guesses and (guess_column + 1) in self.optional_guesses[guess_row]:
                    if guess_column != 10 and guess_direction != 'V':
                        self.waiting_list.append([guess_row, guess_column + 1, 'H'])
                if chr(ord(guess_row) - 1) in self.optional_guesses and \
                        guess_column in self.optional_guesses[chr(ord(guess_row) - 1)]:
                    if guess_row != 'A' and guess_direction != 'H':
                        self.waiting_list.append([chr(ord(guess_row) - 1), guess_column, 'V'])
                if chr(ord(guess_row) + 1) in self.optional_guesses and \
                        guess_column in self.optional_guesses[chr(ord(guess_row) + 1)]:
                    if guess_row != 'J' and guess_direction != 'H':
                        self.waiting_list.append([chr(ord(guess_row) + 1), guess_column, 'V'])
            elif guess_result == 4:  # computer sunk battleship
                self.current_battleship.append([guess_row, guess_column])
                self.sunk_battleship_by_computer_counter += 1
                if self.sunk_battleship_by_computer_counter == 7:
                    self.user_board.print_board(True)
                    self.computer_win()
                    turn_ended = True
                    self.win = True
                else:
                    self.waiting_list = []
                    for position in self.current_battleship:
                        self.surrounding_waters(position[0], position[1])
                    self.current_battleship = []

    def surrounding_waters(self, row, column):
        """
        After computer sunk a user battleship, omit all surrounding positions from the dictionary
        of optional row and column for next computer guesses.
        :param row: str which represents the row in which the battleship is placed
        :param column: int which represent the column in which the battleship is placed
        """
        rows_to_check = [chr(ord(row) - 1), chr(ord(row)), chr(ord(row) + 1)]
        for row_to_check in rows_to_check:
            if row_to_check in self.optional_guesses:
                if (column - 1) in self.optional_guesses[row_to_check]:
                    self.optional_guesses[row_to_check].remove(column - 1)
                if column in self.optional_guesses[row_to_check]:
                    self.optional_guesses[row_to_check].remove(column)
                if (column + 1) in self.optional_guesses[row_to_check]:
                    self.optional_guesses[row_to_check].remove(column + 1)
                if len(self.optional_guesses[row_to_check]) == 0:
                    del self.optional_guesses[row_to_check]

    def you_win(self):
        print("__     __          __          ___       _ _ _ ")
        print("\ \   / /          \ \        / (_)     | | | |")
        print(" \ \_/ /__  _   _   \ \  /\  / / _ _ __ | | | |")
        print("  \   / _ \| | | |   \ \/  \/ / | | '_ \| | | |")
        print("   | | (_) | |_| |    \  /\  /  | | | | |_|_|_|")
        print("   |_|\___/ \__,_|     \/  \/   |_|_| |_(_|_|_)")

    def computer_win(self):
        print("  _____                            _             __          ___       _ _ _ ")
        print(" / ____|                          | |            \ \        / (_)     | | | |")
        print("| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __   \ \  /\  / / _ _ __ | | | |")
        print("| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|   \ \/  \/ / | | '_ \| | | |")
        print("| |___| (_) | | | | | | |_) | |_| | ||  __/ |       \  /\  /  | | | | |_|_|_|")
        print(" \_____\___/|_| |_| |_| .__/ \__,_|\__\___|_|        \/  \/   |_|_| |_(_|_|_)")
        print("                      | |                                                    ")
        print("                      |_|                                                    ")


if __name__ == '__main__':
    game = Game()
    game.play_game()
