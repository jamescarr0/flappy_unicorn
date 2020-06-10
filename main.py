import sys
import pygame


from start_screen import StartScreen
from background import Background
from settings import Settings
from unicorn import Unicorn
from cloud import Cloud
from pillar_top import PillarTop
from pillar_bottom import PillarBottom
from ground import Ground
from scoreboard import Scoreboard
from audio import Audio
from game_over import GameOver


class FlappyUnicorn:
    """ A general class to manage the game. """
    def __init__(self):
        """ Constructor """
        pygame.init()
        pygame.mixer.init()

        # Load game icon
        self.game_icon = pygame.image.load('images/game/icon.png')
        pygame.display.set_icon(self.game_icon)

        self.settings = Settings()

        # Set screen dimensions.
        self.SCREEN_HEIGHT, self.SCREEN_WIDTH = self.settings.screen_height, self.settings.screen_width
        pygame.display.set_caption("Flappy Unicorn")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        self.game_active = False
        self.game_over = False

        self.pillar_time_elapsed = 0
        self.cloud_time_elapsed = 0
        self.clock_tick = 0

        # Audio instance.
        self.audio = Audio()

        # Create start and game over screens.
        self.start_screen = StartScreen(self)
        self.game_over_screen = GameOver(self)

        # Create an animated flying unicorn
        self.unicorn = Unicorn(self)
        self.unicorn_sprite = pygame.sprite.Group(self.unicorn)

        # Create the background
        self.background = Background(self)

        # Create ground.
        self.ground = Ground(self)

        # Create cloud.
        self.clouds = pygame.sprite.Group()

        # Create pillar sprite group.
        self.pillars = pygame.sprite.Group()

        # Create the scoreboard.
        self.scoreboard = Scoreboard(self)

    def run(self):
        """ Main game loop. """

        # Create clock to track time.
        clock = pygame.time.Clock()

        while True:
            # Check key pressed events.
            self._check_key_events()
            self._update_screen()

            # Update clock and time elapsed.
            self.pillar_time_elapsed += clock.get_time()
            self.cloud_time_elapsed += clock.get_time()

            clock.tick(60)

    def _check_key_events(self):
        """ Check for key pressed events. """
        for event in pygame.event.get():
            # Quit / Exit game.
            if event.type == pygame.QUIT:
                sys.exit(0)

            # Key pressed event.
            if event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

            # Mouse clicked event.
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_button_clicked(mouse_position)

    def _check_key_down_events(self, event):
        """ Respond to a key pressed down event. """

        if not self.game_over and not self.start_screen.screen_active:
            if event.key == pygame.K_SPACE:
                self.unicorn.jump_count = 0
                self.audio.play_sound('wings')

        elif event.key == pygame.K_q:
            sys.exit(0)

        elif event.key == pygame.K_p:
            self.game_active = True
            self.start_screen.screen_active = False

    def _check_button_clicked(self, mouse_position):
        """ Check if player clicked a button and process request. """

        # Start game button
        if self.start_screen.start_button.rect.collidepoint(mouse_position):
            self.game_active = True
            self.start_screen.screen_active = False
            pygame.mouse.set_visible(False)

        # Retry Button
        if self.game_over_screen.retry_button.rect.collidepoint(mouse_position):
            self.restart()

    def _check_unicorn_collision(self):
        """ Respond to a collision event. """

        for unicorn in self.unicorn_sprite:
            if unicorn.rect.bottom >= self.settings.gnd_col_zone or unicorn.rect.top <= self.screen_rect.top:
                self._game_over_loop()
                self.audio.play_sound('hit')
                return

        obstacle_collision = pygame.sprite.groupcollide(self.unicorn_sprite, self.pillars, False, False)
        if obstacle_collision:
            self._game_over_loop()
            self.audio.play_sound('hit')

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
        for cloud in self.clouds:
            if cloud.cloud_rect.right <= 0:
                self.clouds.remove(cloud)

    def _create_pillar(self):
        """ Create a new pillar object and add to the pillar sprite group. """
        top_pillar = PillarTop(self)
        bottom_pillar = PillarBottom(self, top_pillar.rect)
        pillars = [top_pillar, bottom_pillar]
        self.pillars.add(*pillars)

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

    def _perform_checks(self):
        """ Check sprite positions. """

        self._check_pillars()
        self._check_clouds()
        self._check_unicorn_collision()
        self.scoreboard.check_score_zone(self.unicorn_sprite, self.pillars)

    def _update_screen(self):
        """ Update surfaces and flip screen. """

        # Update background image.
        self.background.update()

        if self.game_active:
            self._perform_checks()
            self.scoreboard.update()

            # Draw the pillar sprites that have been added to the pillar sprite group.
            for pillar in self.pillars.sprites():
                pillar.draw_pillars()

            # Update unicorn position and animation.
            self.unicorn_sprite.update()
            self.unicorn_sprite.draw(self.screen)

            # Draw new clouds to screen.
            for cloud in self.clouds.sprites():
                cloud.draw_cloud()

            if not self.game_over:
                # Update scrolling ground position.
                self.ground.update()
                # Update clouds position
                self.clouds.update()
                # Update pillar position
                self.pillars.update()

        elif not self.game_over:
            # Start Screen.
            self.ground.blit_background(start_screen=True)
            self.start_screen.blit_me()
        else:
            self._game_over_loop()

        # Flip the new display to screen.
        pygame.display.flip()

    def _game_over_loop(self):
        """
            Halt game blit game over and retry button to screen.
            Enable mouse cursor.
        """
        self.game_over = True
        self.game_active = False

        if self.unicorn.rect.bottom >= self.screen_rect.bottom:
            self.unicorn.rect.bottom = self.screen_rect.bottom

        self.unicorn_sprite.update(animation=False)
        self.unicorn_sprite.draw(self.screen)
        self.pillars.draw(self.screen)
        self.ground.blit_background()
        self.scoreboard.update()
        self.game_over_screen.blit_me()

        # Enable mouse cursor.
        pygame.mouse.set_visible(True)

    def restart(self):
        """ Reset game attributes and start a new game. """
        self.pillars.empty()
        self.clouds.empty()
        self.unicorn.reset_rect()
        self.scoreboard.score = 0
        self.pillar_time_elapsed = 0
        self.cloud_time_elapsed = 0
        self.game_over = False
        self.game_active = True
        pygame.mouse.set_visible(False)


# Run the game.
if __name__ == '__main__':
    unicorn_game = FlappyUnicorn()
    unicorn_game.run()
