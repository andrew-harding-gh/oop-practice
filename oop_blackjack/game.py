from oop_blackjack.decks import CasinoDeck
from oop_blackjack.players import BlackJackPlayer


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
        self.dealer = BlackJackPlayer()
        self.player = BlackJackPlayer()

    def main(self):
        playing = True
        while playing:
            self.new_round()

            if self.blackjack_is_present():
                playing = self.player_keep_playing()
                continue

            self.player_turn()
            if self.player.hand.busted:
                self.end_round("You lose. Busted")
                playing = self.player_keep_playing()  # TODO: instead of asking for a player input every turn, allow for `QQ` input to kill game
                continue

            self.dealer_turn()

            # finally, eval both hands
            self.hand_over()
            playing = self.player_keep_playing()

        print('\n Game over. \n Thanks for playing! :)')

    def blackjack_is_present(self):
        """ if either player has a blackjack, round ends -> return True """

        dbj = self.dealer.hand.blackjack
        pbj = self.player.hand.blackjack

        if dbj and pbj:
            self.end_round("Push on double Blackjack")
        elif dbj:
            self.end_round("You lose. Dealer blackjack")
        elif pbj:
            self.end_round("Blackjack! You win!")

        return dbj or pbj

    def player_turn(self):
        """
        player can begin actions after both hands are checked for blackjack;
        ie. all hands in play are < 21
        """

        player_continues = True

        while player_continues:
            choice = input("Hit (h) or Stay (s)").lower()

            while choice not in ['h', 's']:
                choice = input('Please enter a valid response. `H` or `S`')

            if choice == 'h':
                self.player.is_dealt(self.deck.deal_top_card())
                self.print_hand(self.player.hand)

                if self.player.hand >= 21:
                    player_continues = False

            elif choice == 's':
                player_continues = False

    def new_round(self):
        """
        check if deck needs shuffling,
        do some clean up,
        begin a new hand/round,
        do check for initial blackjack,
        """
        if self.deck.percent_remain <= 75:
            print('\n ~~ Reshuffling deck. ~~ \n')
            self.deck = CasinoDeck(self.deck.num_decks)

        self.player.hand.clear()
        self.dealer.hand.clear()

        for i in range(2):
            self.dealer.is_dealt(self.deck.deal_top_card())
            self.player.is_dealt(self.deck.deal_top_card())

        self.print_hand(self.dealer.hand, dealer=True)
        self.print_hand(self.player.hand)

    def hand_over(self):
        if self.dealer.hand.busted:
            self.end_round('You win! Dealer busted.')
            return

        if self.player.hand == self.dealer.hand:
            self.end_round("Push")
        elif self.player.hand > self.dealer.hand:
            self.end_round("You win!")
        else:
            self.end_round("You lose.")

    def dealer_turn(self):
        """ dealer hits on soft 17 """
        while self.dealer.hand <= 17:
            self.dealer.is_dealt(self.deck.deal_top_card())

    @staticmethod
    def player_keep_playing():
        cont_ = input('Continue? (Y/N):')
        while cont_.lower() not in ["y", "n"]:
            cont_ = input('Please enter a valid response. `Y` or `N`')
        return True if cont_.lower() == "y" else False

    @staticmethod
    def print_hand(hand, dealer=False):
        """
        fancy print Hand
        :param hand: Hand instance to be printed -> Hand;
        :param dealer: switch for hiding first card -> boolean;
        """

        print('\n')
        if dealer:
            BlackJack.line_print("Dealer's hand")
            print(hand.dealer_repr())
            print(f'Hand value of {hand.value}')
        else:
            BlackJack.line_print("Your hand")
            print(hand)
            print(f'Hand value of {hand.value}')
        # finally
        print('\n')

    @staticmethod
    def line_print(text):
        print(f"{'---------' * 3} {text}  {'---------' * 3}")

    def end_round(self, reason):
        BlackJack.line_print("~~ End of Hand ~~")
        print(reason)
        print(f'Dealer had {self.dealer.hand.value}')
        print(f'You had {self.player.hand.value}')
        print('\n')


if __name__ == '__main__':
    BlackJack().main()
