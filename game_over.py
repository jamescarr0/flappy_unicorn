from text_image import TextImage


class GameOver:
    """ A class to manage the game over screen. """

    def __init__(self, game):
        """ Constructor. """
        self.screen = game.screen
        self.settings = game.settings

        self.text = self.settings.game_over_text
        self.game_over_img = TextImage(game.screen, self.settings.game_over_text,
                                       size=60, text_color=self.settings.game_over_color)

        self.r_button_text = self.settings.retry_button_text
        self.retry_button = TextImage(game.screen, self.r_button_text, size=40, text_color=self.settings.game_over_color)
        self.retry_button.rect.midtop = self.game_over_img.rect.midbottom

    def blit_me(self):
        """ Blit game over img to screen. """
        self.game_over_img.blit_me()
        self.retry_button.blit_me()
