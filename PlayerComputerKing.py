from Player import Player
from Move import Move
import Checkers

class PlayerComputerKing(Player):
    """ PlayerComputerKing represents a standard piece of colour black or white and
        is able to move in all four diagonals. This player type does not take
        in user input but rather calculates its own moves.
    """

    def __init__(self, player: str, checkers: Checkers, difficulty: int):
        # _difficulty is the integer 0 or 1. 0=Easy, 1=Medium
        self._difficulty = difficulty
        self._player = player
        self._checkers = checkers

    def get_move(self) -> Move:
        """ Based on what the user selected as the computers difficulty level,
            a move calculate based on that difficulty level will be returned.
            When calculating it is known the player can move in all four diagonals.
        """
        if self._difficulty == 0:
            return self._get_easy_move()
        else:
            return self._get_medium_move()

    def _get_easy_move(self):
        return

    def _get_medium_move(self):
        return
