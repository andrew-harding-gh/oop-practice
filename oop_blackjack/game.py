from oop_blackjack.decks import CasinoDeck
from oop_blackjack.players import Dealer, Player


# TODO: add flags for verbosity of game (eg. removing suites)
# TODO: add initial print statement about when the dealer will be forced to hit/stay
# TODO: double down (split on identical cards)
# TODO: double (take one card and double bet)
# TODO: surrender (lose half bet)
# TODO: insurance (dealer has ace face up)
# TODO: display dealer cards when hand ends

class BlackJack:
    def __init__(self, num_decks=8):
        self.deck = CasinoDeck(num_decks)
        self.dealer = Dealer()
        self.player = Player()
        self.first = True
        # self.playing = True

    def main(self):
        playing = True
        while playing:
            self.new_round()  # do basic stuff

            # blackjack check
            dbj = self.dealer.hand.blackjack
            pbj = self.player.hand.blackjack

            if dbj and pbj:
                self.end_hand("Push")
                playing = self.fetch_continue()
                continue
            elif dbj and not pbj:
                self.end_hand("You lose. Dealer blackjack")
                playing = self.fetch_continue()
                continue
            elif not dbj and pbj:
                self.end_hand("You win!")
                playing = self.fetch_continue()
                continue

            # no blackjack, now we actually play
            while not self.player.hand > 21:
                if self.player_cont_hand():
                    continue
                break

            if self.player.hand > 21:
                self.end_hand("You lose. Busted")
                playing = self.fetch_continue()
                continue

            # if player still alive, dealer turn
            self.dealer_action()

            if self.dealer.hand > 21:
                self.end_hand('You win! Dealer busted.')
                playing = self.fetch_continue()
                continue

            # eval both hands
            self.hand_over()
            playing = self.fetch_continue()

            # TODO: before new hand is dealt, do check for need to reshuffle (rebuild) deck

        print('\n Game over. \n Thanks for playing! :)')

    def new_round(self):
        """
        do some clean up,
        begin a new hand/round,
        do check for initial blackjack
        """
        self.player.hand.clear()
        self.dealer.hand.clear()

        for i in range(2):
            self.dealer.is_dealt(self.deck.deal())
            self.player.is_dealt(self.deck.deal())

        self.print_hand(dealer=True)
        self.print_hand(dealer=False)

    def hand_over(self):
        """ both hands should not be over 21 when getting here """
        # TODO: include blackjack prop in win condition
        if self.player.hand == self.dealer.hand:

            self.end_hand("Push")
        elif self.player.hand > self.dealer.hand:
            self.end_hand("You win!")
        else:
            self.end_hand("You lose.")

    def player_cont_hand(self, dd=False):
        cstr = "Hit (h) or Stay (s)"
        choice = input(cstr)
        while choice not in ['h', 's']:
            choice = input('Please enter a valid response. `H` or `S`')
        if choice == 'h':
            self.player.is_dealt(self.deck.deal())
            self.print_hand(dealer=False)
            return True
        return False

    def dealer_action(self):
        """ dealer hits on soft 17 """
        while self.dealer.hand <= 17:
            self.dealer.is_dealt(self.deck.deal())

    @staticmethod
    def fetch_continue():
        cont_ = input('Continue? (Y/N):')
        while cont_.lower() not in ["y", "n"]:
            cont_ = input('Please enter a valid response. `Y` or `N`')
        if cont_.lower() == "y":
            return True
        return False

    def print_hand(self, dealer=False):
        """
        fancy print Hand
        :param dealer: boolean -> whether hand to be printed is dealer or not
        """
        if dealer:
            BlackJack.line_print("Dealer's hand")
            print(self.dealer.hand)
        else:
            BlackJack.line_print("Player's hand")
            print(self.player.hand)
            print(f'Hand value of {self.player.hand.value}')
        # finally
        print('\n')

    @staticmethod
    def line_print(text):
        print(f"{'---------' * 3} {text}  {'---------' * 3}")

    @staticmethod
    def end_hand(reason):
        BlackJack.line_print("~~ End of Hand ~~")
        print(reason)
        print('\n')


if __name__ == '__main__':
    BlackJack().main()
