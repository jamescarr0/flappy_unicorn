import pygame


class TextImage:
    """A class to render text as an image. """
    def __init__(self, screen, text, size, text_color=(237, 93, 183)):
        """ Constructor. """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font('fonts/UnicornMagic-OVML6.ttf', size)
        self.text_img = self._render_text().convert_alpha()
        self.rect = self.text_img.get_rect()
        self.rect.center = self.screen_rect.center

    def _render_text(self, *text):
        """ Render text and return an image. """
        return self.font.render(self.text, True, self.text_color)

    def change_position(self, width, height):
        """
        (width, height)
        Moves the rect in place.  Starting point is center of screen.
        """
        self.rect.move_ip(width, height)

    def blit_me(self):
        """ Blit to screen"""
        self.screen.blit(self.text_img, self.rect)
