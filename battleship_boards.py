class Board:
    def __init__(self):
        self.board = []
        for i in range(10):
            row = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            self.board.append(row)
        self.sunk_battleship_by_user_counter = 0
        self.sunk_battleship_by_computer_counter = 0

    def print_board(self):
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
                if element == 'Z':
                    display_row.append('Z')  # at the end change back to 'O'
                else:
                    display_row.append(element)
            print(row_name[i] + ' ' + ' '.join(display_row))

    def print_user_board(self):
        print('User Board')
        header = []
        for i in range(11):
            header.append(str(i))
        print(' '.join(header))
        row_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for i in range(10):
            row = self.board[i]
            display_row = []
            for element in row:
                if element == 'Z':
                    display_row.append('Z')
                else:
                    display_row.append(element)
            print(row_name[i] + ' ' + ' '.join(display_row))

    def place_battleship(self, battleship_size, row, column, direction):
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
        row_name = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        column_name = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9}
        if self.board[row_name[row]][column_name[column]] == '-' or \
                self.board[row_name[row]][column_name[column]] == 'X':
            print('You already took that shot')
        elif self.board[row_name[row]][column_name[column]] == 'O':
            print('You missed')
            self.board[row_name[row]][column_name[column]] = '-'
        elif self.board[row_name[row]][column_name[column]] == 'Z':
            print('You hit')
            self.board[row_name[row]][column_name[column]] = 'X'
            up = self.check_up(row_name[row], column_name[column])
            down = self.check_down(row_name[row], column_name[column])
            left = self.check_left(row_name[row], column_name[column])
            right = self.check_right(row_name[row], column_name[column])
            if up and down and left and right:
                print('You sunk my battleship!')
                self.sunk_battleship_by_user_counter += 1
        if self.sunk_battleship_by_user_counter == 7:
            print('You win!!!')
            self.print_board()
            print('GAME OVER')
            return True
        elif self.sunk_battleship_by_computer_counter == 7:  # adding computer counter
            print('Computer wins!!!')
            self.print_board()
            print('GAME OVER')
            return True

    def check_up(self, row, column):
        if row == 0 or self.board[row - 1][column] == 'O' or self.board[row - 1][column] == '-':
            return True
        elif self.board[row - 1][column] == 'Z':
            return False
        elif self.board[row - 1][column] == 'X':
            return self.check_up(row - 1, column)

    def check_down(self, row, column):
        if row == 9 or self.board[row + 1][column] == 'O' or self.board[row + 1][column] == '-':
            return True
        elif self.board[row + 1][column] == 'Z':
            return False
        elif self.board[row + 1][column] == 'X':
            return self.check_down(row + 1, column)

    def check_left(self, row, column):
        if column == 0 or self.board[row][column - 1] == 'O' or self.board[row][column - 1] == '-':
            return True
        elif self.board[row][column - 1] == 'Z':
            return False
        elif self.board[row][column - 1] == 'X':
            return self.check_left(row, column - 1)

    def check_right(self, row, column):
        if column == 9 or self.board[row][column + 1] == 'O' or self.board[row][column + 1] == '-':
            return True
        elif self.board[row][column + 1] == 'Z':
            return False
        elif self.board[row][column + 1] == 'X':
            return self.check_right(row, column + 1)
