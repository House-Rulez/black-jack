import pytest
from scripts.game import Game

from scripts.deck.card import Card
from scripts.player.player import Dealer, User



# Game instance


def test_game_instance(game):
  """
  An instance of Game can be made.
  """

  assert isinstance(game, Game)


# Game introduction


def test_game_intro_exit(game):
  """
  Can exit from game after introduction.
  """

  prints = [
    'Welcome to Black Jack!',
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
    'Okay, come again!',
  ]

  prompts = [
    'Do you want to play?',
  ]

  inputs = [
    'n',
  ]

  set_scripts(prints, prompts, inputs)

  assert not game.intro()


def test_game_intro(game):
  """
  Can choose to play game after introduction.
  """

  prints = [
    'Welcome to Black Jack!',
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
    'Okay, come again!',
  ]

  prompts = [
    'Do you want to play?',
  ]

  inputs = [
    'y',
  ]

  set_scripts(prints, prompts, inputs)

  assert game.intro()


# Game difficulty

def test_player_chooses_easy_difficulty(game):
  """
  Can start playing on easy difficulty.
  """

  prints = [
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
  ]

  prompts = [
    'Which difficulty do you want to play on?',
  ]

  inputs = [
    'e',
  ]

  set_scripts(prints, prompts, inputs)

  assert game.difficulty_level()
  assert game.starting_bank == 100
  assert game.score_goal == 250


def test_player_chooses_hard_difficulty(game):
  """
  Can start playing on hard difficulty.
  """

  prints = [
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
  ]

  prompts = [
    'Which difficulty do you want to play on?',
  ]

  inputs = [
    'h',
  ]

  set_scripts(prints, prompts, inputs)

  assert game.difficulty_level()
  assert game.starting_bank == 50
  assert game.score_goal == 500


def test_player_chooses_easy_difficulty_extended(game):
  """
  Can start playing on easy difficulty after misspeaking.
  """

  prints = [
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
    'Difficulty must be easy or hard.',
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
  ]

  prompts = [
    'Which difficulty do you want to play on?',
    'Which difficulty do you want to play on?',
  ]

  inputs = [
    't',
    'e'
  ]

  set_scripts(prints, prompts, inputs)

  assert game.difficulty_level()
  assert game.starting_bank == 100
  assert game.score_goal == 250


def test_player_chooses_difficulty_exit(game):
  """
  Can exit game while choosing difficulty level.
  """

  prints = [
    'On easy difficulty you start with 100 chips and try to get to 250 chips.',
    'On hard difficulty you start with 50 chips and try to get to 500 chips.',
  ]

  prompts = [
    'Which difficulty do you want to play on?',
  ]

  inputs = [
    'exit',
  ]

  set_scripts(prints, prompts, inputs)

  assert not game.difficulty_level()


# Game turn iterate_round


def test_increment_round(game):
  """
  Round should be updated each turn.
  """

  game.increment_round()
  assert game.round == 1


# Game turn place_user_bet


def test_player_bet(game):
  """
  Player bets legal amount.
  """

  current_bank = 100

  prints = [

    f'Your current bank is {current_bank}',
    'how much would you like to bet?'
  ]

  prompts = [
    'Bet: '
  ]

  inputs = [
    str(current_bank)
  ]

  set_scripts(prints, prompts, inputs)

  bet = game.place_user_bet(current_bank)
  assert bet == True


def test_player_bet_0(game):
  """
  Player bets 0.
  """

  current_bank = 100
  bet_amount = 0

  prints = [
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
    'Your bet must be greater than 0',
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
  ]

  prompts = [
    'Bet: ',
    'Bet: '
  ]

  inputs = [
    str(bet_amount),
    str(current_bank)
  ]

  set_scripts(prints, prompts, inputs)

  bet = game.place_user_bet(current_bank)
  assert bet == True


def test_player_bet_high(game):
  """
  Player bets more than they have.
  """

  current_bank = 100
  bet_amount = 101

  prints = [
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
    'You can\'t bet more points than you have',
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
  ]

  prompts = [
    'Bet: ',
    'Bet: '
  ]

  inputs = [
    str(bet_amount),
    str(current_bank)
  ]

  set_scripts(prints, prompts, inputs)

  bet = game.place_user_bet(current_bank)
  assert bet == True


def test_player_bet_noninteger(game):
  """
  Player must bet an integer amount.
  """

  current_bank = 100
  bet_amount = 50.5

  prints = [
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
    'Please enter an integer',
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
  ]

  prompts = [
    'Bet: ',
    'Bet: '
  ]

  inputs = [
    str(bet_amount),
    str(current_bank)
  ]

  set_scripts(prints, prompts, inputs)

  bet = game.place_user_bet(current_bank)
  assert bet == True


def test_player_exit(game):
  """
  Player can exit game while making bet.
  """

  current_bank = 100

  prints = [
    f'Your current bank is {current_bank}',
    'how much would you like to bet?',
  ]

  prompts = [
    'Bet: '
  ]

  inputs = [
    'exit'
  ]

  set_scripts(prints, prompts, inputs)

  bet = game.place_user_bet(current_bank)
  assert bet == False


# Game turn user_turn


@pytest.mark.skip
def test_user_turn_exit():
  """
  User can exit game while hitting.
  """
  pass


@pytest.mark.skip
def test_user_turn_stay():
  """
  User can stay and doesn't need to hit.
  """
  # user_hand = [Card(2), Card(10)]
  # dealer_hand = [Card(11), Card(12)]
  # user = User(user_hand)
  # dealer = Dealer(dealer_hand)
  # game = Game(mock_print, mock_input, dealer=dealer_hand, user=user_hand)

  # prints = [
  #   f'The Dealer shows:\n{repr(game.dealer)}\n',
  #   f'Your hand is:\n{str(game.user)}\n',
  # ]

  # prompts =
  pass



@pytest.mark.skip
def test_user_turn_hit():
  """
  User can hit.
  """
  pass


@pytest.mark.skip
def test_user_turn_bad_input():
  """
  User hit or stay input must be legal.
  """
  pass


#################################################
## Below code is for helping out tests above ####
#################################################

@pytest.fixture()
def game():
  game = Game(mock_print, mock_input)
  return game

scripts = {
  'prints': [],
  'prompts': [],
  'inputs': [],
}

def set_scripts(prints=[], prompts=[],inputs=[]):
  scripts['prints'] = prints
  scripts['prompts'] = prompts
  scripts['inputs'] = inputs

def mock_print(msg, *args):
  if len(scripts['prints']):
    assert scripts['prints'].pop(0) == msg

def mock_input(prompt, *args):
  if len(scripts['prompts']):
    assert prompt == scripts['prompts'].pop(0)

  if len(scripts['inputs']):
    return scripts['inputs'].pop(0)
