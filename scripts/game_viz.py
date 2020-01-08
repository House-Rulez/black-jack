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




class StartView(arcade.View):
  """Class to display the starting View for the game"""

  def setup_theme(self):
      self.theme = Theme()
      self.theme.set_font(24, arcade.color.WHITE)
      self.set_button_textures()

  def on_show(self):
      self.setup_theme()
      arcade.set_background_color(arcade.color.AMETHYST)
      self.play_button = PlayButton(100, 100, 80, 80, theme=self.theme, text='play')
      self.exit_button = ExitButton(250, 100, 80, 80, theme=self.theme, text='exit')
      self.button_list.append(self.play_button)
      self.button_list.append(self.exit_button)

  def set_button_textures(self):
      normal = "img/buttons/green.png"
      hover = "img/buttons/pink.png"
      clicked = "img/buttons/red.png"
      locked = "img/buttons/blue.png"
      self.theme.add_button_textures(normal, hover, clicked, locked)


  def on_draw(self):
      arcade.start_render()
      arcade.draw_text("Welcome to Black Jack! \n            You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n Would you like to play?", WIDTH/2, HEIGHT/2,
                        arcade.color.BLACK, font_size=30, anchor_x="center")
      super().on_draw()
      self.play_button.draw()
      self.exit_button.draw()



class GameViewBid(arcade.View):
  """Class to display the game view for the game"""

  def __init__(self):
    self.game = Game(self._print, self._input)
    self.game.play
    self.window = MyGameWindow(1200, 700, 'blackjack', 10, 10)
    menu_view = StartView(self, WIDTH, HEIGHT)

    self.window.show_view(menu_view)

    arcade.run()


  def _print(self, *args):

    msg = args[0]




  def _input(self, *args):
    prompt = args[0]

    ########## TODO: Check if it is actually sends the answer to the game

    if prompt == 'Would you like to play?: y/n':

      return 'y'


if __name__ == "__main__":
    viz_game = VizGame()



