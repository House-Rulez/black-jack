
class Player:

  def __init__(self):
    self.hand = []
    self._bust = False


  def hit(self, card):
    # Add new card to their hand
    """
    Takes in a card and adds it to the players hand
    In: Card instance
    Exceptions: None
    Out: None
    """
    self.hand.append(card)


  def __str__(self):
    output = '['
    for card in self.hand:
      if not output == '[':
        output += ', '
      output += str(card) 
    return output + ']'

  def get_score(self):
    """
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
    return len(self.hand) == 2 and self.get_score() == 21


  def bust(self):
    if self.get_score() > 21:
      self._bust = True
    return self._bust


  def reset_hand(self):
    self.hand = []
    self._bust = False


class Dealer(Player):
  def __init__(self):
    super(Dealer, self).__init__()

  def __repr__(self):
    output = '['
    for i in range(1 ,len(self.hand)):
      if output == '[':
        output += '**********, '
      output += str(self.hand[i]) 
    return output + ']'


class User(Player):
  def __init__(self):
    super(User, self).__init__()
    self.bank = 100
    self.bet = 0


  def place_bet(self, bet):
    if not isinstance(bet, int):
      raise ValueError
    self.bet = bet


  def get_bank(self):
    return self.bank


  def get_bet(self):
    return self.bet


  def beat_dealer(self, win = False):
    if win:
      self.bank += self.bet
    else:
      self.bank -= self.bet


###################
## Unique Errors ##
###################

class EmptyHandError(ValueError):
  pass
