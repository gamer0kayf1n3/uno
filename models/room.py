import card
from enum import Enum
class Status(Enum):
    WAITING = 0
    ONGOING = 1
    FINISHED = 2
class Room:
    CONFIG = {}
    PLAYERS = {}

    CURRENT_CARD = None
    DECK = []
    PLAYER_CARDS = {}

    REVERSE_STATUS = False
    GAME_STATUS: Status = Status.WAITING
    def on_game_start(self):
        if len(self.PLAYERS) < 2: raise LessThan2PlayersError("Not enough players!")
        if self.GAME_STATUS != Status.ONGOING: self.GAME_STATUS = Status.ONGOING
        DECK = card.deck()

class LessThan2PlayersError(Exception):
    pass