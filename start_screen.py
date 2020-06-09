import pygame


class StartScreen:
    """ Start game screen. """
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.unicorn_img = pygame.transform.smoothscale(
            pygame.image.load('images/game/Unicorn.png').convert_alpha(), (345, 397))
        self.rect = self._get_rect()
        self.index = 0
        self.past_time = 0

    def _get_rect(self):
        screen_rect = self.screen.get_rect()
        img_rect = self.unicorn_img.get_rect()
        img_rect.bottomleft = screen_rect.bottomleft
        img_rect.move_ip(30, -30)
        return img_rect

    def blit_me(self):
        self.screen.blit(self.unicorn_img, self.rect)
