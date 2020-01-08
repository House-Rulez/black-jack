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

  # Used to give the user different options for answering prompts
  _valid_exit = {'exit', 'exit()', 'leave', 'quit'}
  _valid_yes = {'y', 'yes', 'yeah', 'ok', 'sure'}
  _valid_hit = {'h', 'hit', 'deal', 'hit me'}
  _valid_stay = {'s', 'stay', 'stop'}


  def __init__(self, print_func=print, input_func=input):
    """
    This is where most of the basic game set up should take place. Namely the creation of the deck as well as the dealer. For now we can also add the player.
    In: None
    Exceptions: None
    Out: None
    """
    # Variables to control both the users starting bank as well as their goal
    self.starting_bank = 100
    self.score_goal = 250

    # Override functions so you can create a wrapper around the program
    self._print = print_func
    self._input = input_func

    # Create a new deck of cards
    self.deck = Deck(deck_count=2)

    # Add the players that the game cares about
    self.dealer = Dealer()
    self.user = User(starting_bank = self.starting_bank)
    self.round = 0

  def play(self):
    """
    Start the game loop as well as any other set up that the user needs
    In: None
    Exceptions: None
    Out:
    """
    print('\n')
    self._print('Welcome to Black Jack!')
    print('\n')
    self._print(f'You start off with a certain aount of chips (50 or 100) depending on the difficulty level. Try to make it to (250 or 500) chips by beating against the dealer\'s cards.')
    print('\n')
    response = self._input('Would you like to play?: y/n ')

    self.difficulty_level()

    if response.lower() in self._valid_yes:

      # Run the game loop
      while self.user.get_bank() > 0 and self.user.get_bank() < self.score_goal:
        self.turn()
        if self.deck.deck_size() / 4 > self.deck.cards_remaining():
          self.deck.shuffle()

      if self.user.get_bank() >= self.score_goal:
        self.start_endless()

      if self.user.get_bank() <= 0:
        if self.user.get_max_bank() <= self.starting_bank:
          self._print(f'You had no net gain over {self.round} rounds.')
        else:
          self._print(f'You amassed a max of {self.user.get_max_bank()} points over {self.round} rounds.')

    else:
      self._print('Okay, come again!')

    exit_game()


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

      if level_response.lower() in self._valid_exit:
        exit_game()

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


  def start_endless(self):
    """
    This mode is made an option once the user passes the point where they have more points the the goal. It allows them to play until they go broke.
    In: None
    Out: None
    """
    self._print(f'You have beat the table in {self.round} hands')
    response = self._input(f'You have {self.user.get_bank()} points. Would you like to continue? (y/n) ')
    if response.lower() in self._valid_yes:
      while self.user.get_bank() > 0:
        self.turn()
        if self.deck.deck_size() / 4 > self.deck.cards_remaining():
          self.deck.shuffle()


  def turn(self):
    """
    Runs through a turn of the game
    In: None
    Out: None
    """
    self.iterate_round()

    self.place_user_bet()
    self.deal()
    self.user_turn()

    self.dealer_turn()

    self.calculate_winner()

    self.reset_hands()


  def place_user_bet(self):
    """
    Shows current bank, requests bet, handles edge cases
    In: None
    Out: None
    """
    current_bank = self.user.get_bank()

    while True:
      print('\n')
      self._print(f'Your current bank is {current_bank}')
      self._print('how much would you like to bet?')
      player_bet = self._input('Bet: ')

      # If the player wants to exit they can
      if player_bet.lower() in self._valid_exit:
        exit_game()

      if re.match(r'\s*[0-9]+\s*$', player_bet):
        player_bet = int(player_bet)

        if player_bet >= 1 and player_bet <= current_bank:
          self.user.place_bet(player_bet)
          break

        elif player_bet == 0:
          self._print('Your bet must be greater than 0')

        else:
          self._print('You can\'t bet more points than you have')

      else:
        self._print('Please enter an integer')


  def deal(self):
    """
    Deals 2 cards to the user and dealer
    In: None
    Out: None
    """
    for _ in range(0, 2):
      self.user.hit(self.deck.deal())
      self.dealer.hit(self.deck.deal())


  def user_turn(self):
    """
    Handles the users decision to either hit and gain a card, or to stay and keep the cards they have.
    In: None
    Out: None
    """
    while not self.user.bust():
      self.save_game()
      print('\n')
      self._print(f'The Dealer shows:\n{repr(self.dealer)}\n')
      self._print(f'Your hand is:\n{str(self.user)}\n')
      self._print('Your current score is ', self.user.get_score())
      hit_or_stay_input = self._input('Would you like to hit or stay? (h/s): ')

      # If the player wants to exit they can
      if hit_or_stay_input.lower() in self._valid_exit:
        exit_game()

      if hit_or_stay_input.lower() in self._valid_stay:
        return
      elif hit_or_stay_input in self._valid_hit:
        self.user.hit(self.deck.deal())
      else:
        self._print('invalid input')



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
    print('\n')
    self._print(f'Your last hand is:\n{str(self.user)}')
    self._print(f'Your score is {self.user.get_score()}')
    if self.user.bust():
      self._print('You have bust')
      self.user.beat_dealer(False)

    else:
      self._print(f'The Dealer\'s hand is:\n{str(self.dealer)}')
      self._print(f'Dealer has {self.dealer.get_score()} points')
      if self.user.get_score() == self.dealer.get_score() and not self.dealer.bust():
        self._print(f'It was a tie\nYou don\'t gain or lose points')
        return

      result = self.user.get_score() > self.dealer.get_score() or self.dealer.bust()
      self.user.beat_dealer(result)
      if self.dealer.bust():
        self._print('The Dealer bust')
      if result:
        self._print('You beat the Dealer')
      else:
        self._print('You lost this hand')


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


def exit_game():
  """
  Allows the program to safely exit the program while running
  """
  sys.exit()


if __name__ == "__main__":
	"""The code that starts the game"""
	game = Game()

	game.play()
