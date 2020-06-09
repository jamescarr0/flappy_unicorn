import pygame
from text_image import TextImage

class GameOver:
    """ A class to manage the game over screen. """
    def __init__(self, game):
        """ Constructor. """
        self.screen = game.screen
        self.settings = game.settings
        self.text = self.settings.game_over_text
        self.title = TextImage(game.screen, self.settings.game_over_text,
                               size=60, text_color=self.settings.game_over_color)
        self.bg_rect = self.title.text_img.get_rect()
        self.bg_rect.center = self.title.rect.center

        # Add padding
        self.bg_rect.inflate_ip(20, 20)

    def blit_me(self):
        self.screen.fill((255, 255, 255), self.bg_rect)
        self.title.blit_me()
