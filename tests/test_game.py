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

# def test_greeting_prompt(game):

#     set_scripts(
#         ['Welcome to Black Jack!', 'You start off with 100 chips. Try to make it to 250 chips by beating against the dealer\'s cards.', 'Your current bank is 100'],
#         ['Would you like to play?: y/n '],
#         ['y']
#     )

#     game.play()



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
