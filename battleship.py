import random


class Board:
    def __init__(self):
        self.board = []
        # for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        for i in range(10):
            row = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
            self.board.append(row)

    def print_board(self):
        header = []
        for i in range(11):
            header.append(str(i))
        print(' '.join(header))
        for row in self.board:
            print(' '.join(row))

    def place_battleship(self, battleship_size, row, column, direction):
        if direction == 'vertical':
            current_row = row
            for i in range(battleship_size):
                if i == 0:
                    if self.board[current_row][column] == 'O' \
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
                elif i == battleship_size - 1:
                    if current_row < 10 and self.board[current_row][column] == 'O' \
                            and (column == 0 or self.board[current_row][column - 1] == 'O')\
                            and (column == 9 or self.board[current_row][column + 1] == 'O') \
                            and (current_row == 9 or self.board[current_row + 1][column] == 'O') \
                            and (current_row == 9 or column == 0 or self.board[current_row + 1][column - 1] == 'O') \
                            and (current_row == 9 or column == 9 or self.board[current_row + 1][column + 1] == 'O'):
                        current_row += 1
                    else:
                        return False
                else:
                    if current_row < 10 and self.board[current_row][column] == 'O' \
                            and (column == 0 or self.board[current_row][column - 1] == 'O') \
                            and (column == 9 or self.board[current_row][column + 1] == 'O'):
                        current_row += 1
                    else:
                        return False
            for i in range(battleship_size):
                self.board[row][column] = 'X'
                row += 1
            return True
        if direction == 'horizontal':
            pass  # add for horizontal



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
        self.board.print_board()


# if __name__ == '__main__':
#     print(Board)


game = Game()
# board = Board()
