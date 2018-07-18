class Board:
    """
    Represent the board.
    Contains data of battleships locations, hits and misses.
    Enables battleships placing and guessing.
    """
    def __init__(self):
        """Create an empty board"""
        self.board = [['O' for col in range(10)] for row in range(10)]

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
        for i in range(11):
            header.append(str(i))
        print(' '.join(header))
        row_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for i in range(10):
            row = self.board[i]
            display_row = []
            for element in row:
                if element == 'Z' and not user:
                    display_row.append('O')
                else:
                    display_row.append(element)
            print(row_name[i] + ' ' + ' '.join(display_row))

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
                if current_row < 10 and self.board[current_row][column] == 'O' \
                        and (column == 0 or self.board[current_row][column - 1] == 'O')\
                        and (column == 9 or self.board[current_row][column + 1] == 'O')\
                        and (current_row == 0 or self.board[current_row - 1][column] == 'O') \
                        and (current_row == 0 or column == 0 or self.board[current_row - 1][column - 1] == 'O') \
                        and (current_row == 0 or column == 9 or self.board[current_row - 1][column + 1] == 'O') \
                        and (current_row == 9 or self.board[current_row + 1][column] == 'O') \
                        and (current_row == 9 or column == 0 or self.board[current_row + 1][column - 1] == 'O') \
                        and (current_row == 9 or column == 9 or self.board[current_row + 1][column + 1] == 'O'):
                    current_row += 1
                else:
                    return False
            for i in range(battleship_size):
                self.board[row][column] = 'Z'
                row += 1
            return True
        if direction == 'horizontal':
            current_column = column
            for i in range(battleship_size):
                if current_column < 10 and self.board[row][current_column] == 'O' \
                        and (row == 0 or self.board[row - 1][current_column] == 'O') \
                        and (row == 9 or self.board[row + 1][current_column] == 'O') \
                        and (current_column == 0 or self.board[row][current_column - 1] == 'O') \
                        and (current_column == 0 or row == 0 or self.board[row - 1][current_column - 1] == 'O') \
                        and (current_column == 0 or row == 9 or self.board[row + 1][current_column - 1] == 'O') \
                        and (current_column == 9 or self.board[row][current_column + 1] == 'O') \
                        and (current_column == 9 or row == 0 or self.board[row - 1][current_column + 1] == 'O') \
                        and (current_column == 9 or row == 9 or self.board[row + 1][current_column + 1] == 'O'):
                    current_column += 1
                else:
                    return False
            for i in range(battleship_size):
                self.board[row][column] = 'Z'
                column += 1
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
        if self.board[row_name[row]][column_name[column]] == '-' or \
                self.board[row_name[row]][column_name[column]] == 'X':
            return 1
        elif self.board[row_name[row]][column_name[column]] == 'O':
            self.board[row_name[row]][column_name[column]] = '-'
            return 2
        elif self.board[row_name[row]][column_name[column]] == 'Z':
            self.board[row_name[row]][column_name[column]] = 'X'

            up = self.is_sunk_battleship(row_name[row], column_name[column], -1, 0)
            down = self.is_sunk_battleship(row_name[row], column_name[column], 1, 0)
            left = self.is_sunk_battleship(row_name[row], column_name[column], 0, -1)
            right = self.is_sunk_battleship(row_name[row], column_name[column], 0, 1)
            if up and down and left and right:
                return 4
            return 3

    def is_sunk_battleship(self, row, column, row_shift, column_shift):
        """
        Check if the whole battleship was hit by user or computer
        :param row: int from 0 to 9 which represent the row to place the battleship
        :param column: int from 0 to 9 which represent the column to place the battleship
        :param row_shift: int 0 / 1 / -1 - shift of row to be checked
        :param column_shift: int 0 / 1 / -1 - shift of column to be checked
        :return: True if yes, False if not
        """
        if (row_shift == -1 and column_shift == 0 and row == 0) \
                or (row_shift == 1 and column_shift == 0 and row == 9) \
                or (row_shift == 0 and column_shift == -1 and column == 0) \
                or (row_shift == 0 and column_shift == 1 and column == 9):
            return True  # edge of board
        elif self.board[row + row_shift][column + column_shift] == 'O' \
                or self.board[row + row_shift][column + column_shift] == '-':
            return True
        elif self.board[row + row_shift][column + column_shift] == 'Z':
            return False
        elif self.board[row + row_shift][column + column_shift] == 'X':
            return self.is_sunk_battleship((row + row_shift), (column + column_shift), row_shift, column_shift)
