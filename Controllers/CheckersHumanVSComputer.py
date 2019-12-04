from Model.Players.PlayerHuman import PlayerHuman
from Model.Players.PlayerKing import PlayerKing
from Model.Players.PlayerComputer import PlayerComputer
from Model.Players.PlayerComputerKing import PlayerComputerKing
from Model.Checkers import Checkers
from Controllers.CheckersController import CheckersController
from Model.CheckersBoard import CheckersBoard

class CheckersHumanVSComputer(CheckersController):

    player1: PlayerHuman
    player2: PlayerComputer
    checkers: Checkers
    difficulty: int

    def __init__(self, checkers, difficulty):
        super.__init__(checkers)
        self.player1 = PlayerHuman(CheckersBoard.player_1, self.checkers)
        self.player2 = PlayerComputer(CheckersBoard.player_2, self.checkers, 
                                                                    difficulty)
        self.difficulty = difficulty

    def play(self):
        """ Runs the game loop for human vs computer mode. Until the game is
            over, we continue requesting moves from the user or from the
            computers get move method.
        """
        while not self.checkers.is_gameover():
            players_turn = self.checkers.get_whos_turn()
            if players_turn == self.checkers.board.player_1:
                # This will need params from the visualizer
                move = self.player2.get_move()
                self.checkers.jump(move.get_row(), move.get_col(), 1, 1)
            elif players_turn == self.checkers.board.player_2:
                # Gets a list of moves unlike for PlayerHuman
                moves = self.player2.get_move()
                # If loops through the move/move path and makes the moves
                if len(moves) > 0:
                    for move in moves:
                       self.checkers.jump(move.get_row, move.get_col, 
                                            move.get_drow, move.get_dcol) 
