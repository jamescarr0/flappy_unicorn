import sys
import pygame

from background import Background
from settings import Settings
from unicorn import Unicorn
from cloud import Cloud
from pillar_top import PillarTop
from pillar_bottom import PillarBottom


class FlappyUnicorn:
    """ A general class to manage the game. """
    def __init__(self):
        """ Constructor """
        pygame.init()
        self.pillar_time_elapsed = 0
        self.cloud_time_elapsed = 0
        self.clock_tick = 0

        # Initialise settings
        self.settings = Settings()

        # Set screen dimensions.
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = self.settings.screen_height, self.settings.screen_width
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Create an animated flying unicorn
        self.unicorn = Unicorn(self.screen, self.settings)
        self.unicorn_sprite = pygame.sprite.Group(self.unicorn)

        # Create the background
        self.background = Background(self)

        # Create cloud.
        self.clouds = pygame.sprite.Group()

        # Create pillar obstacles.
        self.pillars = pygame.sprite.Group()

    def run(self):
        """ Main game loop. """

        # Create clock to track time.
        clock = pygame.time.Clock()

        while True:
            # Check key pressed events.
            self._check_key_events()
            self._check_pillars()
            self._check_clouds()
            #self._check_unicorn_collision()
            self._update_screen()

            # Update clock and time elapsed.
            self.pillar_time_elapsed += clock.get_time()
            self.cloud_time_elapsed += clock.get_time()
            clock.tick(60)

    def _check_unicorn_collision(self):
        """ Respond to unicorn collision. """
        if pygame.sprite.spritecollideany(self.unicorn_sprite, self.pillars):
            print("COLLIDE")

    def _check_clouds(self):
        """ Manage clouds on screen. """

        if self.cloud_time_elapsed > self.settings.cloud_frequency and len(self.clouds) < self.settings.cloud_qty:
            self.cloud_time_elapsed = 0
            new_cloud = Cloud(self)
            self.clouds.add(new_cloud)

        self._check_cloud_edges()

    def _check_cloud_edges(self):
        """ Loop through cloud sprites and check if cloud is still on screen.
            Remove clouds that have scrolled off the display.
        """
        for cloud in self.clouds.copy():
            if cloud.cloud_rect.right <= 0:
                self.clouds.remove(cloud)

    def _check_pillars(self):
        """ A method that manages the pillar obstacles. """

        if self.pillar_time_elapsed > self.settings.pillar_frequency:
            # If a certain time has elapsed (settings.pillar_frequency) create a new pillar.
            self.pillar_time_elapsed = 0
            self._create_pillar()

        self._check_pillar_edges()

    def _check_pillar_edges(self):
        """
            Loop through the group of pillar sprites and check their right edge.
            Remove pillar sprites that have left the screen.
        """
        for pillar in self.pillars.copy():
            if pillar.rect.right <= 0:
                self.pillars.remove(pillar)

    def _create_pillar(self):
        """ Create a new pillar object and add to the pillar sprite group. """
        top_pillar = PillarTop(self)
        bottom_pillar = PillarBottom(self, top_pillar.rect)
        pillars = [top_pillar, bottom_pillar]
        self.pillars.add(*pillars)

    def _check_key_events(self):
        """ Check for key pressed events. """
        for event in pygame.event.get():
            # Quit / Exit game.
            if event.type == pygame.QUIT:
                sys.exit(0)

            # Key pressed down.
            if event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

    def _check_key_down_events(self, event):
        """ Respond to a key pressed down event. """
        if event.key == pygame.K_SPACE:
            self.unicorn.jump_count = 0
        elif event.key == pygame.K_q:
            sys.exit(0)

    def _update_screen(self):
        """ Update surfaces and flip screen. """
        # Update background images.
        self.background.update()
        self.clouds.update()
        self.pillars.update()

        # Draw the pillar sprites that have been added to the pillar sprite group.
        for pillar in self.pillars.sprites():
            pillar.draw_pillars()

        # Update unicorn position and animation.
        self.unicorn_sprite.update()
        self.unicorn_sprite.draw(self.screen)

        # Update clouds.
        for cloud in self.clouds.sprites():
            cloud.draw_cloud()

        # Flip the new display to screen.
        pygame.display.flip()


# Run the game.
if __name__ == '__main__':
    unicorn_game = FlappyUnicorn()
    unicorn_game.run()
