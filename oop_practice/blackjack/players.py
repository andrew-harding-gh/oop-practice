from oop_practice.blackjack.abstracts import AbstractCard
from oop_practice.blackjack.hands import BaseHand, BlackJackHand


class BasePlayer:
    def __init__(self):
        self._hand = BaseHand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if not isinstance(value, BaseHand):
            raise ValueError(f'{self.__class__.__name__} hand can only be set as an instance of `{BaseHand.__name__}`')
        self._hand = value

    def is_dealt(self, card):
        if not isinstance(card, AbstractCard):
            raise TypeError(f'Can only deal to this player objects implementing {AbstractCard.__name__} interface')
        self.hand.add(card)


# TODO: add chip/$$ count
class BlackJackPlayer(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)
        self._hand = BlackJackHand()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if not isinstance(value, BlackJackHand):
            raise ValueError(f'{self.__class__.__name__} hand can only be set as an instance of `{BlackJackHand.__name__}`')
        self._hand = value