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

        # Load the ground/base image.
        self.ground_img = pygame.image.load('images/ground.png').convert_alpha()
        self.ground_img = pygame.transform.smoothscale(self.ground_img, (1024, 100))

        # Initialise ground attributes needed to continuously scroll the ground image.
        self.ground_img_x = 0
        self.ground_img_x2 = self.ground_img.get_width()

    def update(self):
        """ Update the background images"""
        self._blit_background()

        # Set ground animation speed.
        self.ground_img_x -= self.settings.ground_animation_speed
        self.ground_img_x2 -= self.settings.ground_animation_speed

        # Update ground animation (continuous scroll)
        if self.ground_img_x <= -self.SCREEN_WIDTH:
            self.ground_img_x = self.SCREEN_WIDTH
        if self.ground_img_x2 <= -self.SCREEN_WIDTH:
            self.ground_img_x2 = self.SCREEN_WIDTH

    def _blit_background(self):
        """ Blit background images. """
        self.screen.blit(self.bg_img, self.screen.get_rect())
        self.screen.blit(self.ground_img, (self.ground_img_x, 668))
        self.screen.blit(self.ground_img, (self.ground_img_x2, 668))
