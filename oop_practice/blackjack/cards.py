from functools import total_ordering

from oop_practice.blackjack.abstracts import AbstractCard


# @total_ordering
class FrenchCard(AbstractCard):
    """ ace (1) ranks low """

    valid_ranks = list(range(1, 14))
    valid_suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        return f'{self.repr_rank(self.rank)} of {self.suit}'

    # def __eq__(self, other):
    #     if isinstance(other, self.__class__):
    #         return self.rank == other.rank
    #     return False

    # def __lt__(self, other):
    #     return self.rank < other.rank

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value not in FrenchCard.valid_ranks:
            raise ValueError(f'French Cards can only have a rank in {FrenchCard.valid_ranks}')
        self._rank = value

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value):
        if value not in FrenchCard.valid_suits:
            raise ValueError(f'French Cards can only have a suit in {FrenchCard.valid_suits}')
        self._suit = value

    @staticmethod
    def repr_rank(rank):
        return {11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace'}.get(rank, rank)
