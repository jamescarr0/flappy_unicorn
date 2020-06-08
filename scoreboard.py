import pygame


class Scoreboard:
    """ A class to manage player scores. """

    def __init__(self, game):
        """ Constructor. """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.score = 0
        self.scored = False
        self._create_scoreboard()

    def _create_scoreboard(self):
        """ Create a scoreboard image and set position. """
        self.font = pygame.font.SysFont('Arial', 42)
        self.scoreboard_image = self._get_score()
        self.rect = self.scoreboard_image.get_rect()
        self.rect.top = self.screen_rect.top - 20
        self.rect.midtop = self.screen_rect.midtop

        # Add some padding to top the scoreboard
        self.rect.move_ip(0, 20)

    def _get_score(self):
        """ Renders the new score. """
        return self.font.render(str(self.score), True, (0, 0, 0)).convert_alpha()

    def check_score_zone(self, unicorn_group, pillar_group):
        """
            Checks if player is in the score zone.
            Checks unicorn center x position is equal to the pillar x position and sets scored flag True.
        """
        for unicorn in unicorn_group:
            unicorn_rect_x = float(unicorn.rect.centerx)
            for pillar in pillar_group:
                if pillar.rect.x == unicorn_rect_x:
                    self.scored = True

        # Check if player has scored.
        self._has_scored()

    def _has_scored(self):
        """ Checks if score flag is True and responds by incrementing score and resetting flag. """
        if self.scored:
            # If player has scored, increment score and reset flag.
            self.score += 1
            self.scored = False
            print(f"Score: {self.score}")

    def update(self):
        """ Update the scoreboard on screen. """
        self.scoreboard_image = self._get_score()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        """ Blit scoreboard. """
        self.screen.blit(self.scoreboard_image, self.rect)
