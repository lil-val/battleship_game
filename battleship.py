class Battleship:
    """
    Representation of a battleship, holds the battleship positions and validate sinking
    """
    def __init__(self, positions):
        """
        creates battleship instance based on positions
        :param positions: list of string containing the battleship positions e.g. ['00', '01', '02', '03']
        """
        self.positions = positions
        self.hit_positions = []
        self.is_sunk = False

    def contains(self, position):
        """
        checks if the battleship is located at that position
        :param position: a position to be checked, string of row and column e.g. '34'
        :return: 'Z' in case the battleship is located at the given position, 'X' in case the battleship is located at
        the given position and was already hit, 'O' in case the battleship is not located at the given position
        """
        if position in self.positions:
            return 'Z'
        elif position in self.hit_positions:
            return 'X'
        return 'O'

    def hit(self, position):
        """
        try to hit the battleship at the given position
        :param position: a position to be checked, string of row and column e.g. '34'
        :return: True in case of a hit, False in case of a miss
        """
        if position in self.positions:
            self.hit_positions.append(position)
            self.positions.remove(position)
            if len(self.positions) == 0:
                self.is_sunk = True
            return True
        return False
