import arcade
from arcade.gui import *
import os
from game import Game

class PlayButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Play", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True


    def on_release(self):
        if self.pressed:

          self.game.pause = False
          self.pressed = False
          arcade.close_window()


class ExitButton(TextButton):
    def __init__(self, game, x=0, y=0, width=100, height=40, text="Exit", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        self.game = game

    def on_press(self):
        self.pressed = True
        print('niinini')

    def on_release(self):
        if self.pressed:
            self.game.pause = True
            self.pressed = False



class MyGameWindow(arcade.Window):
  def __init__(self, width, height, title, from_top, from_right, print_):
    super().__init__(width, height, title)
    self.set_location(from_top,from_right)
    arcade.set_background_color(arcade.color.WHITE)
    self.print_= print_

    self.pause = False
    # self.text = "Graphical User Interface"
    self.text_x = 0
    self.text_y = 300
    self.text_font_size = 40
    self.speed = 1
    self.theme = None

  def set_button_textures(self):
    normal = "img/icons8-button-100.png"
    hover = "img/icons8-button-100.png"
    clicked = "img/icons8-button-96.png"
    locked = "img/icons8-button-100.png"
    self.theme.add_button_textures(normal, hover, clicked, locked)

  def setup_theme(self):
    self.theme = Theme()
    self.theme.set_font(24, arcade.color.WHITE)
    self.set_button_textures()

  def set_buttons(self):
    self.button_list.append(PlayButton(self, 650, 300, 110, 50, theme=self.theme))
    self.button_list.append(ExitButton(self, 450, 300, 110, 50, theme=self.theme))

  def setup(self):
    self.setup_theme()
    self.set_buttons()


  def on_draw(self):
    arcade.start_render()
    super().on_draw()
    arcade.draw_text(self.print_, 200, 350, arcade.color.BLACK, 23)



class VizGame:
  """class to extract prints and inputs data"""

  def __init__(self):
    self.game = None

  def _print(self, *args):

    msg = args[0]

    if msg.startswith('Welcome to Black Jack!'):
      msg = "                   Welcome to Black Jack! \n            You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n Would you like to play?"
      my_game = MyGameWindow(1200, 700, 'blackjack', 50, 50, msg)

      my_game.on_draw()
      my_game.setup()
      arcade.run()

  def _input(self, *args):
    prompt = args[0]


    if PlayButton.on_release:

      return 'y'







if __name__ == "__main__":
    viz_game = VizGame()
    # arcade.run()
    game = Game(viz_game._print, viz_game._input)
    viz_game.game = game

    game.play()


# MyGameWindow(1200, 700, 'blackjack', 30, 20)
# arcade.run()

# class MyGameWindow(arcade.Window):
#   def __init__(self, width, height, title, from_top, from_right):
#     super().__init__(width, height, title)
#     self.set_location(from_top,from_right)
#     arcade.set_background_color(arcade.color.WHITE)

#     self.c_x = 300
#     self.c_y = 200
#     self.x_speed = 10
#     self.y_speed = 5

#     self.sprite1 = arcade.Sprite('cards_PNG8478.png',center_x=self.c_x, center_y=self.c_y)

#   def on_draw(self):
#     arcade.start_render()
#     # self.sprite1.draw()
#     arcade.draw_circle_filled(self.c_x, self.c_y, 40, arcade.color.BLACK, 40)
#     arcade.draw_text("hi", 50, 50, arcade.color.BLACK, 23)
#     # arcade.draw_lines([(0,0), (300,800)], arcade.color.RAJAH)
#     # arcade.draw_point(150, 150, arcade.color.WHEAT, 20)

#   # def on_update(self, delta_time):
#   #   self.c_x += self.x_speed + delta_time + 0.005
#   #   self.c_y += self.y_speed + delta_time

#   #   if self.c_x > 900 - 90 or self.c_x < 0:
#   #     self.x_speed *=-1
#   #   if self.c_y > 600 - 130 or self.c_x < 0:
#   #     self.y_speed *=-1
#   #   # print(delta_time)
#   #   self.sprite1.set_position(self.c_x, self.c_y)

# MyGameWindow(1200, 700, 'blackjack', 100, 100)
# # MyGameWindow(200, 500, 'stats', 900, 150)
# arcade.run()

