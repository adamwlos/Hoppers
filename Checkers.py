from CheckersBoard import CheckersBoard


class Checkers:
    board = CheckersBoard
    whos_turn = CheckersBoard.player_1

    def __init__(self):
        pass

    def get_whos_turn(self):
        return self.whos_turn

    def jump(self, row, col, drow, dcol):
        player = self.get_whos_turn()
        if player != self.board.empty:
            if self.board.jump(row, col, drow, dcol, player):
                if self.is_gameover():
                    self.whos_turn = self.board.empty
                elif self.board.who_has_move() == CheckersBoard.both:
                    self.whos_turn = self.board.other_player(player)
                elif self.board.who_has_move() == self.board.other_player(player) \
                        and self.board.other_player(player) != CheckersBoard.empty:
                    self.whos_turn = self.board.other_player(player)
                return True
            return False


    def is_gameover(self):
        if self.board.who_has_move() == CheckersBoard.empty:
            return True
        elif self.board.get_count(self.board.player_1) == 0 or self.board.get_count(self.board.player_2) == 0:
            return True
        else:
            return False

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

    def get_count(self, player):
        return self.board.get_count(player)

    def get_board_string(self):
        return str(self.board)
