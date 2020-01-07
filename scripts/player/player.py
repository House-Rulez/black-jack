import csv

class Player:

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
  Description
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
  Description
  """
  def __init__(self):
    super(User, self).__init__()
    self.bank = 100
    self.bet = 0


  def place_bet(self, bet):
    """
    Saves the value that was place as a bet by the player
    In: Int Value
    Out: None
    """
    if not isinstance(bet, int):
      raise ValueError
    self.bet = bet


  def get_bank(self):
    """
    Description
    In: None
    Out: Current Players Bank
    """
    return self.bank


  def get_bet(self):
    """
    Returns the value that the user saved as their bet
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
    file_path = './notebooks/hand.csv'
    with open(file_path, mode="w") as csv_file:
      csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow(['Points'])

      for card in self.hand:
        csv_writer.writerow([card.get_value()])

###################
## Unique Errors ##
###################

class EmptyHandError(ValueError):
  pass
