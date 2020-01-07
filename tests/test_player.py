# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/player/')
sys.path.insert(1, myPath + '/../scripts/deck/')


from player import Player, User
from card import Card

def test_import():
  assert Player

def test_player_instance():
  assert Player()

def test_player_score_21():
  user = User()
  user.hit(Card(10))
  user.hit(Card(1))
  assert user.get_score() == 21

def test_2_aces():
  user = User()
  user.hit(Card(1))
  user.hit(Card(1))
  assert user.get_score() == 12

def test_17():
  user = User()
  user.hit(Card(1))
  user.hit(Card(6))
  assert user.get_score() == 17





