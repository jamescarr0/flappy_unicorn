class Settings:
    """ A general class to manage the games settings. """
    def __init__(self):
        """ Constructor. """

        # Screen settings.
        self.screen_height = 768
        self.screen_width = 1024

        # Background settings
        self.ground_animation_speed = 4

        # Unicorn settings.
        self.start_position = (200, 200)
        self.jump_speed = 12
        self.drop_speed = 8

        # Pillar obstacle settings.
        self.pillar_frequency = 3000

        # Cloud settings.
        self.cloud_frequency = 4500
        self.cloud_qty = 3

        # Game over settings
        self.game_over_text = "Game Over!"
        self.game_over_color = (0, 0, 0)
        self.retry_button_text = "rEtRy"

        # Collision settings
        # height of the ground collision zone.
        self.gnd_col_zone = 735
