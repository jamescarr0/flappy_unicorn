import pygame
from pygame.sprite import Sprite
from random import randint


class PillarTop(Sprite):
    """ A class to manage the top pillar obstacle. """
    def __init__(self, game):
        """ Constructor. """
        super().__init__()  # Call superclass.
        self.screen = game.screen
        self.settings = game.settings

        # Load top pillar image
        self.image = self.bottom_pillar = pygame.image.load('images/game/Pillar1.png').convert_alpha()

        # Resize the images
        self._resize_pillars()

        # Get image rect
        self.rect = self.image.get_rect()

        # Set pillar starting position.
        self._set_pillar_position()

    def update(self):
        """ Update top and bottom pillar positions - Horizontal scroll. """
        # Move pillars to the left.
        self.rect.x -= self.settings.ground_animation_speed

    def draw_pillars(self):
        """ Blit image. """
        self.screen.blit(self.image, self.rect)

    def _resize_pillars(self):
        """ Resize the pillar image appropriate for the game. """
        self.image = pygame.transform.smoothscale(self.bottom_pillar, (100, 650))

    def _set_pillar_position(self):
        """ Randomly generate the pillar position on the screen. """

        # Generate a random x starting
        maximum_x_postion = 480
        x_position = randint(0, maximum_x_postion)

        # Set rect position
        self.rect.bottomleft = (self.settings.screen_width, x_position)
