import pygame
from text_image import TextImage

class StartScreen:
    """ Start game screen. """
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.unicorn_img = pygame.transform.smoothscale(
            pygame.image.load('images/game/Unicorn.png').convert_alpha(), (345, 397))
        self.rect = self.unicorn_img.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.rect.move_ip(30, -30)

        self.title = TextImage(game.screen, "FlAppy UnIcQrn", size=100)
        self.title.change_position(0, -200)

        self.start_button = TextImage(game.screen, text="sTaRt", size=50, text_color=(255, 255, 255))

        self.index = 0
        self.past_time = 0

    def blit_me(self):
        self.start_button.blit_me()
        self.title.blit_me()
        self.screen.blit(self.unicorn_img, self.rect)
