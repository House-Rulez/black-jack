import csv

class Player:
  """
  This is the parent class for both the user and the dealer. It handles most of the function of the hand of cards that each player has.

  __str__()
  Returns the string value of the users cards that appears as a list

  hit(card)
  takes in a card and adds it to the player's hand

  get_score()
  Returns the current score of the persons hand

  blackjack()
  Returns true or false based on if the player has 21 points in just 2 cards

  bust()
  Returns true or false depending on if the player's hand is over 21

  reset_hand()
  Removes all cards from the player's hand
  """

  def __init__(self):
    self.hand = []
    self._bust = False


  def hit(self, card):
    """
    Takes in a card and adds it to the players hand
    In: Card instance
    Exceptions: None
    Out: None
    """
    self.hand.append(card)


  def __str__(self):
    """
    Creates a string representing the cards in the players hand.
    In: None
    Out: String
    """
    output = '['
    for card in self.hand:
      if not output == '[':
        output += ', '
      output += str(card)
    return output + ']'

  def __repr__(self):
    return str(self)

  def get_score(self):
    """
    Calculates the highest scoring hand for the user
    In: None
    Exceptions: Empty Hand Raises Error
    Out: Current Score of the players hand
    """
    if len(self.hand) == 0:
      raise EmptyHandError

    score = 0
    aces = 0
    for card in self.hand:
      if card.name == 'Ace':
        aces += 1
      else:
        score += card.value

    for ace in range(0, aces):
      if score + 11 <= 21:
        if score + 11 <= 21 and ace == aces - 1:
          score += 11
        else:
          score += 1
      else:
        score += 1

    return score


  def blackjack(self):
    """
    Description
    In: None
    Out: True / False
    """
    return len(self.hand) == 2 and self.get_score() == 21


  def bust(self):
    """
    Description
    In: None
    Out: True / False
    """
    if not self._bust and self.get_score() > 21:
      self._bust = True
    return self._bust


  def reset_hand(self):
    """
    Resets the values for the players hand back to their default values fir the next round
    In: None
    Out: None
    """
    self.hand = []
    self._bust = False


class Dealer(Player):
  """
  The special instance of a player that the game track to compare the other player's hands too.

  __repr__()
  Returns a string of the dealer's hand with the first card hidden as to hide it from the User
  """

  def __init__(self):
    super(Dealer, self).__init__()

  def __repr__(self):
    """
    Description
    In: None
    Out: String
    """
    output = '['
    for i in range(1 ,len(self.hand)):
      if output == '[':
        output += '**********, '
      output += str(self.hand[i])
    return output + ']'


class User(Player):
  """
  An extention of the Player class that has the added functionality of the bank to track the player's points

  place_bet(bet)
  Takes in an int as the player's bet and stores it to be used as the payout later in the round

  get_bank()
  Returns the current value of the user's bank.

  get_bet()
  Returns the value of the user's last placed bet

  beat_dealer(win)
  Takes in a boolean as an argument and will add (True) or subtract (False) the user's last be from their bank

  to_csv()
  Takes no arguments but will save the users current hand to a csv file to be used when calculating statistics in the notebook
  """
  def __init__(self):
    super(User, self).__init__()
    self.bank = 100
    self.bet = 0


  def place_bet(self, bet):
    """
    Saves the value that was placed as a bet by the player
    In: Int Value
    Exception: Value saved must be an Int
    Out: None
    """
    if not isinstance(bet, int):
      raise ValueError
    self.bet = bet


  def get_bank(self):
    """
    Returns the value of the user's current bank
    In: None
    Out: Current Players Bank
    """
    return self.bank


  def get_bet(self):
    """
    Returns the value of the user's last saved bet
    In: None
    Out: Int Value
    """
    return self.bet


  def beat_dealer(self, win = False):
    """
    Edits the players bank value based on the input boolean. True adds. False subtracts
    In: Boolean
    Out: None
    """
    if win:
      self.bank += self.bet
    else:
      self.bank -= self.bet


  def to_csv(self):
    """
    Description
    In: The player's hand
    Exception: If the file is not found the game will skip saving the user data
    Out: .csv file with the information on the hand
    """
    file_path = './notebooks/hand.csv'
    try:
      with open(file_path, mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Points'])

        for card in self.hand:
          csv_writer.writerow([card.get_value()])
    except FileNotFoundError:
      print('**File not saved**')
      return

###################
## Unique Errors ##
###################

class EmptyHandError(ValueError):
  pass
