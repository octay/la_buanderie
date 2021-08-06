import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, a_settings, screen, ship):
        # cr a bullet in where the ship in
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, a_settings.bullet_width, a_settings.bullet_height)  # cr at (0, 0)
        self.rect.centerx = ship.rect.centerx  # set to correct coordinates
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)  # using float type to store y

        self.color = a_settings.bullet_color
        self.speed_factor = a_settings.bullet_speed_factor

    def update(self):
        # move up
        self.y -= self.speed_factor
        self.rect.y = self.y  # update

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
