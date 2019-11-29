from Player import Player
from Model.Move import Move
from Model.Checkers import Checkers
import random
from Model.CheckersBoard import CheckersBoard


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
        moves = []
        required_jumps = []
        for row in range(self._checkers.dimension):
            for col in range(self._checkers.dimension):
                # Check same color pieces as player to see if they can jump.
                if self._checkers.get(row, col) == self._player:
                    possible_jumps = self.check_for_jump(self._player, row, col)
                    if len(possible_jumps) > 0:
                        required_jumps += possible_jumps
                    else:
                        # This should find regular tiles to move to
                        if self._player == CheckersBoard.P1:
                            # If player is black
                            left = self._checkers.get(row - 1, col - 1)
                            right = self._checkers.get(row - 1, col + 1)
                            if left == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row - 1, col - 1))
                            if right == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row - 1, col + 1))
                        else:
                            # If player is white
                            left = self._checkers.get(row + 1, col + 1)
                            right = self._checkers.get(row + 1, col - 1)
                            if left == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row + 1, col + 1))
                            if right == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row + 1, col - 1))
        # If a move can be made we prioritize the list with possible moves
        random_index = 0
        if len(required_jumps) != 0:
            random_index = random.randint(0, len(required_jumps))
            move = required_jumps[random_index]
            return move
        else:
            random_index = random.randint(0, len(moves))
            move = moves[random_index]
            return move

    def _get_medium_move(self):
        return

    def check_for_jump(self, player: str, row: int, col: int):
        possible_jumps = []
        return possible_jumps
