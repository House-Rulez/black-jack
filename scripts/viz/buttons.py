import arcade
from arcade.gui import TextButton
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
      super().__init__(x, y, width, height, text, theme=theme)

  def on_press(self):
      self.pressed = True


class ValueButton(TextButton):

  def __init__(self,value=0, x=0, y=0, width=100, height=40, text="", theme=None, face_color=None):
      super().__init__(x, y, width, height, str(value), theme=theme, face_color=arcade.color.BYZANTIUM)
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
  """Class to create Play Button for the Starting screen"""
  def __init__(self, x=0, y=0, width=40, height=40,  theme=None, text=" "):
      super().__init__(x, y, width, height, text, theme=theme)


  def on_press(self):
      self.pressed = True


