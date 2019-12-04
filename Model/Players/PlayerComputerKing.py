from Model.Players.Player import Player
from Model.Move import Move
from Model.Checkers import Checkers
import random
from Model.CheckersBoard import CheckersBoard


class PlayerComputerKing(Player):
    """ PlayerComputerKing represents a standard piece of colour black or white
        and is able to move in all four diagonals. This player type does not 
        take in user input but rather calculates its own moves.
    """

    def __init__(self, player: str, checkers: Checkers, difficulty: int):
        # _difficulty is the integer 0 or 1. 0=Easy, 1=Medium
        self._difficulty = difficulty
        self._player = player
        self._checkers = checkers

    def get_move(self):
        """ Based on what the user selected as the computers difficulty level,
            a move calculate based on that difficulty level will be returned.
            When calculating it is known the player can move in all four 
            diagonals.
        """
        if self._difficulty == 0:
            return self._get_easy_move()
        else:
            # Different stategies/difficulties can be attached here
            return

    def _get_easy_move(self):
        """ Easy mode for the computer king will search the four diagonals
            around the player for empty spots and potential pieces to jump.
            If it finds pieces to jump it prioritizes them.This method will 
            return either a list containing a single more or a list containing 
            multiple moves representing a path of multiple jumps.
        """
        moves = []
        required_jumps = []
        for row in range(self._checkers.dimension):
            for col in range(self._checkers.dimension):
                # Check same color pieces as player to see if they can jump.
                if self._checkers.get(row, col) == self._player:
                    path_made = False
                    found_jumps = []
                    for i in range(3):
                        current_path = []
                        while (not path_made):
                            jumps = self.check_for_jump(self._player, row, col)
                            if jumps == []:
                                path_made = True
                                break
                            current_path += (jumps)
                            incrow = 0
                            inccol = 0
                            # South west and east
                            if i == 0:
                                incrow = 2
                                inccol = 2
                            elif i == 1:
                                incrow = 2
                                incrow = -2
                            # North west and east
                            elif i == 2:
                                incrow = -2
                                inccol = -2
                            elif i == 3:
                                incrow = -2
                                incrow = 2
                            row += incrow
                            col += inccol
                        found_jumps.append(current_path)
                    if len(found_jumps) > 0:
                        required_jumps += found_jumps
                    else:
                        # This should find regular tiles to move to
                        north_west = self._checkers.get(row - 1, col - 1)
                        north_east = self._checkers.get(row - 1, col + 1)
                        south_west = self._checkers.get(row + 1, col + 1)
                        south_east = self._checkers.get(row + 1, col - 1)
                        if north_west == CheckersBoard.empty:
                            moves.append(Move(row, col, row - 1, col - 1))
                        if north_east == CheckersBoard.empty:
                            moves.append(Move(row, col, row - 1, col + 1))
                        if south_west == CheckersBoard.empty:
                            moves.append(Move(row, col, row + 1, col + 1))
                        if south_east == CheckersBoard.empty:
                            moves.append(Move(row, col, row + 1, col - 1))
        # If a move can be made we prioritize the list with possible moves
        random_index = 0
        if len(required_jumps) != 0:
            random_index = random.randint(0, len(required_jumps))
            move_path = required_jumps[random_index]
            return move_path
        else:
            random_index = random.randint(0, len(moves))
            move = moves[random_index]
            return [move]

    def check_for_jump(self, player: str, row: int, col: int):
        found_jumps = []
        other_player = self._checkers.other_player(player)
        
        # Tiles where an opponent might be
        north_west = self._checkers.get(row-1,col-1)
        north_east = self._checkers.get(row-1,col+1)
        south_west = self._checkers.get(row+1,col-1)
        south_east = self._checkers.get(row+1,col+1)
        # Tiles where a blank space might be
        further_nw = self._checkers.get(row-2, col-2)
        further_ne = self._checkers.get(row-2, col+2)
        further_sw = self._checkers.get(row+2, col-2)
        further_se = self._checkers.get(row+2, col+2)

        # Checks if a jump is possible and adds the possible Move to the list
        if north_west == other_player and further_nw == CheckersBoard.empty:
            found_jumps.append(Move(row, col, row-2, col-2))
        if north_east == other_player and further_ne == CheckersBoard.empty:
            found_jumps.append(Move(row, col, row-2, col+2))
        if south_west == other_player and further_sw == CheckersBoard.empty:
            found_jumps.append(Move(row, col, row+2, col-2))
        if south_east == other_player and further_se == CheckersBoard.empty:
            found_jumps.append(Move(row, col, row+2, col+2))
        
        return found_jumps
