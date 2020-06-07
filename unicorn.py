import pygame
from pygame.sprite import Sprite


class Unicorn(Sprite):
    """ A class to manage an animated unicorn sprite. """

    def __init__(self, game_screen, settings):
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
        for number in range(1, 5):
            file_name = f'images/Unicorn-Fly000{number}.png'
            image = pygame.image.load(file_name).convert_alpha()
            self.images.append(image)

    def update(self):
        current_time = pygame.time.get_ticks()
        animation_elapsed = current_time - self.animation_begin
        if animation_elapsed > 25:
            self.index += 1
            self.animation_begin = current_time
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        if self.jump_count < 10:
            y = float(self.rect.y) - self.settings.jump_speed
            self.rect.y = y
            self.jump_count += 1
        if self.rect.midbottom == self.screen.get_rect().midbottom:
            self.jump_count = 0
        else:
            y = float(self.rect.y) + self.settings.drop_speed
            self.rect.y = y
