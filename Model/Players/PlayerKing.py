from Player import Player
from Model.Move import Move
from Model.Checkers import Checkers

class PlayerKing(Player):
    """ PlayerKing represents a standard piece of colour black or white and
        is able to move in all four diagonals.
    """

    def __init__(self, player: str, checkers: Checkers):
        self._player = player
        self._checkers = checkers

    def get_move(self, row: int, col: int, drow: int, dcol: int):
        """ Pygame will retrieve the coordinates of the tile and pass those 
            into getMove to return a Move object.    
        """
        # Row, col are the coordinates of the piece you are moving onto some 
        # tile: final_row, final_col
        return Move(row, col, drow, dcol)
