import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # a class to represent a single alien in the fleet

    def __init__(self, ai_game):
        # initialize the alien and set its starting position
        super().__init__()
        self.screen = ai_game.screen

        # load alien image and set its rect attribute
        self.image = pygame.image.load(
            "/Users/jake/Desktop/MIS 5322 - Advanced Python/PyGame Project/alien.bmp"
        )
        self.rect = self.image.get_rect()

        # srar each new alien near the top left corner of screnn
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien exact horizontal position
        self.x = float(self.rect.x)
