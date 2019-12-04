from abc import ABC, abstractmethod
from Model.Move import Move
from Model.Checkers import Checkers
#
class Player(ABC):
    """ Player serves as parent class to PlayerHuman, PlayerKing, 
        PlayerComputer, and PlayerKingComputer. This class is not for in game 
        use but rather an abstract class that enforces consistency and for a 
        base that can allow for player types to become interchangable. Player 
        inherits ABC as this is pythons way of signifying the class is abstract
    """

    def __init__(self, player: str, checkers: Checkers):
        self._player = player
        self._checkers = checkers
    
    #@abstractmethod
    def get_move(self) -> Move:
        """ Retrieves a valid move for the player to make
        """
        return
