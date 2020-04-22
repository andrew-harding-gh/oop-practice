import pytest

from oop_blackjack.decks import FrenchDeck
from oop_blackjack.players import Dealer, Player, BasePlayer


def test_deal_pick_to_player():
    deck = FrenchDeck()
    dealer = Dealer()
    player = Player()

    picked = deck.pick()

    with pytest.raises(TypeError):
        player.is_dealt(picked)

    with pytest.raises(TypeError):
        dealer.is_dealt(picked)

    player.is_dealt(picked[0])
    dealer.is_dealt(picked[0])

    assert len(player.hand) == 1
    assert player.hand.cards == picked
    assert player.hand.cards[0] == picked[0]

    assert len(dealer.hand) == 1
    assert dealer.hand.cards == picked
    assert dealer.hand.cards[0] == picked[0]