import arcade
from arcade.gui import TextButton, Theme
from buttons import PlayButton, ExitButton, ValueButton

class StartView(arcade.View):
  """Class to display the starting View for the game"""
  def __init__(self, game, WIDTH, HEIGHT):
    super().__init__()
    self.game = game
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.start_game = False

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
    # print(os.getcwd())
    # print(type(self.theme))
    self.theme.add_button_textures(normal, hover, clicked, locked)


  def on_draw(self):
    arcade.start_render()
    arcade.draw_text("Welcome to Black Jack! \n            You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n Would you like to play?", self.WIDTH/2, self.HEIGHT/2,
                      arcade.color.BLACK, font_size=30, anchor_x="center")
    super().on_draw()
    self.play_button.draw()
    self.exit_button.draw()
    if self.play_button.pressed:
      self.start_game = True
    if self.exit_button.pressed:
      arcade.close_window()



class GameViewBid(arcade.View):
  """Class to display the game view for the game"""

  def __init__(self, WIDTH, HEIGHT):
    super().__init__()
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2
    self.bet = 0
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


    #  TODO: connect Place bid to the game
    # self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))

    # self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))
    # self.button_list.append(arcade.gui.SubmitButton(self.textbox_list[0], self.on_submit, WIDTH/2+250 , HEIGHT/2))

  def on_show(self):
    arcade.set_background_color(arcade.color.AMAZON)
    increase1_button = ValueButton(1, 200, 200, 80, 30)
    decrease1_button = ValueButton(-1, 400, 200, 80, 30)
    self.button_list.append(increase1_button)
    self.button_list.append(decrease1_button)

  def on_draw(self):
    arcade.start_render()
    self.deck_back.draw()
    self.dealer_card_back1.draw()
    self.dealer_card_back2.draw()
    self.player_card_back1.draw()
    self.player_card_back2.draw()


    super().on_draw()

    arcade.draw_text(f"You're bet is {self.bet}", self.WIDTH/2, self.HEIGHT/2, arcade.color.BLACK, 24)

    for button in self.button_list:

    # if player made input
      if button.on_release():
        if self.bet + button.get_value() < 1:
          continue
        # print(self.button_list[0].on_release)
        self.bet += button.get_value()


  # def on_submit(self):
  #       self.text = "5"

