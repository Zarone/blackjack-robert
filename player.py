from hand import Hand

class Player():
    """Class Player

    # Attributes:
    player_type = None  # (int)
    hand = None  # (Hand)
    winnings = None  # (int)
    """
    # Operations
    def __init__(self, id=0, player_type='player'):
        """function __init__
        """
        self.id = id
        self.type = player_type
        self.hand = Hand()
        self.winnings = 0

    def new_hand(self, deck):
        """function new_hand
        """
        self.hand.new_hand()
        if self.type == 'player':
            self.hand.add_card(deck)
            self.hand.add_card(deck)
        else:
            self.hand.add_card(deck)
            self.hand.add_card(deck)
            self.hand.cards[1].active = False

    def hit(self, deck):
        """function hit

        returns
        """
        self.hand.add_card(deck)

    def stand(self):
        """function stand

        returns
        """
        return self.hand.get_total() # should raise NotImplementedError()

    def double_down(self):
        """function double_down

        returns
        """
        return None # should raise NotImplementedError()

    def split(self):
        """function split

        returns
        """
        return None # should raise NotImplementedError()

    def surrender(self):
        """function surrender

        returns
        """
        return None # should raise NotImplementedError()
