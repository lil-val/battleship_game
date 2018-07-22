import unittest
from battleship import Battleship


class TestBattleship(unittest.TestCase):

    def setUp(self):
        self.battleship = Battleship(['00', '01', '02', '03'])

    def test_contains_Z_before(self):
        self.assertEqual(self.battleship.contains('00'), 'Z')

    def test_contains_X_after(self):
        self.battleship.hit('00')
        self.assertEqual(self.battleship.contains('00'), 'X')

    def test_contains_O_before(self):
        self.assertEqual(self.battleship.contains('04'), 'O')

    def test_contains_O_after(self):
        self.battleship.hit('04')
        self.assertEqual(self.battleship.contains('04'), 'O')

    def test_hit_if_miss(self):
        self.assertFalse(self.battleship.hit('07'))

    def test_hit_if_hit(self):
        self.assertTrue(self.battleship.hit('01'))

    def test_hit_twice(self):
        self.battleship.hit('01')
        self.assertFalse(self.battleship.hit('01'))

    def test_hit_if_not_sunk(self):
        self.battleship.hit('01')
        self.assertFalse(self.battleship.is_sunk)

    def test_hit_if_sunk(self):
        self.battleship.hit('01')
        self.battleship.hit('03')
        self.battleship.hit('02')
        self.battleship.hit('00')
        self.assertEqual(self.battleship.is_sunk, True)


if __name__ == '__main__':
    unittest.main()
