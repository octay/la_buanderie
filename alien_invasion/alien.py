import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, a_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.a_settings = a_settings

        # load bmp of ship and rectangle of surface
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # init every alien in the top left of screen
        # at here set the distance to edge or spacing the width and height of bmp
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # using float type to store x

    def check_edges(self):
        # if is in edge return True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # move right
        self.x += self.a_settings.alien_speed_factor * self.a_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
