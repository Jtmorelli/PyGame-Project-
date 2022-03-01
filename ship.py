import pygame


class Ship:
    # a class to manage the ship

    def __init__(self, ai_game):
        # initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image and get its rect

        self.image = pygame.image.load(
            "/Users/jake/Desktop/MIS 5322 - Advanced Python/PyGame Project/ship.bmp"
        )
        self.rect = self.image.get_rect()

        # start a new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ships horizontal positon
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update the ships postion based on the movement flag
        # update the ships x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
