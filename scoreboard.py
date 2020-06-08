class Scoreboard:
    """ A class to manage player scores. """

    def __init__(self):
        self.score = 0
        self.scored = False

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
