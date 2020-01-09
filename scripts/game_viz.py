import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/./viz/')


import arcade
from arcade.gui import *
# TO DO Don't import star
from game import Game
from views import StartView, GameViewBid

# window Width
WIDTH = 1200

# window Height
HEIGHT = 700

class MyGameWindow(arcade.Window):
  """Class to create game window"""

  def __init__(self, width, height, title, from_top, from_right):
    super().__init__(width, height, title)
    self.set_location(from_top,from_right)



class VizGame:
  """class to extract prints and inputs data"""

  def __init__(self):
    self.game = Game(self._print, self._input)
    self.game.play()
    self.window = MyGameWindow(1200, 700, 'blackjack', 10, 10)
    self.view = StartView(self, WIDTH, HEIGHT)

    self.window.show_view(self.view)

    arcade.run()


  def _print(self, *args):

    msg = args[0]

    if msg == 'how much would you like to bet?':
      self.view = GameViewBid(WIDTH, HEIGHT)
      self.window.show_view(self.view)

  def _input(self, *args):
    prompt = args[0]

    ########## TODO: Check if it is actually sends the answer to the game

    if prompt == 'Would you like to play?: y/n':
      print('Button Press')
      if self.view.start_game:
        self.view = GameViewBid(WIDTH, HEIGHT)
        self.window.show_view(self.view)
        return 'y'
    else:
      return 'e'



if __name__ == "__main__":
    viz_game = VizGame()



