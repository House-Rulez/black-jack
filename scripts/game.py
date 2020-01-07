# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/./deck/')
sys.path.insert(1, myPath + '/./player/')

import re
from deck import Deck
from player import User, Dealer

class Game:
  def __init__(self, print_func=print, input_func=input):
    """
    This is where most of the basic game set up should take place. Namely the creation of the deck as well as the dealer. For now we can also add the player.
    In: None
    Exceptions: None
    Out: None
    """
    self.dealer = Dealer()
    self.deck = Deck()
    self.user = User()
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
    self._print('You start off with 100 chips. Try to make it to 250 chips by beating the dealer\'s cards.')
    response = self._input('Would you like to play?: y/n ')

    if response == 'y':
      while self.user.get_bank() > 0 and self.user.get_bank() < 250:
        self.turn()
    else:
      print('Okay, come again!')

  def iterate_round(self):
    """
    Keeps track of round number
    In: None
    Out: None
    """
    self.round += 1

  def shuffle_deck(self):
    """
    Shuffles decks of cards
    In: None
    Out: None
    """
    self.deck.shuffle()

  def turn(self):
    """
    Runs through a turn of the game
    In: None
    Out: None
    """
    self.place_user_bet()
    self.deal()
    self.user_turn()
    if self.user.bust():
      print(f'Your score is {self.user.get_score()}')
      print('You have bust')
      self.user.beat_dealer(False)
    else:
      self.dealer_turn()
      print('The Dealer\'s hand: ')
      print(str(self.dealer))
      print(f'Dealer has {self.dealer.get_score()} points')
      result = self.user.get_score() > self.dealer.get_score() or self.dealer.bust()
      self.user.beat_dealer(result)
      if self.dealer.bust():
        print('The Dealer bust')
      if result:
        print('You beat the Dealer')
      else:
        print('You lost this hand')
    self.reset_hands()
    self.deck.shuffle()


  def place_user_bet(self):
    """
    Shows current bank, requests bet, handles edge cases
    In: None
    Out: None
    """
    current_bank = self.user.get_bank()

    while True:
      print(f'Your current bank is {current_bank}')
      print('how much would you like to bet?')
      player_bet = input('Bet: ')

      if re.match(r'[0-9]+', player_bet):
        player_bet = int(player_bet)

        if player_bet >= 1 and player_bet <= current_bank:
          self.user.place_bet(player_bet)
          break

        elif player_bet == 0:
          print('Please enter a valid bet')

        else:
          print('Bet is over current bank')

      else:
        print('Please enter an integer')


  def deal(self):
    """
    Deals 2 cards each for user and dealer
    In: None
    Out: None
    """
    for _ in range(0, 2):
      self.user.hit(self.deck.deal())
      self.dealer.hit(self.deck.deal())


  def user_turn(self):
    """
    Handles user turn
    In: None
    Out: None
    """
    while not self.user.bust():
      print(f'The Dealer shows {repr(self.dealer)}')
      print(str(self.user))
      print('Your current score is ', self.user.get_score())
      hit_or_stay_input = input('Would you like to hit or stay? (h/s): ')
      if hit_or_stay_input == 's':
        break
      elif hit_or_stay_input == 'h':
        self.user.hit(self.deck.deal())
      else:
        print('invalid input')

  def dealer_turn(self):
    """
    Handles dealer turn
    In: None
    Out: None
    """
    while not self.dealer.bust():
      if self.dealer.get_score() < 17 :
        self.dealer.hit(self.deck.deal())
      else:
        break

  def reset_hands(self):
    """
    Resets hands of all players to no cards
    In: None
    Out: None
    """
    self.user.reset_hand()
    self.dealer.reset_hand()

  def save_game(self):
    """
    Description
    In: None
    Exceptions: No Data To Save
    Out: .csv files
    """
    # Call the other to csv functions


if __name__ == "__main__":
	"""The code that starts the game"""
	game = Game()

	game.play()
