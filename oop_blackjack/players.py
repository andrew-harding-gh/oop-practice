from abc import abstractmethod

from oop_blackjack.abstracts import AbstractPlayer, AbstractCard, AbstractHand
from oop_blackjack.hands import BaseHand, BlackJackHand


class BasePlayer(AbstractPlayer):
    def __init__(self):
        self._hand = BaseHand()

    @property
    def hand(self):
        return self._hand

    # @hand.setter
    # def hand(self, value):
    #     if not isinstance(value, AbstractHand):
    #         raise ValueError('Player hand can only be set as an instance of `Hand`')
    #     self._hand = value

    def is_dealt(self, card):
        if not isinstance(card, AbstractCard):
            raise TypeError('Can only deal Cards to Players')
        self.hand.add(card)


class Dealer(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)
        self._hand = BlackJackHand(dealer=True)


# TODO: add chip/$$ count
class Player(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)
        self._hand = BlackJackHand()
