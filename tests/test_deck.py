# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/deck/')
sys.path.insert(1, myPath + '/../scripts/dealer/')
sys.path.insert(2, myPath + '/../scripts/player/')

import pytest

###########################################
## Import the classes from the card and player file ##
###########################################

from deck import Deck
from player import User, Dealer
from card import Card

#################################################
## Test the Imports to see if they are working ##
#################################################

@pytest.fixture()
def deck():
    return Deck()

@pytest.fixture()
def user():
    return User()

def test_import():
  assert deck

def test_deck_size(deck):
  assert deck.deck_size() == 104

def test_cards_remaining(deck, user):
  for _ in range(0, 52):
    deck.deal()
  expected = 52
  actual = deck.cards_remaining()
  assert expected == actual

def test_cards_remaining_two(deck, user):
  for _ in range(0, 103):
    deck.deal()
  expected = 1
  actual = deck.cards_remaining()
  assert expected == actual
