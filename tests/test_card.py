# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/deck/')

import pytest

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


def test_number_card9():
  nine = Club(9)
  assert isinstance(nine, (Card, Club))
  assert nine.value == 9
  assert nine.name == '9'

def test_number_card8():
  eight = Diamond(8)
  assert isinstance(eight, (Card, Diamond))
  assert eight.value == 8
  assert eight.name == '8'

def test_number_card7():
  seven = Spade(7)
  assert isinstance(seven, (Card, Spade))
  assert seven.value == 7
  assert seven.name == '7'

def test_number_card6():
  six = Heart(6)
  assert isinstance(six, (Card, Heart))
  assert six.value == 6
  assert six.name == '6'

def test_number_card5():
  five = Club(5)
  assert isinstance(five, (Card, Club))
  assert five.value == 5
  assert five.name == '5'

def test_number_card4():
  four = Diamond(4)
  assert isinstance(four, (Card, Diamond))
  assert four.value == 4
  assert four.name == '4'

def test_number_card3():
  three = Spade(3)
  assert isinstance(three, (Card, Spade))
  assert three.value == 3
  assert three.name == '3'

def test_number_card2():
  two = Heart(2)
  assert isinstance(two, (Card, Heart))
  assert two.value == 2
  assert two.name == '2'
