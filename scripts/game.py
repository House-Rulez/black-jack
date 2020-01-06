# import deck.deck.Deck

class Game:
  def __init__(self, print_func=print, input_func=input):
    """
    This is where most of the basic game set up should take place. Namely the creation of the deck as well as the dealer. For now we can also add the player.
    In: None
    Exceptions: None
    Out: None
    """
    # TODO: Make Deck
    # TODO: Make Dealer
		# TODO: Make Player
    # self.deck = Deck()
    self._print = print_func
    self._input = input_func
    self.round = 1

  def play(self):
    """
    Start the game loop as well as any other set up that the user needs
    In: None
    Exceptions: None
    Out:
    """
    self._print('*' * 122)
    self._print('*' * 50 + 'Welcome to Black Jack!' + '*' * 50)
    self._print('*' * 122)
    self._print('You start off with 100 chips. Try to make it to 250 by beating the dealer\'s cards.')
    response = self._input('Would you like to play?: y/n ')

    if response == 'y':
      while True:

        bet_input = int(self._input(f'Round {self.round}: What\'s your bet?: '))

        # if bet_input > self.bank:
        #   print('Bet is over the amount of chips you have.')
        #   bet_input = int(self._input(f'Round {self.round}: What\'s your bet?: '))

        hit_or_stay_input = self._input(f'Round {self.round}: Here are your cards: *visual or string representation of cards*. Here are my Cards: *cards with one face down*-  Do you want to hit or stay?: h/s ')

        while True:

          if hit_or_stay_input == 'h':
            response = self._input(f'**Show card here** Your total is total is **card points here**. Hit or stay?: h/s ')

          if hit_or_stay_input == 's':
            self._print(f'Your total is {self.card_points}')
            break
  
    else:
      print('Okay, come again!')


  def iterate_round(self):
    self.round += 1

  def shuffle_deck(self):
    self.deck.shuffle()

  def turn(self):
    pass

if __name__ == "__main__":
	"""The code that starts the game"""
	game = Game()

	game.play()
