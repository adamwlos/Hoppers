from Checkers import Checkers
from CheckersBoard import CheckersBoard


class CheckersController:
    """

    """
    checkers: Checkers

    # player1: Player
    # player2: Player

    def __init__(self, checkers):
        self.checkers = checkers

    def report(self):
        s = self.checkers.get_board_string() + "\n" + CheckersBoard.P1 + "has: " \
            + str(self.checkers.get_count(CheckersBoard.P1)) + "pieces on board" + "\n"\
            + CheckersBoard.P2 + "has: " + self.checkers.get_count(CheckersBoard.P2) + "pieces on board" + "\n"\
            + str(self.checkers.get_players_turn()) + "'s turn to move" + "\n"

        print(s)

    def report_final_game_results(self):
        s = self.checkers.get_board_string() + CheckersBoard.P1 + "has: " \
            + str(self.checkers.get_count(CheckersBoard.P1)) + "pieces on board" + "\n"\
            + CheckersBoard.P2 + "has: " + self.checkers.get_count(CheckersBoard.P2) + "pieces on board" + "\n"\
            + "The winner is:" + self.checkers.get_winner() + "\n"

        print(s)

    def report_curr_move(self, player, move):
        pass

    def play(self):
        while not self.checkers.is_gameover():
            self.report()
            # players_turn = self.checkers.get_whos_turn()

        self.report_final_game_results()

