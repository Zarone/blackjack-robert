import os
from deck import Deck
from player import Player
import Cards

class Blackjack():
    """Class Blackjack

    # Attributes:
    players = None  # ([Player])
    dealer = None  # (Player)
    deck = None  # (Deck)
    """

    # Operations
    def __init__(self, video_stream, train_ranks, train_suits):
        """function __init__
        """
        self.video_stream = video_stream
        self.train_ranks = train_ranks
        self.train_suits = train_suits

        self.players = []
        self.dealer = Player(9999, 'dealer')
        self.deck = Deck()
        self.new_game(1)

    def player_turn(self, p):
        turn = True
        while turn:
            os.system('cls' if os.name == 'nt' else 'clear')
            '''
            cards = self.get_cards()
            if cards is not None:
                s = ''
                for i in range(len(cards)):
                    s += cards[i].best_rank_match + ' of ' + cards[i].best_suit_match + '. '
                print(s)
            else:
                print('None found')
            '''

            print('Dealers hand: ' + self.dealer.hand.cards[0].get_str() + ' and an unkown card')
            print('Player ' + str(p.id) + "'s cards:")
            for c in p.hand.cards:
                print(c.get_str())
            print('For a total of: ' + str(p.hand.get_total()))
            print('Hit (h) or stand (s)?')
            x = input()
            if x == 'h':
                os.system('cls' if os.name == 'nt' else 'clear')
                p.hit(self.deck)
                print('Player ' + str(p.id) + "'s cards:")
                for c in p.hand.cards:
                    print(c.get_str())

                if p.hand.is_bust():
                    print('For a total of: ' + str(p.hand.get_total()))
                    print('Bust')
                    turn = False
                else:
                    print('For a total of: ' + str(p.hand.get_total()))
            elif x == 's':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Player ' + str(p.id) + ' is standing with a hand of: ')
                for c in p.hand.cards:
                    print(c.get_str())
                print('For a total of: ' + str(p.hand.get_total()))
                turn = False
        print('Press any key to continue...')
        input()

    def dealer_turn(self):
        turn = True
        os.system('cls' if os.name == 'nt' else 'clear')
        self.dealer.hand.cards[1].active = True
        while turn:
            if self.dealer.hand.get_total() < 17:
                self.dealer.hit(self.deck)
            else:
                turn = False
        s = ''
        for c in self.dealer.hand.cards:
            s += c.get_str() + ' '
        print('Dealers hand: ' + s)
        print('For a total of: ' + str(self.dealer.hand.get_total()))
        if self.dealer.hand.is_bust():
            print('Dealer bust')

    def find_winner(self):
        player_win = False
        for p in self.players:
            if p.hand.is_bust():
                print('Player ' + str(p.id) + ' is bust')
            else:
                print('Player ' + str(p.id) + "'s total is: " + str(p.hand.get_total()))
        for p in self.players:
            if self.dealer.hand.is_bust() and not p.hand.is_bust():
                dealer_win = False
                player_win = True
                print('Player ' + str(p.id) + ' wins!')
            elif p.hand.is_bust():
                dealer_win = True
            elif self.dealer.hand.get_total() < p.hand.get_total():
                dealer_win = False
                player_win = True
                print('Player ' + str(p.id) + ' wins!')
            else:
                dealer_win = True
        if dealer_win and not player_win:
            print('Dealer wins...')

    def resolve_round(self):
        """function resolve_round

        returns
        """
        for p in self.players:
            self.player_turn(p)
        self.dealer_turn()
        self.find_winner()

    def new_game(self, num_players):
        """function new_game

        returns
        """
        self.players = []
        self.dealer.winnings = 0
        self.dealer.new_hand(self.deck)
        for i in range(num_players):
            self.players.append(Player(i + 1))
            self.players[-1].new_hand(self.deck)
    '''
    def get_cards(self):
        img = self.video_stream.read()

        pre = Cards.preprocess_image(img)

        cnts, cnt_card = Cards.find_cards(pre)

        if len(cnts) != 0:
            cards = []

            for i, cnt in enumerate(cnts):
                if cnt_card[i] == 1:
                    found_card = Cards.preprocess_card(cnt, img)
                    cards.append(found_card)
                    found_card.best_rank_match, found_card.best_suit_match, found_card.rank_diff, found_card.suit_diff = Cards.match_card(found_card, self.train_ranks, self.train_suits)
            if len(cards) != 0:
                for c in cards:
                    print(c)
                return cards
        return None
    '''
