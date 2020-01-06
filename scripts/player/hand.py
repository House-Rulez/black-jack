class Hand:
  def __init__(self):
    self.cards = []

  # Calculate Score
  def score(self):
    """
    In: None
    Exceptions: Empty Hand Raises Error
    Out: Current Score of the players hand
    """
    if len(self.cards) == 0:
      raise EmptyHandError

    score = 0
    aces = 0
    for card in self.cards:
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


  def add_card(self, card):
    """
    Takes in a card and adds it to the players hand
    In: Card instance
    Exceptions: None
    Out: None
    """
    self.cards.append(card)

###################
## Unique Errors ##
###################

class EmptyHandError(ValueError):
  pass
