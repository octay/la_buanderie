import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    a_settings = Settings()
    screen = pygame.display.set_mode((a_settings.screen_width, a_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(a_settings, screen, "Play")
    stats = GameStats(a_settings)  # store statistics
    gf.load_high_score(stats)  # load high score if exists in json data file
    score_b = Scoreboard(a_settings, screen, stats)
    ship = Ship(a_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(a_settings, screen, ship, aliens)  # cr aliens group

    while 1:
        gf.check_events(a_settings, screen, stats, score_b, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullet(a_settings, screen, stats, score_b, ship, aliens, bullets)
            gf.update_aliens(a_settings, stats, screen, score_b, ship, aliens, bullets)

        gf.update_screen(a_settings, screen, stats, score_b, ship, aliens, bullets, play_button)


run_game()
