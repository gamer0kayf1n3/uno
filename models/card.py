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
    WILD = 5
    PLUS_4 = 6

class Card:
    def __init__(self, *, wildcard: Wildcard = None, color: Color = None, card_type: CardTypeColored = None, number: int = None):
        if wildcard is not None:
            # Wildcard cards
            self.wildcard = wildcard
            self.color = None  # Color can be chosen later during play
            self.card_type = None
            self.number = None
        elif color is not None and card_type is not None:
            # Colored action or number cards
            self.wildcard = None
            self.color = color
            self.card_type = card_type
            if card_type == CardTypeColored.NUMBER:
                if number is None or not (0 <= number <= 9):
                    raise ValueError("Number must be between 0 and 9 for NUMBER cards.")
                self.number = number
            else:
                self.number = None
        else:
            raise ValueError("Invalid card configuration. Must specify either wildcard or color with card type.")

    def __repr__(self):
        if self.wildcard is not None:
            return f"Wildcard: {self.wildcard.name}"
        elif self.card_type == CardTypeColored.NUMBER:
            return f"{self.color.name} {self.number}"
        else:
            return f"{self.color.name} {self.card_type.name}"

# Example usage:
try:
    card1 = Card(color=Color.RED, card_type=CardTypeColored.NUMBER, number=5)
    card2 = Card(color=Color.BLUE, card_type=CardTypeColored.PLUS_2)
    card3 = Card(wildcard=Wildcard.WILD)
    card4 = Card(wildcard=Wildcard.PLUS_4)

    print(card1)
    print(card2)
    print(card3)
    print(card4)
except ValueError as e:
    print(e)

def generate_all_cards():
    cards = []

    # Generate number cards (0-9 for each color, two copies of each except 0)
    for color in Color:
        cards.append(Card(color=color, card_type=CardTypeColored.NUMBER, number=0))
        for number in range(1, 10):
            cards.append(Card(color=color, card_type=CardTypeColored.NUMBER, number=number))
            cards.append(Card(color=color, card_type=CardTypeColored.NUMBER, number=number))

    # Generate action cards (two copies for each color and type)
    for color in Color:
        for card_type in [CardTypeColored.PLUS_2, CardTypeColored.REVERSE, CardTypeColored.SKIP]:
            cards.append(Card(color=color, card_type=card_type))
            cards.append(Card(color=color, card_type=card_type))

    # Generate wildcards (4 copies each)
    for wildcard in Wildcard:
        for _ in range(4):
            cards.append(Card(wildcard=wildcard))

    return cards
print(generate_all_cards())