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
        self.bg_rect = self.game_over_img.text_img.get_rect()
        self.bg_rect.center = self.game_over_img.rect.center

        # Add padding
        self.bg_rect.inflate_ip(20, 20)

    def blit_me(self):
        """ Blit game over img to screen. """
        self.screen.fill((255, 255, 255), self.bg_rect)
        self.game_over_img.blit_me()
