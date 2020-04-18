from abc import abstractmethod

from oop_blackjack.abstracts import AbstractPlayer, AbstractCard, AbstractHand
from oop_blackjack.hands import BaseHand, BlackJackHand


class BasePlayer(AbstractPlayer):
    def __init__(self):
        self.hand = BaseHand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if not isinstance(value, AbstractHand):
            raise ValueError('Player hand can only be set as an instance of `Hand`')
        self._hand = value


class Dealer(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)


class Player(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)
