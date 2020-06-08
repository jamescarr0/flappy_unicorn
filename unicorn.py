import pygame
from pygame.sprite import Sprite


class Unicorn(Sprite):
    """ A class to manage an animated unicorn sprite. """

    def __init__(self, game_screen, settings):
        """ Constructor. """
        super().__init__()
        self.screen = game_screen
        self.settings = settings
        self.jump_count = 10
        self.animation_begin = pygame.time.get_ticks()
        self.images = []
        self._load_unicorn_images()
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (200, 350)

    def _load_unicorn_images(self):
        """ Load the unicorn images and append to image list. """
        for number in range(1, 5):
            file_name = f'images/Unicorn-Fly000{number}.png'
            image = pygame.image.load(file_name).convert_alpha()
            self.images.append(image)

    def update(self):
        """
            Animate the unicorn by iterating through the image list.
            Update unicorn Y position.
        """
        self._animate_unicorn()
        self._update_position()

    def _update_position(self):
        """ Update the unicorn Y position. """

        if self.jump_count < 10:
            y = float(self.rect.y) - self.settings.jump_speed
            self.rect.y = y
            self.jump_count += 1

        else:
            y = float(self.rect.y) + self.settings.drop_speed
            self.rect.y = y

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
