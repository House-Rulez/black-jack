from .hand import Hand

class Player:
  def __init__(self):
    self.hand = Hand()

  def hit(self, card):
    # Add new card to their hand
    self.hand.add_card(card)

  def get_score(self):
    return hand.score()

  def bust(self):
    return self.get_score() > 21

class Dealer(Player):
  def __init__(self):
    super(Dealer, self).__init__()

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