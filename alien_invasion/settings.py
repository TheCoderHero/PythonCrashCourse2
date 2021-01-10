# Class to hold all game settings
class Settings:
    # Initialize the game settings (STATIC) these don't change
    def __init__(self):
        # Screen Settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30

        # Aliens speed up after each fleet is destroyed
        self.speedup_scale = 1.1
        # Alien point value increases after each level
        self.score_scale = 1.5
        # This function re-initializes settings that change
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        # Fleet direction (1 = R) (-1 = L)
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alein_points = int(self.alien_points * self.score_scale)