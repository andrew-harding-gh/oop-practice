from oop_blackjack.decks import CasinoDeck
from oop_blackjack.players import Dealer, Player


class BlackJack:
    def __init__(self, num_decks=8):
        self.deck = CasinoDeck(num_decks)
        self.dealer = Dealer()
        self.player = Player()
