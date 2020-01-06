# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../scripts/player/')

###########################################
## Import the classes from the card file ##
###########################################

from hand import Hand

def test_import():
  assert Hand

def test_hand_instance():
  assert Hand()

