import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    def __init__(self, a_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.a_settings = a_settings
        self.stats = stats

        # font of score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare image of score
        self.prep_image()

    def prep_image(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        # trans score to image
        rounded_score = int(round(self.stats.score, 0))  # plain pc game so just round(x, 0)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.a_settings.bg_color)

        # set top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20  # never forget to remain spacing

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, 0))  # plain pc game so just round(x, 0)
        high_score_str = 'high score : ' + "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.a_settings.bg_color)

        # set below score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.score_rect.right
        self.high_score_rect.top = self.score_rect.bottom + 10

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.a_settings.bg_color)

        # set below high score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.high_score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.a_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
