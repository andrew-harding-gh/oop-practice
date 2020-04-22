from oop_blackjack.decks import CasinoDeck
from oop_blackjack.players import Dealer, Player


# TODO: add flags for verbosity of game (eg. removing suites)
# TODO: add initial print statement about when the dealer will be forced to hit/stay
# TODO: double down (split on identical cards)
# TODO: double (take one card and double bet)
# TODO: surrender (lose half bet)
# TODO: insurance (dealer has ace face up)

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
            # first deal
            for i in range(2):
                self.dealer.is_dealt(self.deck.pick()[0])
                self.player.is_dealt(self.deck.pick()[0])

            self.print_hand(dealer=True)
            self.print_hand(dealer=False)

            # blackjack check
            d = self.dealer.hand == 21
            p = self.player.hand == 21

            if d and p:
                self.pushed()
                playing = self.fetch_continue()
                continue
            elif d and not p:
                self.d_win()
                playing = self.fetch_continue()
                continue
            elif p and not d:
                self.p_win()
                playing = self.fetch_continue()
                continue

            # no blackjack, now we actually play
            while not self.player.hand > 21:
                if self.player_cont_hand():
                    continue
                break

            print('boop')

            if self.player.hand > 21:
                BlackJack.line_print('End of Hand')
                print('You bust :(')
                playing = self.fetch_continue()
                continue

            # if player still alive, dealer turn
            self.dealer_action()

            if self.dealer.hand > 21:
                BlackJack.line_print('End of Hand')
                print('Dealer bust. You win!')
                playing = self.fetch_continue()
                continue

            # eval both hands
            self.hand_over()

            # TODO: before new hand is dealt, do check for need to reshuffle (rebuild) deck

        print('\n Game over. \n Thanks for playing! :)')

    def hand_over(self):
        """ both hands should not be over 21 when getting here """
        if self.player.hand == self.dealer.hand:
            self.pushed()
        elif self.player.hand > self.dealer.hand:
            self.p_win()
        self.d_win()

    def player_cont_hand(self, dd=False):
        cstr = "Hit (h) or Stay (s)"
        choice = input(cstr)
        while choice not in ['h', 's']:
            choice = input('Please enter a valid response. `H` or `S`')
        if choice == 'h':
            self.player.is_dealt(self.deck.pick()[0])
            self.print_hand(dealer=False)
            return True
        return False

    def dealer_action(self):
        """ dealer hits on soft 17 """
        while self.dealer.hand <= 17:
            self.dealer.is_dealt(self.deck.pick()[0])

    def fetch_continue(self):
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

    @staticmethod
    def line_print(text):
        print(f"{'---------' * 3} {text}  {'---------' * 3}")

    @staticmethod
    def pushed():
        BlackJack.line_print("End of Hand")
        print("Push")

    @staticmethod
    def p_win():
        BlackJack.line_print("End of Hand")
        print("You win! :)")

    @staticmethod
    def d_win():
        BlackJack.line_print("End of Hand")
        print("You win! :)")


if __name__ == '__main__':
    BlackJack().main()
