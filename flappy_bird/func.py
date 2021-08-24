import time

import pygame

from bird import Bird
from pipe import Pipe


def arrange_m(screen, ms, a_settings):
    ms.move_floor()
    ms.move_bird()
    ms.change_frame_idx()

    screen.blit(ms.images['bg'], (0, 0))  # background
    screen.blit(ms.images['floor'], (ms.get_floor_x(), ms.floor_y))
    screen.blit(ms.images['guide'], (ms.guide_x, ms.guide_y))
    screen.blit(ms.images['birds'][a_settings.bird_frames[ms.get_frame_idx()]],
                (ms.bird_menu_x, ms.bird_menu_y + ms.get_bird_y_hen()))


def arrange_g(screen, ms, a_settings, bird, flap, pipe_group, score):
    ms.move_floor()

    bird.update(flap)

    check_pipe_out(ms, a_settings, pipe_group)

    pipe_group.update()

    screen.blit(ms.images['bg'], (0, 0))
    pipe_group.draw(screen)
    screen.blit(ms.images['floor'], (ms.get_floor_x(), ms.floor_y))
    screen.blit(bird.get_image(), bird.get_coordinates())
    show_score(screen, ms, a_settings, score)


def arrange_e(screen, ms, a_settings, result):
    # ms.move_floor()
    result['bird'].when_die()
    screen.blit(ms.images['bg'], (0, 0))
    result['pipe_group'].draw(screen)
    screen.blit(ms.images['floor'], (ms.get_floor_x(), ms.floor_y))
    screen.blit(ms.images['gameover'], (ms.gameover_x, ms.gameover_y))
    screen.blit(result['bird'].get_image(), result['bird'].get_coordinates())
    show_score(screen, ms, a_settings, result['score'])


def check_pipe_out(ms, a_settings, pipe_group):
    first_pipe_up = pipe_group.sprites()[0]
    first_pipe_down = pipe_group.sprites()[1]
    if first_pipe_up.get_rect_right() < 0:
        pipe_y = ms.get_pipe_y_random()
        pipe_gap = ms.get_pipe_gap_random()
        new_pipe_up = Pipe(ms, a_settings, first_pipe_up.get_rect_x() + a_settings.pipe_n * a_settings.pipe_d, pipe_y)
        new_pipe_down = Pipe(ms, a_settings, first_pipe_up.get_rect_x() + a_settings.pipe_n * a_settings.pipe_d,
                             pipe_y - pipe_gap, False)
        pipe_group.add(new_pipe_up)
        pipe_group.add(new_pipe_down)
        first_pipe_up.kill()
        first_pipe_down.kill()


def show_score(screen, ms, a_settings, score):
    score_str = str(score)
    num_show_width = ms.num_show_width
    num_show_x = (a_settings.screen_width - len(score_str) * num_show_width) / 2
    for number in score_str:
        screen.blit(ms.images[number], (num_show_x, ms.num_show_y))
        num_show_x += num_show_width


def menu_window(screen, clock, ms, a_settings):
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit(0)
                elif event.key == pygame.K_SPACE:
                    return

        arrange_m(screen, ms, a_settings)  # arrange materials in menu window

        pygame.display.update()
        clock.tick(a_settings.fps)


def game_window(screen, clock, ms, a_settings):
    ms.flap_w.play()
    bird = Bird(ms, a_settings)
    pipe_group = pygame.sprite.Group()

    gen_pipes(ms, a_settings, pipe_group)

    score = 0

    while 1:
        flap = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit(0)
                elif event.key == pygame.K_SPACE:
                    flap = True
                    ms.flap_w.play()

        arrange_g(screen, ms, a_settings, bird, flap, pipe_group, score)

        if bird.rect.y > ms.floor_y or bird.rect.y < 0 or pygame.sprite.spritecollideany(bird, pipe_group):
            # check if collision
            ms.hit_w.play()
            ms.die_w.play()
            result = {'bird': bird, 'pipe_group': pipe_group, 'score': score}
            return result

        if bird.rect.left + a_settings.pipe_v < pipe_group.sprites()[0].rect.centerx < bird.rect.left:
            # when bird cross the centerx
            ms.score_w.play()
            score += a_settings.each_score

        pygame.display.update()
        clock.tick(a_settings.fps)


def gen_pipes(ms, a_settings, pipe_group):
    for i in range(a_settings.pipe_n):
        pipe_y = ms.get_pipe_y_random()
        pipe_gap = ms.get_pipe_gap_random()
        pipe_up = Pipe(ms, a_settings, a_settings.screen_width + i * a_settings.pipe_d, pipe_y)
        pipe_down = Pipe(ms, a_settings, a_settings.screen_width + i * a_settings.pipe_d, pipe_y - pipe_gap,
                         False)
        pipe_group.add(pipe_up)
        pipe_group.add(pipe_down)


def end_window(screen, clock, ms, a_settings, result):
    time_start = time.time()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit(0)
                elif event.key == pygame.K_SPACE and time.time() - time_start > a_settings.end_remain:
                    # return but only after min time which is for gamer to check score
                    return

        arrange_e(screen, ms, a_settings, result)

        pygame.display.update()
        clock.tick(a_settings.fps)
