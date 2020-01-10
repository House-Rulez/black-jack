class Card:
  """
  Used to create a card that stores both the value and the name of the function

  get_value()
  returns the card's point value
  """
  def __init__(self, value):
    self.suit = 'None'
    self.value, self.name = Card.card_values(value)
    self.img = Card.set_image(self.name, self.suit)

  def __str__(self):
    return f'{self.name} of {self.suit}'

  def get_value(self):
    return self.value

  @staticmethod
  def card_values(value):
    """
    Takes in an int Value and returns the value of the card represents in the game as well as the name of the card as a string
    In: Int value
    Exceptions: If Greater than 13 will raise a value error
    Out: (Value of card, String name of card)
    """
    if value > 13 or value < 1:
      raise ValueError

    if value == 1:
      return (11, 'A')

    elif value > 10:
      name = ''
      if value == 11:
        name = 'J'
      elif value == 12:
        name = 'Q'
      elif value == 13:
        name = 'K'
      return(10, name)

    return (value, str(value))

  @staticmethod
  def set_image(name, suit):
    return str(name) + suit[0] + '.png'


class Spade(Card):
  def __init__(self, value):
    super(Spade, self).__init__(value)
    self.suit = 'Spades'
    self.img = Card.set_image(self.name, self.suit)



class Heart(Card):
  def __init__(self, value):
    super(Heart, self).__init__(value)
    self.suit = 'Hearts'
    self.img = Card.set_image(self.name, self.suit)



class Diamond(Card):
  def __init__(self, value):
    super(Diamond, self).__init__(value)
    self.suit = 'Diamonds'
    self.img = Card.set_image(self.name, self.suit)



class Club(Card):
  def __init__(self, value):
    super(Club, self).__init__(value)
    self.suit = 'Clubs'
    self.img = Card.set_image(self.name, self.suit)

