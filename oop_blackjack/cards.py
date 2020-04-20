from functools import total_ordering

from oop_blackjack.abstracts import AbstractCard


# @total_ordering  # fill orderings from eq and one operator
class FrenchCard(AbstractCard):
    valid_ranks = list(range(1, 14))
    valid_suites = ['Diamonds', 'Hearts', 'Clubs', 'Spades']

    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if not 13 >= value >= 1:
            raise ValueError('French Cards can only be ranked 1 (Ace) through King (13)')
        self._rank = value

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, value):
        if value not in FrenchCard.valid_suites:
            raise ValueError(f'French Cards can only have a suite in {FrenchCard.valid_suites}')
        self._suite = value

    @staticmethod
    def repr_rank(rank):
        d = {11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace'}
        return d.get(rank, rank)

    def __repr__(self):
        return f'{self.repr_rank(self.rank)} of {self.suite}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rank == other.rank and self.suite == other.suite
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # def __lt__(self, other):
    #     return self.rank < other.rank  and self.suite < other.suite
