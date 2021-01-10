class GameStats:
    def __init__(self, ai_game):
        # Stats when game is created
        self.game_active = False
        self.settings = ai_game.settings
        self.reset_stats()
        with open('highscore.txt') as file_object:
            high_score = file_object.read()
        self.high_score = int(high_score)
        self.highest_score = int(high_score)

    def reset_stats(self):
        # stats that can change durring gameplay
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1