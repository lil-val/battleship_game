import random


class Board:
    def __init__(self):
        self.board = []
        for i in range(10):
            row = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            self.board.append(row)
        self.sunk_battleship_counter = 0

    def print_board(self):
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
                    display_row.append('O')
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
                self.sunk_battleship_counter += 1
        if self.sunk_battleship_counter == 7:
            print('Victory!!!')
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


class Game:
    def __init__(self):
        self.board = Board()
        battleships_size = [5, 4, 3, 2, 2, 1, 1]
        for battleship_size in battleships_size:
            result = False
            while not result:
                row = random.randint(0, 9)
                column = random.randint(0, 9)
                direction = random.choice(['vertical', 'horizontal'])
                result = self.board.place_battleship(battleship_size, row, column, direction)

    def play_game(self):
        win = False
        while not win:
            self.board.print_board()
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
            if self.board.guess(guess_row, guess_column):
                win = True


if __name__ == '__main__':
    game = Game()
    game.play_game()
