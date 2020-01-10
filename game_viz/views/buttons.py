import arcade
from arcade.gui import TextButton, Theme
# from game_viz import my_game


class PlayButton(TextButton):
  """Class to create Play Button for the Starting screen"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme)



  def on_press(self):
      self.pressed = True



class ExitButton(TextButton):
  """Class to create Exit Button for the Starting screen"""

  def __init__(self,x=0, y=0, width=100, height=40, theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme, font_color=arcade.color.BLACK)

  def on_press(self):
      self.pressed = True


class ValueButton(TextButton):
  """Class to crete number buttons to increment or decrease the bid value on the Bid View screen"""

  def __init__(self,value=0, x=0, y=0, width=100, height=40, text="", theme=None, face_color=None):
      super().__init__(x, y, width, height, str(value), theme=theme, face_color=arcade.color.BYZANTIUM, font_color=arcade.color.BLACK)
      self.pressed = False
      self.value = value

  def on_press(self):
      self.pressed = True
      # return self.pressed

  def on_release(self):

    if self.pressed:
      self.pressed = False
      return True

  def get_value(self):
    return self.value


class SubmitButton(TextButton):
  """Class to create Submit Button for the Place Bid screen"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme, font_color=arcade.color.BLACK)


  def on_press(self):
      self.pressed = True

class HitButton(TextButton):
  """Class to create Hit Button for the Round screen view"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme, font_color=arcade.color.BLACK)


  def on_press(self):
      self.pressed = True

  def on_release(self):

    if self.pressed:
      self.pressed = False
      return True

class StandButton(TextButton):
  """Class to create Stand Button for the Round screen view"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme, font_color=arcade.color.BLACK)


  def on_press(self):
      self.pressed = True

  def on_release(self):

    if self.pressed:
      self.pressed = False
      return True

