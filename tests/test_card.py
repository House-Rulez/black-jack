# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/deck/')

###########################################
## Import the classes from the card file ##
###########################################

from card import Card, Heart, Spade, Diamond, Club

#################################################
## Test the Imports to see if they are working ##
#################################################

def test_import():
  assert Heart
  assert Spade
  assert Diamond
  assert Club

def test_ace_of_spades():
  ace = Spade(1)
  assert isinstance(ace, (Card, Spade))
  assert ace.value == 11
  assert ace.name == 'Ace'

def test_face_card():
  queen = Heart(12)
  assert isinstance(queen, (Card, Heart))
  assert queen.value == 10
  assert queen.name == 'Queen'

