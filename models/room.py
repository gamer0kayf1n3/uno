import card, player
import random
from enum import Enum
import uuid
class Status(Enum):
    WAITING = 0
    ONGOING = 1
    FINISHED = 2
class Room:
    CONFIG = {
        "number_of_cards": 7
    }
    PLAYERS = {}

    CURRENT_CARD = None
    DECK = []
    PLAYER_CARDS = {}

    REVERSE_STATUS = False
    GAME_STATUS: Status = Status.WAITING
    def on_game_start(self):
        if len(self.PLAYERS) < 2: raise LessThan2PlayersError("Not enough players!")
        if self.GAME_STATUS != Status.ONGOING: self.GAME_STATUS = Status.ONGOING
        self.DECK = card.deck()
        for player in self.PLAYERS:
            self.PLAYER_CARDS[player] = []
            random.shuffle(self.DECK)
            for x in range(self.CONFIG["number_of_cards"]):
                self.PLAYER_CARDS[player].append(self.DECK.pop())
    
    def on_new_player(self, player: player.Player):
        self.PLAYERS[uuid] = {"name": player.NAME}
        if self.GAME_STATUS == Status.ONGOING:
            return
    

class LessThan2PlayersError(Exception):
    pass
if __name__ == "__main__":
    room = Room()
    room.on_game_start()
print("d")
