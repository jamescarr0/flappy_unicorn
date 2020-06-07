import pygame


class Cloud:
    """ A class to manage a cloud. """
    def __init__(self, screen, settings):
        """ Constructor. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Load a cloud image.
        self.cloud_image = pygame.image.load('images/clouds5.png').convert_alpha()
        self.rect = self.cloud_image.get_rect()
        self.rect.centerx = self.screen.get_width()
        self.x = float(self.rect.x)

    def update(self):
        """ Update the clouds position and blit. """
        self.x -= self.settings.cloud_speed
        self.rect.x = self.x
        self.blit_me()

    def blit_me(self):
        """ Blit cloud to screen. """
        self.screen.blit(self.cloud_image, self.rect)
