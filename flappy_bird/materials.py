import os
import random

import pygame

'''
Notice:
all func of bird in game window are realized in Bird class
using func in ms class is still necessary in menu window
some func of pipe in game window are realized in Pipe class
func of pipe in ms class are useful as console of basic parameters
'''


class Materials:
    def __init__(self, a_settings):
        self.a_settings = a_settings
        self.init_load_png()  # load images
        self.init_load_music()  # load music
        self.init_materials_coordinates()  # init coordinates
        self.init_sp_values()  # init special value
        self.set_default_random()  # it is meaningless

        self.reset_floor_x()  # floor image is moving so floor_x is a variation
        self.reset_bird_y_hen()  # bird image is moving so bird_menu_y is a variation
        self.reset_frame_idx()

    # load file
    def init_load_png(self):
        # using os
        self.images = {}
        for image in os.listdir('sprites'):
            name, extension = os.path.splitext(image)
            path = os.path.join('sprites', image)
            # images[name + extension.replace('.', '_')] = pygame.image.load(path)
            self.images[name] = pygame.image.load(path)

    def init_load_music(self):
        self.start_w = pygame.mixer.Sound('audio/start.wav')
        self.die_w = pygame.mixer.Sound('audio/die.wav')
        self.hit_w = pygame.mixer.Sound('audio/hit.wav')
        self.score_w = pygame.mixer.Sound('audio/score.wav')
        self.flap_w = pygame.mixer.Sound('audio/flap.wav')

    # init value
    def init_materials_coordinates(self):
        self.floor_y = self.get_floor_y()
        self.guide_x = self.get_guide_x()
        self.guide_y = self.get_guide_y()
        self.bird_menu_x = self.get_bird_menu_x()
        self.bird_menu_y = self.get_bird_menu_y()  # bird_menu_x bird_menu_y only available in menu_window()
        self.gameover_x = self.get_gameover_x()
        self.gameover_y = self.get_gameover_y()
        self.pipe_x = self.get_pipe_x()
        self.pipe_y = self.get_pipe_y()

    def init_sp_values(self):
        self.floor_bg_gap = self.get_floor_bg_gap()
        self.num_width = self.get_num_width()
        self.num_show_width = self.get_num_show_width()
        self.num_show_y = self.get_num_show_y()

    # cal coordinates
    def get_floor_y(self):
        return self.a_settings.screen_height - self.images['floor'].get_height()

    def get_guide_x(self):
        return (self.a_settings.screen_width - self.images['guide'].get_width()) / 2

    def get_guide_y(self):
        return (self.get_floor_y() - self.images['guide'].get_height()) / 2

    def get_bird_menu_x(self):  # never mind the coordinates of bird
        return self.a_settings.screen_width * 0.2

    def get_bird_menu_y(self):
        return (self.a_settings.screen_height - self.images['red-mid'].get_height()) / 2  # every birds png 34 x 24

    def get_gameover_x(self):
        return (self.a_settings.screen_width - self.images['gameover'].get_width()) / 2

    def get_gameover_y(self):
        return (self.get_floor_y() - self.images['gameover'].get_height()) / 2

    def get_pipe_x(self):
        return self.a_settings.screen_width * 0.5

    def get_pipe_y(self):
        return self.a_settings.screen_height * 0.5

    # all values in this function will no be accepted when game running but can be default values when error hassei
    def set_default_random(self):
        self.images['bg'] = self.images['day']
        bird_color = 'red'
        self.images['birds'] = [self.images[bird_color + '-up'], self.images[bird_color + '-mid'],
                                self.images[bird_color + '-down']]
        pipe_color = 'green'
        self.images['pipes'] = [self.images[pipe_color + '-pipe'],
                                pygame.transform.flip(self.images[pipe_color + '-pipe'], False, True)]

    # when start a new game we should random the background and the color of bird
    def random_while_start(self):
        self.images['bg'] = self.images[random.choice(['day', 'night'])]
        bird_color = random.choice(['red', 'yellow', 'blue'])
        self.images['birds'] = [self.images[bird_color + '-up'], self.images[bird_color + '-mid'],
                                self.images[bird_color + '-down']]
        pipe_color = random.choice(['green', 'red'])
        self.images['pipes'] = [self.images[pipe_color + '-pipe'],
                                pygame.transform.flip(self.images[pipe_color + '-pipe'], False, True)]

    # sp
    def reset_floor_x(self):
        self.floor_x = 0

    def reset_bird_y_hen(self):
        self.bird_y_hen = 0

    def reset_frame_idx(self):
        self.fi = 0

    def get_floor_x(self):
        return self.floor_x

    def get_bird_y_hen(self):
        return self.bird_y_hen

    def get_frame_idx(self):
        return self.fi

    def get_floor_bg_gap(self):
        # cal the difference of the bg and floor
        # floor need to move
        return self.images['floor'].get_width() - self.a_settings.screen_width

    def get_num_width(self):
        return self.images['0'].get_width()

    def get_num_show_width(self):
        return self.get_num_width() * self.a_settings.s_fr

    def get_num_show_y(self):
        return self.a_settings.screen_height * self.a_settings.s_y

    def get_pipe_y_random(self):
        # random a y coordination of pipe in game windows
        return random.randint(int(self.a_settings.screen_height * self.a_settings.pipe_y_gw_bh[0]),
                              int(self.a_settings.screen_height * self.a_settings.pipe_y_gw_bh[1]))

    def get_pipe_gap_random(self):
        return random.randint(self.a_settings.pipe_gap[0], self.a_settings.pipe_gap[1])

    # func
    def pre_game(self):
        self.random_while_start()
        # self.reset_floor_x()
        self.reset_bird_y_hen()

    def move_floor(self):
        self.floor_x -= self.a_settings.floor_v  # 336 x 112
        if self.floor_x < -self.floor_bg_gap:
            self.floor_x = 0

    def move_bird(self):
        self.bird_y_hen += self.a_settings.bird_y_v
        if self.bird_y_hen < self.a_settings.bird_y_range[0] or self.bird_y_hen > self.a_settings.bird_y_range[1]:
            self.a_settings.bird_y_v *= -1

    def change_frame_idx(self):
        self.fi += 1
        self.fi %= len(self.a_settings.bird_frames)
