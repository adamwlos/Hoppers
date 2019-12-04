class Move:
    """ This class represents a move on the board. A Move object gives the
        game access to the row and column of the intial piece and the row
        and column of the tile they move to.
    """

    _final_row: int
    _final_col: int
    _row: int
    _col: int

    def __init__(self, row: int, col: int, final_row: int, final_col: int):
        self._row = row
        self._col = col
        self._final_row = final_row
        self._final_col = final_col

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col

    def get_final_row(self):
        return self._final_row
    
    def get_final_col(self):
        return self._final_col

    def get_dcol(self):
        return self._final_col - self._col

    def get_drow(self):
        return self._final_row - self._row
