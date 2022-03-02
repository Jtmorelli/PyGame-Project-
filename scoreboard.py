import pygame.font


class Scoreboard:
    # a class to report score
    def __init__(self, ai_game):
        # start scoring
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the inital score image
        self.prep_score()
