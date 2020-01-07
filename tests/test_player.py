# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, myPath + '/../scripts/player/')
sys.path.insert(1, myPath + '/../scripts/deck/')
import pytest

from player import Player, User
from card import Card

def test_import():
  assert Player

def test_player_instance():
  assert Player()


@pytest.mark.parametrize("test_input_1, test_input_2, expected",
[(Card(10), Card(1), 21),
(Card(1), Card(1), 12),
(Card(1), Card(6), 17)])
def test_score_2_cards(test_input_1, test_input_2, expected):
  user = User()
  user.hit(test_input_1)
  user.hit(test_input_2)
  assert user.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",
[(Card(10), Card(8), Card(9), 27),
(Card(6), Card(5), Card(9), 20),
(Card(1), Card(1), Card(5), 17)])
def test_score_3_cards(test_input_1, test_input_2, test_input_3, expected):
  user = User()
  user.hit(test_input_1)
  user.hit(test_input_2)
  user.hit(test_input_3)
  assert user.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, test_input_4, expected",
[(Card(10), Card(3), Card(5), Card(4), 22),
(Card(6), Card(5), Card(9), Card(1), 21),
(Card(1), Card(1), Card(5), Card(6), 13)])
def test_score_4_cards(test_input_1, test_input_2, test_input_3, test_input_4, expected):
  user = User()
  user.hit(test_input_1)
  user.hit(test_input_2)
  user.hit(test_input_3)
  user.hit(test_input_4)
  assert user.get_score() == expected



