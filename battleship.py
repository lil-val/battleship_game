import random
# import csv
# from datetime import datetime
from battleship_boards import Board


class Game:
    def __init__(self):
        self.computer_board = Board()
        self.user_board = Board()
        self.battleships_size = [5, 4, 3, 2, 2, 1, 1]
        self.allocate_computer_battleships()
        self.allocate_user_battleships()
        # self.rounds = 0
        # self.name = input('Enter you name: ')
        # self.high_scores = []

    def allocate_computer_battleships(self):
        for battleship_size in self.battleships_size:
            result = False
            while not result:
                row = random.randint(0, 9)
                column = random.randint(0, 9)
                direction = random.choice(['vertical', 'horizontal'])
                result = self.computer_board.place_battleship(battleship_size, row, column, direction)

    def allocate_user_battleships(self):
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

    def play_game(self):
        win = False
        while not win:
            self.computer_board.print_board()
            self.user_board.print_user_board()
            # self.user_board.print_board()
            # self.rounds += 1
            # print('Round number {}'.format(self.rounds))
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
            if self.computer_board.guess(guess_row, guess_column):
                win = True
        # self.is_high_score(self.rounds)

    # def create_high_scores_file(self, sorted_high_scores):
    #     with open('high_scores.csv', 'w', newline='') as high_scores_file:
    #         writer = csv.DictWriter(high_scores_file, fieldnames=['name', 'score', 'timestamp'], dialect='excel')
    #         writer.writeheader()
    #         for sorted_high_score in sorted_high_scores:
    #             writer.writerow(
    #                 {'name': sorted_high_score['name'], 'score': sorted_high_score['score'],
    #                  'timestamp': sorted_high_score['timestamp']})

    # def get_high_scores(self, file_name='high_scores.csv'):
    #     try:
    #         with open(file_name, 'r', newline='') as high_scores_file:
    #             next(high_scores_file)
    #             reader = csv.DictReader(high_scores_file, fieldnames=['name', 'score', 'timestamp'], dialect='excel')
    #             for line in reader:
    #                 self.high_scores.append(line)
    #     except IOError:
    #         pass

    # def is_high_score(self, rounds):
    #     self.get_high_scores()
    #     if len(self.high_scores) < 3:
    #         self.high_scores.append({'name': self.name, 'score': rounds,
    #                                  'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    #     else:
    #         for score in self.high_scores:
    #             if rounds < int(score['score']):
    #                 self.high_scores.append(
    #                     {'name': self.name, 'score': rounds, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    #                 break
    #     sorted_scores = sorted(self.high_scores, key=lambda k: int(k['score']))
    #     for high_score in sorted_scores[:3]:
    #         print('***Name: {} *** Score: {} ***'.format(high_score['name'], high_score['score']))
    #     self.create_high_scores_file(sorted_scores[:3])


if __name__ == '__main__':
    game = Game()
    game.play_game()
