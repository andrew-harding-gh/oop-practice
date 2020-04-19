from oop_blackjack.abstracts import AbstractCard


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
            raise ValueError(f'French Cards can only be in {FrenchCard.valid_suites}')
        self._suite = value

    @staticmethod
    def repr_rank(rank):
        d = {11: 'Jack', 12: 'Queen', 13: 'King'}
        return d[rank] if rank > 10 else rank

    def __repr__(self):
        return f'{self.repr_rank(self.rank)} of {self.suite}'

    def __eq__(self, other):
        if isinstance(other, FrenchCard):
            return self.rank == other.rank and self.suite == self.suite
        return False


