

import arcade
from arcade.gui import TextButton, Theme
from buttons import PlayButton, ExitButton, ValueButton, SubmitButton

class GameView(arcade.View):
  def __init__(self, view, WIDTH, HEIGHT):
    super().__init__()
    self.view = view
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.game = view.game





class StartView(GameView):
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
      self.view.set_view(GameViewBid(self.view, self.WIDTH, self.HEIGHT))

    if self.exit_button.pressed:
      arcade.close_window()



class GameViewBid(GameView):
  """Class to display the game view for the game"""

  def __init__(self,view, WIDTH, HEIGHT):
    super().__init__(view, WIDTH, HEIGHT)
    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2
    self.bet = 1
    self.user_bank = self.game.user.get_bank()
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


  def on_show(self):
    arcade.set_background_color(arcade.color.AMAZON)
    increase1_button = ValueButton(1, 200, 200, 80, 30)
    decrease1_button = ValueButton(-1, 400, 200, 80, 30)
    submit_button = SubmitButton(900, 350, 40, 40, text="Submit")
    self.button_list.append(increase1_button)
    self.button_list.append(decrease1_button)
    self.button_list.append(submit_button)

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

      if isinstance(button, ValueButton) and button.on_release():
        if self.bet + button.get_value() < 1:
          continue

        if self.bet + button.get_value() >= self.user_bank:
          self.bet = self.user_bank
          continue

        self.bet += button.get_value()

      if isinstance(button, SubmitButton) and button.pressed:
        self.game.place_user_bet(self.bet)
        self.view.set_view(RoundView(self.view, self.WIDTH, self.HEIGHT))


class RoundView(GameView):
  def __init__(self,view, WIDTH, HEIGHT):
    super().__init__(view, WIDTH, HEIGHT)

    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2
    self.bet = 1
    self.game
    self.deck_back = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)
    self.dealer_hand1 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)
    self.dealer_hand2 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)
    self.user_hand1 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)
    self.user_hand2 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x, center_y=self.c_y)



  def on_show(self):
    self.game.deal()



  def on_draw(self):
    arcade.start_render()


    user_hand = self.game.user_hand()
    dealer_hand = self.game.dealer_hand()
    for card in user_hand:
      card_image = arcade.Sprite(f'img/{card.img}',scale=0.2,center_x=self.c_x, center_y=self.c_y)
      card_image.draw()








