# https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, myPath + '/../scripts/player/')
sys.path.insert(1, myPath + '/../scripts/deck/')
sys.path.insert(2, myPath + '/../scripts/dealer/')
import pytest

from player import Player, User, Dealer
from card import Card

@pytest.fixture()
def player():
    return Player()

@pytest.fixture()
def user():
    return User()

@pytest.fixture()
def dealer():
    return Dealer()

@pytest.fixture()
def card():
    return Card()

def test_import_player():
  assert Player

def test_player_instance():
  assert Player()

def test_import_dealer():
  assert Dealer

def test_dealer_instance():
  assert Dealer()

def test_import_user():
  assert User

def test_dealer_instance():
  assert User()

def test_import_card():
  assert Card

def test_card_instance():
  assert Card(1)


#User Tests
@pytest.mark.parametrize("test_input_1, test_input_2, expected",
[(Card(10), Card(1), 21),
(Card(1), Card(1), 12),
(Card(1), Card(6), 17)])
def test_score_player_2_cards(test_input_1, test_input_2, expected, user):
  user.hit(test_input_1)
  user.hit(test_input_2)
  assert user.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",
[(Card(10), Card(8), Card(9), 27),
(Card(6), Card(5), Card(9), 20),
(Card(1), Card(1), Card(5), 17)])
def test_score_player_3_cards(test_input_1, test_input_2, test_input_3, expected, user):
  user.hit(test_input_1)
  user.hit(test_input_2)
  user.hit(test_input_3)
  assert user.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, test_input_4, expected",
[(Card(10), Card(3), Card(5), Card(4), 22),
(Card(6), Card(5), Card(9), Card(1), 21),
(Card(1), Card(1), Card(5), Card(6), 13)])
def test_score_player_4_cards(test_input_1, test_input_2, test_input_3, test_input_4, expected, user):
  user.hit(test_input_1)
  user.hit(test_input_2)
  user.hit(test_input_3)
  user.hit(test_input_4)
  assert user.get_score() == expected

@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, test_input_4, expected",
[(Card(10), Card(3), Card(5), Card(7), True),
(Card(6), Card(5), Card(9), Card(1), False),
(Card(10), Card(1), Card(5), Card(6), True)])
def test_user_bust(test_input_1, test_input_2, test_input_3, test_input_4, expected, user):
  user.hit(test_input_1)
  user.hit(test_input_2)
  user.hit(test_input_3)
  user.hit(test_input_4)
  assert user.bust() == expected

@pytest.mark.parametrize("test_input_1, test_input_2,expected",
[(Card(10), Card(11), True and len(User().hand) == 2),
(Card(10), Card(10), False and len(User().hand) == 2)])
def test_user_blackjack(test_input_1, test_input_2,expected, user):
  user.hit(test_input_1)
  user.hit(test_input_2)
  assert user.blackjack() == expected

def test_user_reset_hand(user):
  assert user.reset_hand() == None

def test_get_bank(user):
  user.bank = 100
  actual = user.get_bank()
  assert user.bank == actual

def test_get_bet_and_place_bet(user):
  user.place_bet(100)
  actual = user.get_bet()
  assert user.bank == actual

#Dealer Tests
@pytest.mark.parametrize("test_input_1, test_input_2, expected",
[(Card(10), Card(1), 21),
(Card(1), Card(1), 12),
(Card(1), Card(6), 17)])
def test_score_dealer_2_cards(test_input_1, test_input_2, expected, dealer):
  dealer.hit(test_input_1)
  dealer.hit(test_input_2)
  assert dealer.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, expected",
[(Card(10), Card(8), Card(9), 27),
(Card(6), Card(5), Card(9), 20),
(Card(1), Card(1), Card(5), 17)])
def test_score_dealer_3_cards(test_input_1, test_input_2, test_input_3, expected, dealer):
  dealer.hit(test_input_1)
  dealer.hit(test_input_2)
  dealer.hit(test_input_3)
  assert dealer.get_score() == expected


@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, test_input_4, expected",
[(Card(10), Card(3), Card(5), Card(4), 22),
(Card(6), Card(5), Card(9), Card(1), 21),
(Card(1), Card(1), Card(5), Card(6), 13)])
def test_score_dealer_4_cards(test_input_1, test_input_2, test_input_3, test_input_4, expected, dealer):
  dealer.hit(test_input_1)
  dealer.hit(test_input_2)
  dealer.hit(test_input_3)
  dealer.hit(test_input_4)
  assert dealer.get_score() == expected

@pytest.mark.parametrize("test_input_1, test_input_2, test_input_3, test_input_4, expected",
[(Card(10), Card(3), Card(5), Card(7), True),
(Card(6), Card(5), Card(9), Card(1), False),
(Card(10), Card(1), Card(5), Card(6), True)])
def test_dealer_bust(test_input_1, test_input_2, test_input_3, test_input_4, expected, dealer):
  dealer.hit(test_input_1)
  dealer.hit(test_input_2)
  dealer.hit(test_input_3)
  dealer.hit(test_input_4)
  assert dealer.bust() == expected

@pytest.mark.parametrize("test_input_1, test_input_2,expected",
[(Card(10), Card(11), True and len(User().hand) == 2),
(Card(10), Card(10), False and len(User().hand) == 2)])
def test_dealer_blackjack(test_input_1, test_input_2,expected, dealer):
  dealer.hit(test_input_1)
  dealer.hit(test_input_2)
  assert dealer.blackjack() == expected

def test_user_reset_hand(dealer):
  assert dealer.reset_hand() == None
