class Settings:
    """ A general class to manage the games settings. """
    def __init__(self):
        """ Constructor. """

        # Screen settings.
        self.screen_height = 768
        self.screen_width = 1024

        # Background settings
        self.ground_animation_speed = 2

        # Unicorn settings.
        self.jump_speed = 18
        self.drop_speed = 8

        # Pillar obstacle settings.
        self.pillar_frequency = 3000
        self.pillar_gap = 200

        # Cloud settings.
        self.cloud_frequency = 4500
        self.cloud_qty = 3
