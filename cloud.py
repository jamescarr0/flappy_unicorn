import pygame
from pygame.sprite import Sprite
from random import randint

class Cloud(Sprite):
    """ A class to manage a cloud. """
    def __init__(self, game):
        """ Constructor. """
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        # Load a random cloud image.
        self.cloud_image = pygame.image.load(f'images/clouds{randint(1, 4)}.png').convert_alpha()
        self.cloud_rect = self.cloud_image.get_rect()

        self.cloud_speed = float(self._set_cloud_speed())

        # Set cloud at random position.
        self._set_cloud_position()

    def _set_cloud_speed(self):
        n = randint(1, 3)
        if n == 2:
            n -= 0.5
        return n

    def _set_cloud_position(self):
        t_pos = randint(0, 100)
        self.cloud_rect.topleft = (self.settings.screen_width, t_pos)
        self.x = float(self.cloud_rect.x)

    def update(self):
        """ Update the clouds position and blit. """
        self.x -= self.cloud_speed
        self.cloud_rect.x = self.x

    def draw_cloud(self):
        """ Blit cloud to screen. """
        self.screen.blit(self.cloud_image, self.cloud_rect)
