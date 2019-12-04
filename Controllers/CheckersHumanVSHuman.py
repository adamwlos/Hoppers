from Model.Players.PlayerHuman import PlayerHuman
from Controllers.CheckersController import CheckersController
from Model.Checkers import Checkers
from Model.CheckersBoard import CheckersBoard

class CheckersControllerHumanVSHuman(CheckersController):

    player1: PlayerHuman
    player2: PlayerHuman
    #

    def __init__(self):
        super().__init__( Checkers(CheckersBoard()))
        self.player1 = PlayerHuman
        self.player2 = PlayerHuman

    def report(self):
        s = self.checkers.get_board_string() + "\n" + self.checkers.board.player_1 + "has: " \
            + str(self.checkers.get_count(self.checkers.board.player_1)) + "pieces on board" + "\n"\
            + self.checkers.board.player_2 + "has: " + self.checkers.get_count(self.checkers.board.player_2) \
            + "pieces on board" + "\n" + str(self.checkers.get_players_turn()) + "'s turn to move" + "\n"

        print(s)

    def report_final_game_results(self):
        s = self.checkers.get_board_string() + self.checkers.board.player_1 + "has: " \
            + str(self.checkers.get_count(self.checkers.board.player_1)) + "pieces on board" + "\n"\
            + self.checkers.board.player_2 + "has: " + self.checkers.get_count(self.checkers.board.player_2) \
            + "pieces on board" + "\n" + "The winner is:" + self.checkers.get_winner() + "\n"

        print(s)

    def report_curr_move(self, player, move):
        s = player + "moved to" + move
        print(s)

    def play(self):
        while not self.checkers.is_gameover():
            self.report()
            players_turn = self.checkers.get_whos_turn()
            if players_turn == self.checkers.board.player_1:
                move = self.player1.get_move()
                self.report_curr_move(players_turn, move)
                self.checkers.jump(move.get_row(), move.get_col(), 1, 1)
            elif players_turn == self.checkers.board.player_2:
                move = self.player2.get_move()
                self.report_curr_move(players_turn, move)
                self.checkers.jump(move.get_row(), move.get_col(), 1, 1)
        self.report_final_game_results()


if __name__ == "__main__":
    checkersHvsH = CheckersControllerHumanVSHuman()
    checkersHvsH.play()
