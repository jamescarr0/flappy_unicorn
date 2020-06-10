import pygame


class Audio:
    """ A class to set audio properties and process playing game sound effect. """
    def __init__(self):
        """ Assign file paths. """
        self.point_scored = 'audio/point.wav'
        self.hit = 'audio/hit.wav'
        self.die = 'audio/die.wav'
        self.wings = 'audio/wings.wav'

    def play_sound(self, effect):
        """ Play sound effect. """
        if effect == 'point_scored':
            file = self.point_scored
        elif effect == 'hit':
            file = self.hit
        elif effect == 'die':
            file = self.die
        elif effect == 'wings':
            file = self.wings

        # Play sound.
        pygame.mixer.Sound(file).play()
