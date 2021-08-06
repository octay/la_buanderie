class GameStats:
    def __init__(self, a_settings):
        self.a_settings = a_settings
        self.game_active = False  # game is not active in the beginning
        self.reset_stats()

        # high score should not be reset
        self.high_score = 0

    def reset_stats(self):
        # init statistics that may change during game running
        self.ships_left = self.a_settings.ship_limit
        self.score = 0
        self.level = 1

    def set_high_score(self, h_s):
        self.high_score = h_s
