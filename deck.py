from random import shuffle
from card import Card

class Deck():
    """Class Deck

    # Attributes:
    suits = None # ([suits])
    cards = None  # ([Card])
    """
    # Operations
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.cards = []
        self.new_deck()

    def shuffle(self):
        """function shuffle

        returns
        """
        shuffle(self.cards)

    def new_deck(self):
        """function new_deck

        returns
        """
        for i in self.suits:
            for j in range(1, 13):
                self.cards.append(Card(i, j))
        self.shuffle()

    def draw_card(self):
        """function draw_card

        returns Card
        """
        return self.cards.pop()
