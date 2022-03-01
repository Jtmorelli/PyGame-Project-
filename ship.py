import pygame


class Ship:
    # a class to manage the ship

    def __init__(self, ai_game):
        # initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect

        self.image = pygame.image.load(
            "/Users/jake/Desktop/MIS 5322 - Advanced Python/PyGame Project/ship.bmp"
        )
        self.rect = self.image.get_rect()

        # start a new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag
        self.moving_right = False

    def update(self):
        # update the ships postion based on the movement flag
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
