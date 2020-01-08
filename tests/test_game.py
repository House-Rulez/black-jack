# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/')

from game import Game
import pytest


def test_import():
  assert Game

def test_game_instance():
  assert Game()

def test_player_chooses_easy_difficulty(game):
  prints = [
    'Welcome to Black Jack!', 
    'You start off with a certain aount of chips (50 or 100) depending on the difficulty level. Try to make it to (250 or 500) chips by beating against the dealer\'s cards.',
    'Your current bank is 100',
    'how much would you like to bet?'
  ]

  prompts = [
    'Would you like to play?: y/n ',
    'Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): ',
    'Bet: '
  ]

  inputs = ['y', 'e', 'exit']

  set_scripts(prints, prompts, inputs)

  with pytest.raises(SystemExit) as e:
    game.play()


def test_player_chooses_hard_difficulty(game):
  prints = [
    'Welcome to Black Jack!', 
    'You start off with a certain aount of chips (50 or 100) depending on the difficulty level. Try to make it to (250 or 500) chips by beating against the dealer\'s cards.',
    'Your current bank is 50',
    'how much would you like to bet?'
  ]

  prompts = [
    'Would you like to play?: y/n ',
    'Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): ',
    'Bet: '
  ]

  inputs = ['y', 'h', 'exit']

  set_scripts(prints, prompts, inputs)

  with pytest.raises(SystemExit) as e:
    game.play()


def test_player_chooses_easy_difficulty_extended(game):
  prints = [
    'Welcome to Black Jack!', 
    'You start off with a certain aount of chips (50 or 100) depending on the difficulty level. Try to make it to (250 or 500) chips by beating against the dealer\'s cards.',
    'Difficulty must be Easy or Hard',
    'Your current bank is 100',
    'how much would you like to bet?',
  ]

  prompts = [
    'Would you like to play?: y/n ',
    'Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): ',
    'Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): ',
    'Bet: '
  ]

  inputs = ['y', 't', 'e', 'exit']

  set_scripts(prints, prompts, inputs)

  with pytest.raises(SystemExit) as e:
    game.play()

def test_player_chooses_difficulty_exit(game):
  prints = [
    'Welcome to Black Jack!', 
    'You start off with a certain aount of chips (50 or 100) depending on the difficulty level. Try to make it to (250 or 500) chips by beating against the dealer\'s cards.',
  ]

  prompts = [
    'Would you like to play?: y/n ',
    'Which difficulty? \nEasy: start with 100 chips, and goal is 250 chips \nHard: start with 50 chips, and goal is 500 chips \nPress (e) or (h): '
  ]

  inputs = ['y', 'exit']

  set_scripts(prints, prompts, inputs)

  with pytest.raises(SystemExit) as e:
    game.play()

#################################################
## Below code is for helping out tests above ####
#################################################

scripts = {
    'prints' : [],
    'prompts' : [],
    'inputs' : [],
}

@pytest.fixture()
def game():
    play = Game(mock_print, mock_input)
    return play

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
