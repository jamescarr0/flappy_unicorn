import pygame
from pygame.sprite import Sprite
import time

class Unicorn(Sprite):
    """ A class to manage an animated unicorn sprite. """

    def __init__(self, game):
        """ Constructor. """

        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.audio = game.audio
        self.jump_count = 10
        self.animation_begin = pygame.time.get_ticks()
        self.images = []
        self._load_unicorn_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.settings.start_position

    def reset_rect(self):
        self.rect.center = self.settings.start_position

    def _load_unicorn_images(self):
        """ Load the unicorn images and append to image list. """
        for number in range(1, 5):
            file_name = f'images/game/Unicorn-Fly000{number}.png'
            image = pygame.image.load(file_name).convert_alpha()
            self.images.append(image)

    def _update_position(self):
        """ Update the unicorn Y position. """

        if self.jump_count < 10:
            y = float(self.rect.y) - self.settings.jump_speed
            self.rect.y = y
            self.jump_count += 1

        self.rect.y += self.settings.drop_speed

    def _animate_unicorn(self):
        """ Animate the unicorn """

        # Control the speed of unicorn sprite animation.
        current_time = pygame.time.get_ticks()
        animation_elapsed = current_time - self.animation_begin

        if animation_elapsed > 25:
            self.index += 1
            self.animation_begin = current_time

            # Once the end of the image list has been reached, reset [index] to 0.
            if self.index >= len(self.images):
                self.index = 0

            # Change the image.
            self.image = self.images[self.index]

    def update(self, animation=True):
        """
            Animate the unicorn by iterating through the image list.
            Update unicorn Y position.
        """
        if animation:
            self._animate_unicorn()
        self._update_position()

