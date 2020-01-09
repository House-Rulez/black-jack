

import arcade
from arcade.gui import TextButton, Theme
from buttons import PlayButton, ExitButton, ValueButton, SubmitButton, HitButton, StandButton

class GameView(arcade.View):
  """Class to create GameView instance"""
  def __init__(self, view, WIDTH, HEIGHT):
    super().__init__()
    self.view = view
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.game = view.game
    self.bank = self.game.user.get_bank()
    self.user_bet = self.game.user.get_bet()

  def on_draw(self):
    arcade.start_render()
    super().on_draw()








class StartView(GameView):
  """Class to display the starting View for the game"""

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
    self.theme.add_button_textures(normal, hover, clicked, locked)

      #Exit button
    normal2 = "img/buttons/red.png"
    hover2 = "img/buttons/blue.png"
    clicked2 = "img/buttons/pink.png"
    locked2 = "img/buttons/green.png"
    self.theme_2.add_button_textures(normal2, hover2, clicked2, locked2)


  def on_draw(self):
    super().on_draw()

    start_x = self.WIDTH/2
    start_y = self.HEIGHT/2

    arcade.draw_text("Welcome to Black Jack! \n You start off with 100 chips.\n Try to make it to 250 chips by beating the dealer\'s cards.\n \nWould you like to playg?", start_x, start_y, arcade.color.BLACK, font_size=30, anchor_x="center", anchor_y="center", align='center')
    self.play_button.draw()
    self.exit_button.draw()

    if self.play_button.pressed:
      self.view.set_view(BetView(self.view, self.WIDTH, self.HEIGHT))

    if self.exit_button.pressed:
      arcade.close_window()



class BetView(GameView):
  """Class to display the game view for the "Make a Bid" screen"""

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
    self.dealer_card_back2 = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3 + 70, center_y=self.c_y + HEIGHT/4 + 30)

    # # place 2 player's closed cards to the bottom of the screen
    self.player_card_back1  = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3, center_y=self.c_y - HEIGHT/4 - 30)
    self.player_card_back2  = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.c_x + WIDTH/3 +70, center_y=self.c_y - HEIGHT/4 - 30)


    # Place Bid section


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

    submit_button = SubmitButton(1000, 200, 90, 40, text="Submit")
    self.button_list.append(submit_button)

  def on_draw(self):
    super().on_draw()
    arcade.draw_text(f"Your bank is {self.bank - self.bet}", 100, 100, arcade.color.BLACK, 24)

    self.deck_back.draw()
    self.dealer_card_back1.draw()
    self.dealer_card_back2.draw()
    self.player_card_back1.draw()
    self.player_card_back2.draw()


    arcade.draw_text(f"Place your bid:\n Your bet is {self.bet}", self.WIDTH/2, self.HEIGHT/2, arcade.color.BLACK, 24, anchor_x="center")



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
  """Class to display the window view for the Round"""
  def __init__(self,view, WIDTH, HEIGHT):
    super().__init__(view, WIDTH, HEIGHT)
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2

    self.total_time = 0.0


    self.new_card_x = self.c_x
    self.new_card_y = self.c_y

    self.deck_back = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.new_card_x, center_y=self.new_card_y)
    self.new_card = self.deck_back

  def on_show(self):
    self.game.reset_hands()
    self.game.deal()
    stand_button = StandButton(self.WIDTH/2-40, self.HEIGHT/2, 110, 40, text="Stand")
    self.button_list.append(stand_button)

    hit_button = HitButton(self.WIDTH/2+100, self.HEIGHT/2, 110, 40, text="Hit")
    self.button_list.append(hit_button)

  def on_draw(self):
    super().on_draw()
    arcade.draw_text(f"Your bank is {self.bank - self.user_bet}", 100, 100, arcade.color.BLACK, 24)
    arcade.draw_text(f"Your bet is {self.user_bet}", 100, 50, arcade.color.BLACK, 24)
    self.deck_back.draw()

    user_hand = self.game.user_hand()
    dealer_hand = self.game.dealer_hand()

    for i,card in enumerate(dealer_hand):

      card_image = arcade.Sprite(f'img/{card.img}', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y + self.HEIGHT/4+30)

      if i == 0:
        card_image = arcade.Sprite('img/purple_back.png', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y + self.HEIGHT/4+30)

      card_image.draw()

    for i,card in enumerate(user_hand):
      card_image = arcade.Sprite(f'img/{card.img}', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y - self.HEIGHT/4-30)
      card_image.draw()


    self.new_card.draw()

    for button in self.button_list:
    # if player clicked "Hit"
      if isinstance(button, HitButton) and button.pressed:

        self.game.user_hit()
        button.pressed = False
      if self.game.user.bust():
        self.view.set_view(ScoreView(self.view, self.WIDTH, self.HEIGHT))

      if isinstance(button, StandButton) and button.pressed:

        self.game.dealer_turn()
        self.view.set_view(ScoreView(self.view, self.WIDTH, self.HEIGHT))





  def on_update(self, delta_time):
    self.total_time += 0.5

    # if self.total_time > 30.0:
    # self.new_card_x += (self.c_x + self.WIDTH/3 + 200)/90
    # self.new_card_y -= (self.c_y - self.HEIGHT/4-30)/90
    self.new_card_x = self.c_x + self.WIDTH/3 + 140
    self.new_card_y = self.c_y - self.HEIGHT/4-30
      # if self.new_card_x == (self.c_x + self.WIDTH/3 + 140) and self.new_card_y == (self.c_y - self.HEIGHT/4-30):
      #   return



class ScoreView(GameView):
  def __init__(self,view, WIDTH, HEIGHT):
    super().__init__(view, WIDTH, HEIGHT)
    self.WIDTH = WIDTH
    self.HEIGHT = HEIGHT
    self.c_x = WIDTH/6
    self.c_y = HEIGHT/2

    self.total_time = 0.0

    # self.bet = 1
    # self.game

    self.new_card_x = self.c_x
    self.new_card_y = self.c_y

    self.deck_back = arcade.Sprite('img/purple_back.png',scale=0.2,center_x=self.new_card_x, center_y=self.new_card_y)
    self.new_card = self.deck_back

  def on_show(self):
    result = self.game.calculate_winner()
    self.bank = self.game.user.get_bank()

    #create message variable
    msg = ''

    # dEcide message based on result
    if result == None:
      msg = 'It\s a tie'
    if result:
      msg = 'You won this hand'
    if result == False:
      if self.game.user.bust():
        msg = 'You bust'
      else:
        msg = 'The dealer won'

    self.msg = msg


    submit_button = SubmitButton(self.WIDTH/2-40, self.HEIGHT/2, 110, 40, text="Continue")
    self.button_list.append(submit_button)
  #   # hit_button = HitButton(self.WIDTH/2+100, self.HEIGHT/2, 110, 40, text="Hit")
  #   # self.button_list.append(hit_button)

  def on_draw(self):
    super().on_draw()
    arcade.draw_text(f"Your bank is {self.bank}", 100, 100, arcade.color.BLACK, 24)
    self.deck_back.draw()

    user_hand = self.game.user_hand()
    dealer_hand = self.game.dealer_hand()

    for i,card in enumerate(dealer_hand):

      card_image = arcade.Sprite(f'img/{card.img}', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y + self.HEIGHT/4+30)

      if i == 0 and self.game.user.bust():
        card_image = arcade.Sprite('img/purple_back.png', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y + self.HEIGHT/4+30)

      card_image.draw()

    for i,card in enumerate(user_hand):
      card_image = arcade.Sprite(f'img/{card.img}', scale=0.2,center_x=self.c_x + self.WIDTH/3 + i*70, center_y=self.c_y - self.HEIGHT/4-30)
      card_image.draw()


    arcade.draw_text(self.msg, self.WIDTH/2, self.HEIGHT/2, arcade.color.BLACK, 24, anchor_x="center")

    self.new_card.draw()

    for button in self.button_list:
      if isinstance(button, SubmitButton) and button.pressed:
        if self.game.user.get_bank() == 0:
          self.view.set_view(GameOver(self.view, self.WIDTH, self.HEIGHT))

        elif self.game.user.get_bank() >= 250:
          self.view.set_view(GameOver(self.view, self.WIDTH, self.HEIGHT))

        else:
          self.view.set_view(BetView(self.view, self.WIDTH, self.HEIGHT))




class GameOver(GameView):

  def on_draw(self):
    arcade.start_render()



