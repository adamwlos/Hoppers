from CheckersBoard import CheckersBoard


class Checkers:
    board = CheckersBoard
    whos_turn = CheckersBoard.player_1
    dimension = 10

    def __init__(self):
        pass

    def get_whos_turn(self):
        return self.whos_turn

    def jump(self):
        pass

    def has_move(self):
        pass

    def is_gameover(self):
        pass

    def get_winner(self):
        if self.is_gameover():
            p1_token = self.get_count(self.board.player_1)
            p2_token = self.get_count(self.board.player_2)
            if p1_token > p2_token:
                return self.board.player_1
            elif  p2_token > p1_token:
                return self.board.player_2
            else:
                return self.board.empty
        else:
            return self.board.empty
            return

    def get_count(self, player):
        return self.board.get_count(player)

    def get_board_string(self):
        return str(self.board)
