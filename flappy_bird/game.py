import pygame

import func
from materials import Materials as Ms
from settings import Settings

pygame.init()
a_settings = Settings()
ms = Ms(a_settings)
SCREEN = pygame.display.set_mode((a_settings.screen_width, a_settings.screen_height))
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()


def run_game():
    while 1:
        ms.pre_game()
        ms.start_w.play()
        func.menu_window(SCREEN, CLOCK, ms, a_settings)
        result = func.game_window(SCREEN, CLOCK, ms, a_settings)
        func.end_window(SCREEN, CLOCK, ms, a_settings, result)


run_game()
