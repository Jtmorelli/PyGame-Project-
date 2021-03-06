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

    def prep_score(self):
        # turn score into image
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # draw score to screen
        self.screen.blit(self.score_image, self.score_rect)
