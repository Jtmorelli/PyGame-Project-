class GameStats:
    # tract statistics for alien invasion

    def __init__(self, ai_game):
        # initialize stats
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in an iactive state
        self.game_active = False

    def reset_stats(self):
        # initialized stats that can change furing game
        self.ships_left = self.settings.ship_limit
        self.score = 0
