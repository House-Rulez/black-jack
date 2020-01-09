# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/./deck/')
sys.path.insert(1, myPath + '/./player/')


import re
from deck import Deck
from player import User, Dealer

class Game:
  """
  This is the main controller for Black Jack. It handles the creation of the Deck, Dealer, and User.
  As well as managing the main parts of the game flow.
  """

  def __init__(self, print_func=print, input_func=input):
    """
    This is where most of the basic game set up should take place. Namely the creation of the deck as well as the dealer. For now we can also add the player.
    In: None
    Exceptions: None
    Out: None
    """
    # Variables to control both the users starting bank as well as their goal
    self.starting_bank = 270
    self.score_goal = 250
    self.endless = False

    # Override functions so you can create a wrapper around the program
    self._print = print_func
    self._input = input_func

    # Create a new deck of cards
    self.deck = Deck(deck_count=2)

    # Add the players that the game cares about
    self.dealer = Dealer()
    self.user = User(starting_bank = self.starting_bank)
    self.round = 0


  def difficulty_level(self):
    valid_easy_responses = {'e', 'easy'}
    valid_hard_responses = {'h', 'hard'}
    while True:
      level_response = self._input('Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): ')

      if level_response.lower() in valid_easy_responses:
        self.user = User(starting_bank = 100)
        self.score_goal = 250
        break

      if level_response.lower() in valid_hard_responses:
        self.user = User(starting_bank = 50)
        self.score_goal = 500
        break

      self._print('Difficulty must be Easy or Hard')


  def iterate_round(self):
    """
    Increment the round number
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


  def place_user_bet(self, value):
    """
    Shows current bank, requests bet, handles edge cases
    In: None
    Out: None
    """
    current_bank = self.user.get_bank()

    if value >= 1 and value <= current_bank:
      self.user.place_bet(value)


  def deal(self):
    """
    Deals 2 cards to the user and dealer
    In: None
    Out: None
    """
    for _ in range(0, 2):
      self.user.hit(self.deck.deal())
      self.dealer.hit(self.deck.deal())
    self.save_game()

  def user_hand(self):
    return self.user.hand

  def dealer_hand(self):
    return self.dealer.hand

  def user_hit(self):
    """
    Handles the users decision to either hit and gain a card, or to stay and keep the cards they have.
    In: None
    Out: None
    """
    self.user.hit(self.deck.deal())
    self.save_game()



  def dealer_turn(self):
    """
    Controls the dealers logic if they need to hit again or keep the cards that they already have
    In: None
    Out: None
    """
    while not self.dealer.bust():
      if self.dealer.get_score() < 17 :
        self.dealer.hit(self.deck.deal())
      else:
        break


  def calculate_winner(self):
    """
    ** WIP **
    Used to decide if the player or the dealer is the one to win the round
    In: None
    Out: Changes the value in the Player's bank
    """

    if self.user.bust():
      self.user.beat_dealer(False)
      return False

    else:
      if self.user.blackjack() and not self.dealer.blackjack():
        self.user.beat_dealer(True)
        return True

      if not self.user.blackjack() and self.dealer.blackjack():
        self.user.beat_dealer(False)
        return False

      if self.user.get_score() == self.dealer.get_score() and not self.dealer.bust():

        return None

      result = self.user.get_score() > self.dealer.get_score() or self.dealer.bust()
      self.user.beat_dealer(result)

      return result



  def reset_hands(self):
    """
    Resets hands of all players to contain no cards
    In: None
    Out: None
    """
    self.user.reset_hand()
    self.dealer.reset_hand()


  def save_game(self):
    """
    Calls on the player and the deck to save their respective cards to the csv files for the notebook.
    In: None
    Exceptions: No Data To Save
    Out: .csv files
    """
    self.user.to_csv()
    self.deck.to_csv()

