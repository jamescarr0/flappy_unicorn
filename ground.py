import pygame


class Ground:
    """ A class to manage the scrolling ground.  """

    def __init__(self, game):
        """ Constructor. """
        # Initialise game attributes.
        self.settings = game.settings
        self.screen = game.screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.settings.screen_width, self.settings.screen_height

        # Load the ground/base image.
        self.ground_img = pygame.image.load('images/game/ground.png').convert_alpha()
        self.ground_img = pygame.transform.smoothscale(self.ground_img, (1024, 100))

        # Initialise ground attributes needed to continuously scroll the ground image.
        self.ground_img_x = 0
        self.ground_img_x2 = self.ground_img.get_width()

    def update(self):
        """ Update the ground image. """
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
        """ Blit ground images. """

        self.screen.blit(self.ground_img, (self.ground_img_x, 700))
        self.screen.blit(self.ground_img, (self.ground_img_x2, 700))
