from Player import Player
from Model.Move import Move
import random
from Model.CheckersBoard import CheckersBoard
from Model.Checkers import Checkers


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
            TODO: Make it search the 2 diagonals infront of it
        """
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

    def check_for_jump(self, player: str, row: int, col: int):
        """ Checks the two front diagonals for possible jumps.
            Black begins on the bottom side, white begins at the top side.
            left and right directions in perspective of the board side.
        """
        possible_jumps = []
        other_player = CheckersBoard.other_player(player)
        # Check the player to correspond to direction
        if player == CheckersBoard.PLAYER1:
            # If black then check row-1,col-1 and row-1,col+1
            left = self._checkers.get(row-1,col-1)
            right = self._checkers.get(row-1,col+1)
            further_left = self._checkers.get(row-2, col-2)
            further_right = self._checkers.get(row-2, col+2)
            if left == other_player and further_left == CheckersBoard.EMPTY:
                possible_jumps.append(Move(row, col, row-2, col-2))
            if right == other_player and further_right == CheckersBoard.EMPTY:
                possible_jumps.append(Move(row, col, row-2, col+2))
        elif player == CheckersBoard.PLAYER2:
            # If white then check row+1,col-1 and row+1,col+1
            left = self._checkers.get(row+1,col-1)
            right = self._checkers.get(row+1,col+1)
            further_left = self._checkers.get(row+2, col-2)
            further_right = self._checkers.get(row+2, col+2)
            if left == other_player and further_left == CheckersBoard.EMPTY:
                possible_jumps.append(Move(row, col, row+2, col-2))
            if right == other_player and further_right == CheckersBoard.EMPTY:
                possible_jumps.append(Move(row, col, row+2, col+2))
        return possible_jumps

    def _get_medium_move(self):
        """ Medium mode
        """
        return