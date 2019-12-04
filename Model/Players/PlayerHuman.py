from Model.Players.Player import Player
from Model.Move import Move
from Model.Checkers import Checkers

class PlayerHuman(Player):
    """ PlayerHuman represents a standard piece of colour black or white and
        is restricted to move forwards diagonally.
    """

    def __init__(self, player: str, checkers: Checkers):
        super.__init__(player, checkers)
 #
    def get_move(self, row: int, col: int, drow: int, dcol: int):
        """ Pygame will retrieve the coordinates of the tile and pass those
        into getMove to return a Move object.
        """
        # Row, col are the coordinates of the piece you are moving onto some
        # tile: final_row, final_col
        return Move(row, col, drow, dcol)
