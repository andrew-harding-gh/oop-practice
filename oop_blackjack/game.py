from oop_blackjack.decks import CasinoDeck
from oop_blackjack.players import Dealer, Player


# TODO: add flags for verbosity of game (eg. removing suites)

class BlackJack:
    def __init__(self, num_decks=8):
        self.deck = CasinoDeck(num_decks)
        self.dealer = Dealer()
        self.player = Player()
        self.playing = True

    def main(self):
        while self.playing:
            # first deal
            for card in self.deck.pick(2):
                self.dealer.is_dealt(card)
            for card in self.deck.pick(2):
                self.player.is_dealt(card)

            self.print_hand("Dealer", self.dealer.hand)
            self.print_hand("Player", self.player.hand)

            # blackjack check
            d = True if self.dealer.hand.value == 21 else False
            p = True if self.player.hand.value == 21 else False

            if d and p:
                BlackJack.line_print("End of Hand")
                print("Push")
                self.playing = self.fetch_continue()
            elif d and not p:
                BlackJack.line_print("End of Hand")
                print("Dealer wins :(")
                self.playing = self.fetch_continue()
            elif p and not d:
                BlackJack.line_print("End of Hand")
                print("You win! :)")
                self.playing = self.fetch_continue()

            # no blackjack, now normal player functionality



        # TODO: before new hand is dealt, do check for need to reshuffle (rebuild) deck

    def fetch_continue(self):
        cont_ = input('Continue? (Y/N):')
        while cont_.lower() not in ["y", "n"]:
            print('Please enter a valid response. `Y` or `N`')
        if cont_.lower() == "y":
            return True
        return False

    @staticmethod
    def print_hand(who, hand):
        """
        fancy print Hand
        :param who: Who's hand is being printed (eg. Player or Dealer)
        :param hand: BlackJackHand class instance
        """

        BlackJack.line_print(f"{who}'s hand")
        print(hand)
        print(f'Value of {hand.value}')

    @staticmethod
    def line_print(text):
        print(f"{'---------' * 3} {text}  {'---------' * 3}")


if __name__ == '__main__':
    BlackJack().main()
