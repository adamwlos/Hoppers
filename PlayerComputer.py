from Player import Player
from Move import Move
import random
import CheckersBoard
import Checkers

class PlayerComputer(Player):
    """ PlayerComputer represents a standard piece of colour black or white and
        is restricted to move forwards diagonally. This player type does not take
        in user input but rather calculates its own moves.
    """

    def __init__(self, player: str, checkers: Checkers, difficulty: int):
        self._difficulty = difficulty
        self._player = player
        self._checkers = checkers

    def get_move(self) -> Move:
        """ Based on what the user selected as the computers difficulty level,
            a move calculate based on that difficulty level will be returned.
            When calculating there will be restrictions of the player only being
            able to move forward diagonally
        """
        if self._difficulty == 0:
            return self._get_easy_move()
        else:
            return self._get_medium_move()

    def _get_easy_move(self):
        """ Easy mode will calculate a random move to make
            Checks if any piece can jump, if so does that. Otherwise makes random move
        """
        moves = []
        required_jumps = []
        for row in range(self._checkers.dimension):
            for col in range(self._checkers.dimension):
                # Check same color pieces as player to see if they can jump.
                if self._checkers.get(row, col) == self._player:
                    possible_jump = self.check_for_jump(self._player, self._checkers, row, col)
                    if possible_jump[0] != -1 and possible_jump[1] != -1:

                        required_jumps.append(Move(row, col, possible_jump[0], possible_jump[1]))

                    else:
                        if self._player == CheckersBoard.P1:
                            # If player is black
                            left = self._checkers.get(row-1, col-1)
                            right = self._checkers.get(row-1, col+1)
                            if left == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row-1, col-1))
                            if right == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row-1, col+1))

                        else:
                            # If player is white
                            left = self._checkers.get(row+1, col+1)
                            right = self._checkers.get(row+1, col-1)
                            if left == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row+1, col+1))
                            if right == CheckersBoard.EMPTY:
                                moves.append(Move(row, col, row+1, col-1))
        random_index = 0
        # If a move can be made we prioritize the list with possible moves to choose from
        if len(required_jumps) != 0:
            random_index = random.randint(0, len(required_jumps))
            move = required_jumps[random_index]
            return move
        else:
            random_index = random.randint(0, len(moves))
            move = moves[random_index]
            return move

    def check_for_jump(self, player: str, checkers: Checkers, row: int, col: int):
        """ Checks the two front diagonals for possible jumps
            Black will always start on the bottom side of the board. White will start at the top
            TODO: Improve how this method looks for valid paths that moves can be made in.
        """

        final_row = -1
        final_col = -1

        # This is put the search into the perspective of the specific player colour
        if player == CheckersBoard.P1:
            left_dir = (-1,-1)
            right_dir = (-1,1)
        else:
            left_dir = (1,1)
            right_dir = (1,-1)

        found = False

        while not found:
            left_diag = (row+left_dir[0], col+left_dir[1])
            after_left_diag = (row+2*left_dir[0], col+2*left_dir[1])
            right_diag = (row+right_dir[0], col+right_dir[1])
            after_right_diag  = (row+2*right_dir[0], col+2*right_dir[1])

            left_player = checkers.get(left_diag[0, left_diag[1]])
            after_left_player = checkers.get(after_left_diag[0], after_left_diag[1])
            right_player = checkers.get(right_diag[0], right_diag[1])
            after_right_player = checkers.get(after_right_diag[0], after_right_diag[1])

            if left_player == CheckersBoard.get_other_player(player) and after_left_player == CheckersBoard.EMPTY:
                row = left_diag[0]
                col = left_diag[1]
            elif right_player == CheckersBoard.get_other_player(player) and after_right_player == CheckersBoard.EMPTY:
                row = right_diag[0]
                col = right_diag[1]
            else:
                found = True
                final_row = row
                final_col = col

        return (final_row, final_col)

    def _get_medium_move(self):
        """ Medium mode
        """
        return