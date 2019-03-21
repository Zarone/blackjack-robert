
class Hand():
    """Class Hand

    # Attributes:
    cards = None  # ([Cards])
    """
    # Operations
    def __init__(self):
        self.cards = []

    def new_hand(self):
        """function new_hand
        """
        self.cards = []

    def add_card(self, deck):
        """function add_card

        card: Card

        returns
        """
        self.cards.append(deck.draw_card())

    def get_total(self):
        """function get_total

        returns int
        """
        tot = 0
        ace = 0
        for c in self.cards:
            if c.active:
                if c.value == 1:
                    ace = 1
                if c.value < 10:
                    tot += c.value
                else:
                    tot += 10
        if ace == 1 and tot + 10 < 21:
            return tot + 10
        return tot

    def is_bust(self):
        return self.get_total() > 21
