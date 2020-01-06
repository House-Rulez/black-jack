class Card:
  """"""
  def __init__(self, value):
    self.value, self.name = Card.card_values(value)

  @staticmethod
  def card_values(value):
    """
    Takes in an int Value and returns the value of the card represents in the game as well as the name of the card as a string
    In: Int value
    Exceptions: If Greater than 13 will raise a value error
    Out: (Value of card, String name of card)
    """
    if value > 13:
      raise ValueError

    if value == 1:
      return (11, 'Ace')

    elif value > 10:
      name = ''
      if value == 11:
        name = 'Jack'
      elif value == 12:
        name = 'Queen'
      elif value == 13:
        name = 'King'
      return(10, name)

    return (value, str(value))


class Spade(Card):
  def __init__(self, value):
    self.suit = 'Spade'
    super(Spade, self).__init__(value)


class Heart(Card):
  def __init__(self, value):
    self.suit = 'Heart'
    super(Heart, self).__init__(value)


class Diamond(Card):
  def __init__(self, value):
    self.suit = 'Diamond'
    super(Diamond, self).__init__(value)


class Club(Card):
  def __init__(self, value):
    self.suit = 'Club'
    super(Club, self).__init__(value)
