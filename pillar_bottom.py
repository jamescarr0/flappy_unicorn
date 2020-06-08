import pygame
from pygame.sprite import Sprite
from random import randint


class PillarBottom(Sprite):
    """ A class to manage the pillar obstacle. """
    def __init__(self, game, top_pillar_rect):
        """ Constructor. """
        super().__init__()  # Call superclass.
        self.screen = game.screen
        self.settings = game.settings
        self.top_pillar_rect = top_pillar_rect

        # Load bottom pillar image.
        self.image = pygame.image.load('images/Pillar1.png').convert_alpha()

        # Resize the image.
        self._resize_pillars()

        # Set image rect
        self.rect = self.image.get_rect()

        # Randomly get a pillar gap for sprite to fly through to vary difficulty.
        self.pillar_gap = randint(190, 300)

        # Set pillar starting position.
        self._set_pillar_position()

    def update(self):
        """ Update top and bottom pillar positions - Horizontal scroll. """
        # Move pillar to the left.
        self.rect.x -= self.settings.ground_animation_speed

    def draw_pillars(self):
        """ Blit pillar image. """
        self.screen.blit(self.image, self.rect)

    def _resize_pillars(self):
        """ Resize the pillar image appropriate for the game. """
        self.image = pygame.transform.smoothscale(self.image, (100, 650))

    def _set_pillar_position(self):
        """ Randomly generate the pillars positioning on the screen. """

        # Set the top pillar to meet the bottom pillar, then move the bottom
        # pillar to create a gap.
        self.rect.topleft = self.top_pillar_rect.bottomleft
        pygame.Rect.move_ip(self.rect, 0, self.pillar_gap)
