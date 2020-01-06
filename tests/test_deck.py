# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/deck/')

###########################################
## Import the classes from the card file ##
###########################################

from deck import Deck

#################################################
## Test the Imports to see if they are working ##
#################################################

def test_import():
  assert Deck

def test_deck_creation():
  assert Deck
  new_deck = Deck()
  assert new_deck.deck
  assert len(new_deck.deck) == 104
