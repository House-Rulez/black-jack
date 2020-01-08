import arcade
from arcade.gui import *
# TO DO Dont'import star
import os
from game import Game



WIDTH = 1200
HEIGHT = 700


class GameView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game - press SPACE to advance", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    # def on_key_press(self, key, _modifiers):
    #     if key == arcade.key.SPACE:
    #         game_over_view = GameOverView()
    #         self.window.show_view(game_over_view)


class StartView(arcade.View):
  def on_show(self):
      arcade.set_background_color(arcade.color.ORANGE)
      play_button = TextButton(200, 200, 350, 20, "Play")
      self.button_list.append(play_button)


  def on_draw(self):
      arcade.start_render()
      arcade.draw_text("Welcome to Black Jack! \n            You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n Would you like to play?", WIDTH/2, HEIGHT/2,
                        arcade.color.BLACK, font_size=30, anchor_x="center")
      super().on_draw()

  # def on_mouse_press(self, _x, _y, _button, _modifiers):
  #     game_view = GameView()
  #     self.window.show_view(game_view)

  # def set_button_textures(self):
  #   normal = "img/icons8-button-100.png"
  #   hover = "img/icons8-button-100.png"
  #   clicked = "img/icons8-button-96.png"
  #   locked = "img/icons8-button-100.png"
  #   self.theme.add_button_textures(normal, hover, clicked, locked)

  # def setup_theme(self):
  #   self.theme = Theme()
  #   self.theme.set_font(24, arcade.color.WHITE)
  #   self.set_button_textures()

  # def set_buttons(self):
  #   self.button_list.append(PlayButton(self, 650, 300, 110, 50, theme=self.theme))
  #   self.button_list.append(ExitButton(self, 450, 300, 110, 50, theme=self.theme))

  # def setup(self):
  #   self.setup_theme()
  #   self.set_buttons()




class PlayButton(TextButton):
    def __init__(self, x=0, y=0, width=100, height=40, text="Play", theme=None):
        super().__init__(x, y, width, height, text, theme=theme)
        # self.game = game

    def on_press(self):
        self.pressed = True


    def on_release(self):
      game_view = GameView()
      self.window.show_view(game_view)
      
        # # if self.pressed:

        #   # self.game.pause = False
        #   self.pressed = False
        #   print("uhkhb")
        #   # arcade.close_window()


# class ExitButton(TextButton):
#     def __init__(self, game, x=0, y=0, width=100, height=40, text="Exit", theme=None):
#         super().__init__(x, y, width, height, text, theme=theme)
#         self.game = game

#     def on_press(self):
#         self.pressed = True
#         print('niinini')

#     def on_release(self):
#         if self.pressed:
#             self.game.pause = True
#             self.pressed = False



class MyGameWindow(arcade.Window):
  def __init__(self, width, height, title, from_top, from_right):
    super().__init__(width, height, title)
    self.set_location(from_top,from_right)
    arcade.set_background_color(arcade.color.WHITE)
    # self.print_= print_

    self.pause = False
    # self.text = "Graphical User Interface"
    self.text_x = 0
    self.text_y = 300
    self.text_font_size = 40
    self.speed = 1
    self.theme = None

  # def set_button_textures(self):
  #   normal = "img/icons8-button-100.png"
  #   hover = "img/icons8-button-100.png"
  #   clicked = "img/icons8-button-96.png"
  #   locked = "img/icons8-button-100.png"
  #   self.theme.add_button_textures(normal, hover, clicked, locked)

  # def setup_theme(self):
  #   self.theme = Theme()
  #   self.theme.set_font(24, arcade.color.WHITE)
  #   self.set_button_textures()

  # def set_buttons(self):
  #   self.button_list.append(PlayButton(self, 650, 300, 110, 50, theme=self.theme))
  #   self.button_list.append(ExitButton(self, 450, 300, 110, 50, theme=self.theme))

  # def setup(self):
  #   self.setup_theme()
  #   self.set_buttons()


  # def on_draw(self):
  #   arcade.start_render()
  #   super().on_draw()
  #   arcade.draw_text(self.print_, 200, 350, arcade.color.BLACK, 23)



class VizGame:
  """class to extract prints and inputs data"""

  def __init__(self):
    self.game = None

  def _print(self, *args):

    msg = args[0]

    if msg.startswith('Welcome to Black Jack!'):

      my_game = MyGameWindow(1200, 700, 'blackjack', 50, 50)

      # my_game.on_draw()

      menu_view = StartView()
      # menu_view.setup()
      my_game.show_view(menu_view)
      # my_game.setup()


      arcade.run()

  def _input(self, *args):
    prompt = args[0]


    if prompt == 'Would you like to play?: y/n' and PlayButton.on_release:

      return 'y'







if __name__ == "__main__":
    viz_game = VizGame()
    # arcade.run()
    game = Game(viz_game._print, viz_game._input)
    viz_game.game = game

    game.play()




















