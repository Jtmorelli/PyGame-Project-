import sys

import pygame

from settings import Settings


class AlienInvasion:
    # Overall class to manage game assets and behavior

    def __init__(self):
        # Initialized the game, and create game resources
        pygame.init()

        self.settings = Settings()

        # set screen size
        self.screen = pygame.display.set_mode(
            (self.settings.screenwidth, self.settings.screenheight)
        )
        pygame.display.set_caption("Alien Invasion")
        # set backrounf color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # start the main loop for the game
        while True:
            # Watch for ketboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass though the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
