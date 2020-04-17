from abc import ABC, abstractmethod
from collections import namedtuple

card = namedtuple('Card', ['num', 'suite'])

'''
 A class that has a metaclass derived from ABCMeta cannot be instantiated unless 
 all of its abstract methods and properties are overridden.
'''


class AbstractCard(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @property
    @abstractmethod
    def rank(self):
        pass

    @property
    @abstractmethod
    def suite(self):
        pass


class AbstractDeck(ABC):
    def _init_deck(self):
        return list()

    @abstractmethod
    def pick(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def cut(self):
        pass
