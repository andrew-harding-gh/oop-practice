from abc import abstractmethod

from oop_blackjack.abstracts import AbstractPlayer, AbstractCard


class BasePlayer(AbstractPlayer):
    def __init__(self):
        self.hand = list()

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        if not isinstance(value, list) or not all(isinstance(c, AbstractCard) for c in value):
            raise ValueError('Can only set a player hand to be a list of Card instances')
        self._hand = value

    @abstractmethod
    def hit(self):
        pass

    @abstractmethod
    def stay(self):
        pass


class Dealer(BasePlayer):
    pass

class Player(BasePlayer):
    def __init__(self):
        BasePlayer.__init__(self)
