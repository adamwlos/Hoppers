from Model.Players.PlayerHuman import PlayerHuman
from Controllers.CheckersController import CheckersController
from Model.Checkers import Checkers
from Model.CheckersBoard import CheckersBoard

class CheckersControllerHumanVSHuman(CheckersController):

    player1: PlayerHuman
    player2: PlayerHuman


    def __init__(self):
        super().__init__( Checkers(CheckersBoard()))
        self.player1 = PlayerHuman
        self.player2 = PlayerHuman


if __name__ == "__main__":
    checkersHvsH = CheckersControllerHumanVSHuman()
    checkersHvsH.play()
