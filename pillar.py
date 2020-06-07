import pygame
from pygame.sprite import Sprite
from random import randint


class Pillar(Sprite):
    """ A class to manage the pillar obstacle. """
    def __init__(self, game):
        """ Constructor. """
        super().__init__()  # Call superclass.
        self.screen = game.screen
        self.settings = game.settings

        # Load top and bottom pillar images.
        self.bottom_pillar = pygame.image.load('images/Pillar1.png').convert_alpha()
        self.top_pillar = self.bottom_pillar = pygame.image.load('images/Pillar2.png').convert_alpha()
        self.x_top = 0.0
        self.x_btm = 0.0

        # Resize the images.
        self._resize_pillars()

        # Set pillar starting position.
        self._set_pillar_position()

    def update(self):
        """ Update top and bottom pillar positions - Horizontal scroll. """
        # Move pillars to the left.
        self.x_top -= self.settings.ground_animation_speed
        self.x_btm -= self.settings.ground_animation_speed

        # Set new rect.x position.
        self.bottom_pillar_rect.x = self.x_btm
        self.top_pillar_rect.x = self.x_top

    def draw_pillars(self):
        """ Blit pillar images. """
        self.screen.blit(self.bottom_pillar, self.bottom_pillar_rect)
        self.screen.blit(self.top_pillar, self.top_pillar_rect)

    def _resize_pillars(self):
        """ Resize the pillar images appropriate for the game. """
        self.top_pillar = pygame.transform.smoothscale(self.bottom_pillar, (100, 650))
        self.bottom_pillar = pygame.transform.smoothscale(self.bottom_pillar, (100, 650))

    def _set_pillar_position(self):
        """ Randomly generate the pillars positioning on the screen. """

        # Generate a random starting position for top(tp) and bottom(bp) pillars and add a gap between
        # the top and bottom pillars.
        tp_pos = randint(0, 568)
        bp_pos = tp_pos + self.settings.pillar_gap

        # Get pillar rects and set their position.
        self.top_pillar_rect = self.top_pillar.get_rect()
        self.bottom_pillar_rect = self.bottom_pillar.get_rect()
        self.top_pillar_rect.bottomleft = (self.settings.screen_width, tp_pos)
        self.bottom_pillar_rect.topleft = (self.settings.screen_width, bp_pos)

        self.x_btm = float(self.bottom_pillar_rect.x)
        self.x_top = float(self.top_pillar_rect.x)
