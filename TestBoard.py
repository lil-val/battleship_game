import unittest
from battleship_boards import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.place_battleship(5, 'A', 1, 'vertical')
        self.board.place_battleship(4, 'A', 3, 'vertical')
        self.board.place_battleship(3, 'A', 5, 'vertical')

    def test_find_battleship_if_not_there(self):
        self.assertEqual(self.board.find_battleship(0, 3), 'O')

    def test_find_battleship_if_there(self):
        self.assertEqual(self.board.find_battleship(0, 0), 'Z')

    def test_find_battleship_if_there_and_already_hit(self):
        self.board.guess('A', 1)
        self.assertEqual(self.board.find_battleship(0, 0), 'X')

    def test_place_battleship_vertical_can_be_placed(self):
        self.assertTrue(self.board.place_battleship(2, 'A', 8, 'vertical'))

    def test_place_battleship_vertical_cannot_be_placed(self):
        self.assertFalse(self.board.place_battleship(2, 'A', 2, 'vertical'))

    def test_place_battleship_horizontal_can_be_placed(self):
        self.assertTrue(self.board.place_battleship(2, 'H', 6, 'horizontal'))

    def test_place_battleship_horizontal_cannot_be_placed(self):
        self.assertFalse(self.board.place_battleship(2, 'F', 2, 'horizontal'))

    def test_place_battleship_horizontal_on_edge(self):
        self.assertFalse(self.board.place_battleship(2, 'I', 10, 'horizontal'))

    def test_guess_already_guess_and_miss(self):
        self.board.guess('A', 2)
        self.assertEqual(self.board.guess('A', 2), 1)

    def test_guess_already_guess_and_hit(self):
        self.board.guess('A', 1)
        self.assertEqual(self.board.guess('A', 1), 1)

    def test_guess_and_miss(self):
        self.assertEqual(self.board.guess('A', 2), 2)

    def test_guess_and_hit(self):
        self.assertEqual(self.board.guess('A', 1), 3)

    def test_guess_and_sunk(self):
        self.board.guess('A', 1)
        self.board.guess('B', 1)
        self.board.guess('C', 1)
        self.board.guess('D', 1)
        self.assertEqual(self.board.guess('E', 1), 4)


if __name__ == '__main__':
    unittest.main()
