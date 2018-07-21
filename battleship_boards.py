from battleship import Battleship


class Board:
    """
    Represent the board.
    Contains data of battleships locations, hits and misses.
    Enables battleships placing and guessing.
    """
    def __init__(self):
        """Create an empty board"""
        self.board = [['O' for col in range(10)] for row in range(10)]
        self.battleships = []

    def find_battleship(self, row, column):
        """
        checks if a battleship is located at the given position and returns its status
        :param row: int from 0 to 9 which represent the row to check
        :param column: int from 0 to 9 which represent the column to check
        :return: 'Z' in case a battleship is located at the given position, 'X' in case a battleship is located at
        the given position and was already hit, 'O' in case a battleship is not located at the given position
        """
        position = str(row) + str(column)
        for battleship in self.battleships:
            battleship_status = battleship.contains(position)
            if battleship_status != 'O':
                return battleship_status
        return 'O'

    def print_board(self, user):
        """
        Prints to console the current status of the game board.
        :param user: boolean, True = user board (battleships displayed) and False = computer board (battleships hidden)
        """
        if user:
            print('User Board')
        else:
            print('Computer Board')
        header = []
        for column_name in range(11):
            header.append(str(column_name))
        print(' '.join(header))
        row_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for row_number in range(10):
            row = self.board[row_number]
            display_row = []
            for column_number in range(10):
                if row[column_number] == '-':
                    display_row.append('-')
                elif self.find_battleship(row_number, column_number) == 'Z' and not user:
                    display_row.append('O')
                else:
                    display_row.append(self.find_battleship(row_number, column_number))
            print(row_name[row_number] + ' ' + ' '.join(display_row))

    def place_battleship(self, battleship_size, row, column, direction):
        """
        Check if battleship can be placed in the given position and place it if possible.
        :param battleship_size: int which represent the battleship size
        :param row: int from 0 to 9 which represent the row to place the battleship
        :param column: int from 0 to 9 which represent the column to place the battleship
        :param direction: str 'vertical' or 'horizontal' which represent the required direction
        :return: True if battleship was placed or False if not
        """
        if direction == 'vertical':
            current_row = row
            for i in range(battleship_size):
                if current_row < 10 and self.find_battleship(current_row, column) == 'O' \
                        and (column == 0 or self.find_battleship(current_row, column - 1) == 'O')\
                        and (column == 9 or self.find_battleship(current_row, column + 1) == 'O')\
                        and (current_row == 0 or self.find_battleship(current_row - 1, column) == 'O') \
                        and (current_row == 0 or column == 0 or self.find_battleship(current_row - 1, column - 1) == 'O') \
                        and (current_row == 0 or column == 9 or self.find_battleship(current_row - 1, column + 1) == 'O') \
                        and (current_row == 9 or self.find_battleship(current_row + 1, column) == 'O') \
                        and (current_row == 9 or column == 0 or self.find_battleship(current_row + 1, column - 1) == 'O') \
                        and (current_row == 9 or column == 9 or self.find_battleship(current_row + 1, column + 1) == 'O'):
                    current_row += 1
                else:
                    return False
            positions = []
            for i in range(battleship_size):
                positions.append(str(row) + str(column))
                row += 1
            self.battleships.append(Battleship(positions))
            return True
        if direction == 'horizontal':
            current_column = column
            for i in range(battleship_size):
                if current_column < 10 and self.find_battleship(row, current_column) == 'O' \
                        and (row == 0 or self.find_battleship(row - 1, current_column) == 'O') \
                        and (row == 9 or self.find_battleship(row + 1, current_column) == 'O') \
                        and (current_column == 0 or self.find_battleship(row, current_column - 1) == 'O') \
                        and (current_column == 0 or row == 0 or self.find_battleship(row - 1, current_column - 1) == 'O') \
                        and (current_column == 0 or row == 9 or self.find_battleship(row + 1, current_column - 1) == 'O') \
                        and (current_column == 9 or self.find_battleship(row, current_column + 1) == 'O') \
                        and (current_column == 9 or row == 0 or self.find_battleship(row - 1, current_column + 1) == 'O') \
                        and (current_column == 9 or row == 9 or self.find_battleship(row + 1, current_column + 1) == 'O'):
                    current_column += 1
                else:
                    return False
            positions = []
            for i in range(battleship_size):
                positions.append(str(row) + str(column))
                column += 1
            self.battleships.append(Battleship(positions))
            return True

    def guess(self, row, column):
        """
        Check the received input from user or computer against the board
        :param row: str which present the row to check if battleship is placed
        :param column: int which present the column to check if battleship is placed
        :return: 1 - already guessed this position, 2 - miss, 3 - hit, 4 - battleship sunk
        """
        row_name = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        column_name = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9}
        position = str(row_name[row]) + str(column_name[column])
        if self.board[row_name[row]][column_name[column]] == '-' or \
                self.find_battleship(row_name[row], column_name[column]) == 'X':
            return 1
        for battleship in self.battleships:
            hit_result = battleship.hit(position)
            if hit_result:
                if battleship.is_sunk:
                    return 4
                else:
                    return 3
        self.board[row_name[row]][column_name[column]] = '-'
        return 2
