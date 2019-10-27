import PlayerHuman
import Checkers
from CheckersController import CheckersController
import PlayerHuman


class CheckersControllerHumanVSHuman(CheckersController):
    player1: PlayerHuman
    player2: PlayerHuman
    checkers: Checkers

    def __init__(self):
        super().__init__(checkers)
        self.player1 = PlayerHuman
        self.player2 = PlayerHuman
        self.checkers = Checkers


if __name__ == "__main__":
    checkers = Checkers
    checkersHvsH = CheckersControllerHumanVSHuman()
    checkersHvsH.play()
