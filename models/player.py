from enum import Enum
class PlayerRoles(Enum):
    PLAYER = 0
    SPECTATOR = 1
    GAMEMASTER = 2
class Player:
    NAME = ""
    ROLE = 1

    def __init__(self, name):
        self.NAME = name