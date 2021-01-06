class GameStats:
    def __init__(self, ai_game):
        # Stats when game is created
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        # stats that can change durring gameplay
        self.ships_left = self.settings.ship_limit