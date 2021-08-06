import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, a_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.a_settings = a_settings

        # load bmp of ship and rectangle of surface
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set every new ship in bottom half or center of bottom specifically
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float type or decimal number in center parameter
        # using this extra parameter bcuz of rect.centerx store int only
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # updating location according to the flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.a_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.a_settings.ship_speed_factor

        # update rect refer to self.center parameter
        self.rect.centerx = self.center

    def blitme(self):
        # show it in the specified coordinate
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
