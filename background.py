import pygame


class Background:
    """ A class to manage the background and ground animation. """
    def __init__(self, game):
        """ Constructor. """
        self.screen = game.screen
        self.settings = game.settings
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = self.settings.screen_height, self.settings.screen_width

        # Load the background image
        self.bg_img = pygame.image.load('images/bg.png').convert_alpha()
        self.bg_img = pygame.transform.smoothscale(self.bg_img, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def update(self):
        """ Update the background images"""
        self.screen.blit(self.bg_img, self.screen.get_rect())

