# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/./')

from collections import deque
from random import randint


from card import Spade, Heart, Diamond, Club



class Deck:
  """
  This class is used to store the set of cards that are being used in this game.
  Methods:

  __init__():
  Creates New Deck

  shuffle():
  Reshuffles Deck

  deal():
  Returns card instence

  cards_remaining():
  Returns # of cards that havn't been delt

  deck_size():
  Returns the total # of cards
  """

  def __init__(self, deck_count = 2):
    self.deck_count = deck_count
    self.cards_delt = 0
    # Creates an instencce of a list for the creating of a new deck. Will later be reassigned to a queue to play with instead
    self.deck = []

    # Populate the Deck and shuffle the cards the deck should now be a Queue
    self._create_deck()
    self.shuffle()


  #################
  ## Queue Class ##
  #################


  # The deck mostly uses a queue to
  class Queue:
    """Used to create a Queue of cards that will be used for dealing out the cards from the deck"""
    def __init__(self):
      self._dq = deque()

    def enqueue(self, card):
      self._dq.appendleft(card)

    def dequeue(self):
      return self._dq.pop()

    def is_empty(self):
      return len(self._dq) == 0

    def __len__(self):
      return len(self._dq)


  def _get_queue(self):
    """Hidden Method to get the Queue Class that is used to store the deck
    Will return a reference to the entire class. Mainly used for testing of the deck"""
    return self.Queue


  #############
  ## Methods ##
  #############


  def _create_deck(self):
    """
    **Do Not Use Outside Class**
    Takes in no input into the function and creates an instence of each card type between 1 and 13
    In: Empty list
    Exceptions: None
    Out: List with
    """
    # We are useing 2 decks so %13+1 will keep the cards in range
    for i in range(0, (13 * self.deck_count)):
      card_value = (i % 13) + 1
      self.deck.append(Spade(card_value))
      self.deck.append(Heart(card_value))
      self.deck.append(Diamond(card_value))
      self.deck.append(Club(card_value))


  def shuffle(self):
    """
    Can Work with either a list or a queue. Converst the deck to a list. Randomly selects a card from the deck and adds it to the Queue
    In: the deck as either a List or Queue
    Exceptions: None
    Out: Reassign the deck to be a Queue
    """
    if not isinstance(self.deck, list):
      self._to_list()

    self.cards_delt = 0

    q = self.Queue()
    while len(self.deck) > 0:
      index = randint(0, len(self.deck)-1)
      value = self.deck.pop(index)
      q.enqueue(value)

    self.deck = q


  def _to_list(self):
    """
    Used when the deck is still a Queue to convert it back to a list
    In: Deck needs to currently be a Queue
    Exceptions: Error if the deck is not a Queue at the time
    Out: Sets the Deck to be a List
    """
    if not isinstance(self.deck, self.Queue):
      raise TypeError

    lst = []
    while not self.deck.is_empty():
      lst.append(self.deck.dequeue())
    self.deck = lst


  def deal(self):
    """

    In: None
    Exceptions: If all cards have been delt with out shuffling raise Error
    Out: An instence of a card
    """

    if self.cards_remaining() == 0:
      raise EmptyDeckError

    card = self.deck.dequeue()
    self.cards_delt += 1

    # The way the deck is set up it would slowly break the game to loose a card each time it's delt instead the number of cards delt is saved instead
    self.deck.enqueue(card)
    return card


  def cards_remaining(self):
    """
    Used to tell you how many cards in the have yet to be delt
    In: None
    Exceptions: None
    Out: Number of cards that havn't been delt yet
    """
    return (52 * self.deck_count) - self.cards_remaining


  def deck_size(self):
    """
    Tells you the size of the entire deck the game is played with
    In: None
    Exceptions: None
    Out: Number of cards that havn't been delt yet
    """
    return len(self.deck)

###################
## Unique Errors ##
###################

class EmptyDeckError(IndexError):
  pass
