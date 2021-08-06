import json
import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


# to deal with mouse and keypress
def check_keydown_events(event, a_settings, screen, stats, score_b, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(a_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        dump_high_score(stats)
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(a_settings, screen, stats, score_b, ship, aliens, bullets)


def fire_bullet(a_settings, screen, ship, bullets):
    if len(bullets) < a_settings.bullets_allowed:  # limitation
        # cr a bullet and add to bullets
        new_bullet = Bullet(a_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(a_settings, screen, stats, score_b, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dump_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, a_settings, screen, stats, score_b, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(a_settings, screen, stats, score_b, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def start_game(a_settings, screen, stats, score_b, ship, aliens, bullets):
    a_settings.initialize_dynamic_settings()  # reset when new game
    pygame.mouse.set_visible(False)  # hide mouse
    stats.reset_stats()
    stats.game_active = True

    score_b.prep_image()

    aliens.empty()
    bullets.empty()
    create_fleet(a_settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(a_settings, screen, stats, score_b, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  # in certain space and game_active is False
        start_game(a_settings, screen, stats, score_b, ship, aliens, bullets)


# update screen and cut in new screen
def update_screen(a_settings, screen, stats, score_b, ship, aliens, bullets, play_button):
    screen.fill(a_settings.bg_color)  # fill screen with this color in every loop
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score_b.show_score()  # show score after settlement when other operations in every loop completed

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()  # make screen visible


def update_bullet(a_settings, screen, stats, score_b, ship, aliens, bullets):
    # update all bullets' location
    bullets.update()

    # del disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # check if the bullet hit
    check_bullet_alien_collisions(a_settings, screen, stats, score_b, ship, aliens, bullets)


def check_bullet_alien_collisions(a_settings, screen, stats, score_b, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # collisions : dict
    if collisions:
        for aliens in collisions.values():  # every value or aliens : list
            stats.score += a_settings.alien_points * len(aliens)
            score_b.prep_score()
        check_high_score(stats, score_b)

    if len(aliens) == 0:
        bullets.empty()  # del all remained bullets

        a_settings.increase_speed()  # speed up
        stats.level += 1  # level up
        score_b.prep_level()

        create_fleet(a_settings, screen, ship, aliens)


def check_fleet_edges(a_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(a_settings, aliens)
            break


def change_fleet_direction(a_settings, aliens):
    # if certain alien is in edge move down and change direction
    for alien in aliens.sprites():
        alien.rect.y += a_settings.fleet_drop_speed
    a_settings.fleet_direction *= -1


def ship_hit(a_settings, stats, screen, score_b, ship, aliens, bullets):
    if stats.ships_left > 0:  # one ship at least game continues
        stats.ships_left -= 1
        score_b.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(a_settings, screen, ship, aliens)  # recreate aliens
        ship.center_ship()  # arrange ship like operation in __init__

        sleep(0.5)  # pause
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # show mouse


def check_aliens_bottom(a_settings, stats, screen, score_b, ship, aliens, bullets):
    # check if alien reaches the bottom
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # operation like alien hits ship
            ship_hit(a_settings, stats, screen, score_b, ship, aliens, bullets)
            break


def update_aliens(a_settings, stats, screen, score_b, ship, aliens, bullets):
    check_fleet_edges(a_settings, aliens)  # check if is in edge
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):  # check if alien hits ship
        ship_hit(a_settings, stats, screen, score_b, ship, aliens, bullets)

    check_aliens_bottom(a_settings, stats, screen, score_b, ship, aliens, bullets)  # check if alien reaches the bottom


def get_number_alien_x(a_settings, alien_width):
    available_space_x = a_settings.screen_width - 2 * alien_width
    # why - 2 * alien_width ? due to the __init__ of Alien
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(a_settings, ship_height, alien_height):
    available_space_y = (a_settings.screen_height - (3 * alien_height) - ship_height)
    # available_space_y = a_settings.screen_height - 3 * alien_height - ship_height
    # vertical space needs to take into account the ship height and alien height and alien spacing
    # Leave blank above the ship for player
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(a_settings, screen, aliens, alien_number, row_number):
    alien = Alien(a_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(a_settings, screen, ship, aliens):
    # cr one alien and cal the number of aliens in one row first
    # the spacing is the width of bmp
    alien = Alien(a_settings, screen)
    number_alien_x = get_number_alien_x(a_settings, alien.rect.width)
    number_rows = get_number_rows(a_settings, ship.rect.height, alien.rect.height)

    # cr one row
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(a_settings, screen, aliens, alien_number, row_number)


def check_high_score(stats, score_b):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_b.prep_high_score()


# load and store high score
def load_high_score(stats):
    try:
        with open('data/high_score.json', 'r') as j_f:
            high_score = json.load(j_f)
    except FileNotFoundError:
        return
    else:
        stats.set_high_score(high_score)


def dump_high_score(stats):
    with open('data/high_score.json', 'w') as j_f:
        json.dump(stats.high_score, j_f)
