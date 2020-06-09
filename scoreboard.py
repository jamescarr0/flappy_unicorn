import pygame


class Scoreboard:
    """ A class to manage player scores. """

    def __init__(self, game):
        """ Constructor. """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.audio = game.audio
        self.score = 0
        self.scored = False
        self._create_scoreboard()

    def _create_scoreboard(self):
        """ Create a scoreboard image and set position. """
        self.scoreboard_image = self._get_scoreboard_image()
        self.rect = self.scoreboard_image.get_rect()
        self.rect.top = self.screen_rect.top - 20
        self.rect.midtop = self.screen_rect.midtop

        # Add some padding to top the scoreboard
        self.rect.move_ip(0, 20)

    def _get_scoreboard_image(self):
        """
            Get the current score and return a scoreboard image.
        """
        # Convert score to string.
        score = str(self.score)
        score_img = []
        # Iterate through the score string and load corresponding images and append to image list.
        for number in score:
            score_img.append(pygame.image.load(f'images/score/{number}.png'))

        # Concatenate the number images on the screen.
        new_image = self._concatenate_score_img(score_img)
        return new_image

    def _concatenate_score_img(self, img_list):
        """
            Blit multiple number images to the same surface.
            Move image rects so they stack horizontal.
        """
        new_image = pygame.Surface((50, 40))
        position = 0
        for img in img_list:
            img_rect = img.get_rect()
            img_rect.move_ip((position * 24), 0)
            new_image.blit(img, img_rect)
            position += 1
        return new_image

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
            self.audio.play_sound('point_scored')

    def update(self):
        """ Update the scoreboard on screen. """
        self.scoreboard_image = self._get_scoreboard_image()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        """ Blit scoreboard. """
        self.screen.blit(self.scoreboard_image, self.rect)
