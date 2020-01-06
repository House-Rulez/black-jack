# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/')


from game import Game

def test_import():
  assert Game

def test_game_instance():
  assert Game()

# def test_round_start():
#   game = Game()
#   assert game.play()
