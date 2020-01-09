import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/./views/')


import arcade
from arcade.gui import *
# TO DO Don't import star
from game import Game
from views import StartView, GameViewBid

# window Width
WIDTH = 1200

# window Height
HEIGHT = 700

class Window(arcade.Window):
  """Class to create game window"""

  def __init__(self, width, height, title, from_top, from_right):
    # self.width = width
    # self.height = height
    super().__init__(width, height, title)
    self.set_location(from_top,from_right)



class VizGame:
  """class to extract prints and inputs data"""

  def __init__(self):
    self.game = Game()
    self.window = Window(WIDTH, HEIGHT, 'blackjack', 10, 10)
    self.view = StartView(self, WIDTH, HEIGHT)

  def run(self):
    self.set_view(self.view)
    arcade.run()

  def get_view(self):
    return self.view

  def set_view(self, view):
    self.view = view
    self.window.show_view(self.view)



if __name__ == "__main__":
    viz_game = VizGame()
    viz_game.run()




