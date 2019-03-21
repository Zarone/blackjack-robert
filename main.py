class Blackjack():
    def __init__(self, players=1):
        self.players = [Player() for i in range(players)]

class Player():
    def __init__(self):
        pass

    def turn(self):
        pass

    def stand(self, player):
        pass

    def hit(self, player):
        pass
