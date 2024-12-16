from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4

class CardTypeColored(Enum):
    NUMBER = 1
    PLUS_2 = 2
    REVERSE = 3
    SKIP = 4

class Wildcard(Enum):
    COLOR = 5
    PLUS_4 = 6
class Card:
    def __init__(self, wildcard: Wildcard = None, color: Color = None, type: CardTypeColored=None):
        self.wildcard = None
        self.color = None
        self.type = None
        if wildcard == None:
            if color == None: raise ValueError("Missing card color!")
            self.color = color
            if type == None: raise ValueError("Missing card type!")
            self.type = type
        else:
            self.wildcard = wildcard

    def __repr__(self):
        if self.wildcard == None:
            return f"{self.color} {self.type}"
        else:
            return {self.wildcard}