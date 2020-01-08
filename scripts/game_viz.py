import arcade
from arcade.gui import *
# TO DO Don't import star
import os
from game import Game

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
      self.play_button = PlayButton(100, 100, 40, 40, theme=self.theme, text='play')
      self.exit_button = ExitButton(200, 100, 40, 40, theme=self.theme, text='exit')
      self.button_list.append(self.play_button)
      self.button_list.append(self.exit_button)

  def set_button_textures(self):
      normal = "img/buttons/green.png"
      hover = "img/buttons/pink.png"
      clicked = "img/buttons/red.png"
      locked = "img/buttons/blue.png"
      print(os.getcwd())
      print(type(self.theme))
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
    super().__init__()
    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2
    self.text =""
    # place the deck image to the left of the screen
    self.deck_back = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)

    # place 2 dealer's closed cards to the top of the screen
    self.dealer_card_back1 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3, center_y=self.c_y + HEIGHT/4 +30)
    self.dealer_card_back2 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3 + 140, center_y=self.c_y + HEIGHT/4 + 30)

    # # place 2 player's closed cards to the bottom of the screen
    self.player_card_back1  = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3, center_y=self.c_y - HEIGHT/4 - 30)
    self.player_card_back2  = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3 +140, center_y=self.c_y - HEIGHT/4 - 30)


    # Place Bid section
    self.text_list.append(arcade.gui.Text("Place your bid: ", WIDTH/2, HEIGHT/2, arcade.color.BLACK, font_size=20, anchor_x="center"))

    # TODO:Find out why place Bid Field doesn't work
    #  TODO: connect Place bid to the game
    # self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))

    self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))
    self.button_list.append(arcade.gui.SubmitButton(self.textbox_list[0], self.on_submit, WIDTH/2+250 , HEIGHT/2))

  def on_show(self):
    arcade.set_background_color(arcade.color.AMAZON)

  def on_draw(self):
    arcade.start_render()
    self.deck_back.draw()
    self.dealer_card_back1.draw()
    self.dealer_card_back2.draw()
    self.player_card_back1.draw()
    self.player_card_back2.draw()

    super().on_draw()

    # if player made input
    if self.text:
      arcade.draw_text(f"You're bet is {self.text}", 400, 100, arcade.color.BLACK, 24)

  def on_submit(self):
        self.text = self.textbox_list[0].text_storage.text


class PlayButton(TextButton):
  """Class to create Play Button for the Starting screen"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme)



  def on_press(self):
      self.pressed = True


  def on_release(self):
    """Method to change view to GAmeViewBid when Play button clicked"""
    game_view = GameViewBid()
    my_game.show_view(game_view)

class ExitButton(TextButton):
  """Class to create Exit Button for the Starting screen"""

  def __init__(self,x=0, y=0, width=100, height=40, theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme)

  def on_press(self):
      self.pressed = True


  def on_release(self):

    """Method to close game when Exit button clicked"""

    # TODO: figure out why window is not closing
    arcade.close_window()



class VizGame:
  """class to extract prints and inputs data"""

  def __init__(self):
    self.game = None

  def _print(self, *args):

    msg = args[0]

    if msg.startswith('Welcome to Black Jack!'):

      menu_view = StartView()

      my_game.show_view(menu_view)

      arcade.run()

  def _input(self, *args):
    prompt = args[0]

    ########## TODO: Check if it is actually sends the answer to the game

    if prompt == 'Would you like to play?: y/n' and PlayButton.on_release:

      return 'y'


if __name__ == "__main__":
    my_game = MyGameWindow(1200, 700, 'blackjack', 10, 10)
    viz_game = VizGame()
    game = Game(viz_game._print, viz_game._input)
    viz_game.game = game

    # start the game
    game.play()
