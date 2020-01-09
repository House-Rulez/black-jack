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

  def setup_theme(self):
      self.theme = Theme()
      self.theme_2 = Theme()
      self.theme.set_font(24, arcade.color.BLACK)
      self.set_button_textures()

  def on_show(self):
      self.setup_theme()
      arcade.set_background_color(arcade.color.AMETHYST)
      self.play_button = PlayButton(550, 100, 80, 80, theme=self.theme, text='play')
      self.exit_button = ExitButton(650, 100, 80, 80, theme=self.theme_2, text='exit')
      self.button_list.append(self.play_button)
      self.button_list.append(self.exit_button)

  def set_button_textures(self):
    #Play button
      normal = "img/buttons/green.png"
      hover = "img/buttons/pink.png"
      clicked = "img/buttons/red.png"
      locked = "img/buttons/blue.png"

    #Exit button
      self.theme.add_button_textures(normal, hover, clicked, locked)
      normal2 = "img/buttons/red.png"
      hover2 = "img/buttons/blue.png"
      clicked2 = "img/buttons/pink.png"
      locked2 = "img/buttons/green.png"
      self.theme_2.add_button_textures(normal2, hover2, clicked2, locked2)



  def on_draw(self):
      arcade.start_render()
      start_x = self.WIDTH/2
      start_y = self.HEIGHT/2
      arcade.draw_text("Welcome to Black Jack! \n You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n Would you like to play?", start_x, start_y, arcade.color.BLACK, font_size=30, anchor_x="center", anchor_y="center", align='center')
      super().on_draw()
      self.play_button.draw()
      self.exit_button.draw()
      if self.play_button.pressed:
        game_view = GameViewBid(self.WIDTH, self.HEIGHT)
        self.game.window.show_view(game_view)
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


    # TODO:Find out why place Bid Field doesn't work
    #  TODO: connect Place bid to the game
    # self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))

    # self.textbox_list.append(arcade.gui.TextBox(WIDTH/2 - 90, HEIGHT/2, width=50, height=40, theme=None, outline_color=arcade.color.BLACK))
    # self.button_list.append(arcade.gui.SubmitButton(self.textbox_list[0], self.on_submit, WIDTH/2+250 , HEIGHT/2))

  def on_show(self):
    arcade.set_background_color(arcade.color.AMAZON)
    increase1_button = ValueButton(1, 950, 400, 80, 30)
    decrease1_button = ValueButton(-1, 1050, 400, 80, 30)
    self.button_list.append(increase1_button)
    self.button_list.append(decrease1_button)
    increase5_button = ValueButton(5, 950, 350, 80, 30)
    decrease5_button = ValueButton(-5, 1050, 350, 80, 30)
    self.button_list.append(increase5_button)
    self.button_list.append(decrease5_button)
    increase10_button = ValueButton(10, 950, 300, 80, 30)
    decrease10_button = ValueButton(-10, 1050, 300, 80, 30)
    self.button_list.append(increase10_button)
    self.button_list.append(decrease10_button)
    increase25_button = ValueButton(25, 950, 250, 80, 30)
    decrease25_button = ValueButton(-25, 1050, 250, 80, 30)
    self.button_list.append(increase25_button)
    self.button_list.append(decrease25_button)

  def on_draw(self):
    arcade.start_render()
    self.deck_back.draw()
    self.dealer_card_back1.draw()
    self.dealer_card_back2.draw()
    self.player_card_back1.draw()
    self.player_card_back2.draw()


    super().on_draw()

    arcade.draw_text(f"Place your bid:\n Your bet is {self.bet}", self.WIDTH/2, self.HEIGHT/2, arcade.color.BLACK, 24, anchor_x="center")

    for button in self.button_list:

    # if player made input
      if button.on_release():
        if self.bet + button.get_value() < 1:
          continue
        # print(self.button_list[0].on_release)
        self.bet += button.get_value()


  # def on_submit(self):
  #       self.text = "5"

