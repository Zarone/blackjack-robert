
class Card():
    """Class Card

    # Attributes:
    value = None  # (int)
    suit = None  # (string)
    """
    # Operations
    def __init__(self, suit: str, value: int, active=True):
        self.value = value
        self.suit = suit
        self.active = active

    def get_str(self):
        if self.value == 1:
            return 'Ace of ' + self.suit
        elif self.value == 11:
            return 'Jack of ' + self.suit
        elif self.value == 12:
            return 'Queen of ' + self.suit
        elif self.value == 13:
            return 'King of ' + self.suit
        else:
            return str(self.value) + ' of ' + self.suit