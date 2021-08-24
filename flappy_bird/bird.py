import pygame.transform


class Bird:
    def __init__(self, ms, a_settings):
        self.a_settings = a_settings
        self.ms = ms

        self.rect = self.ms.images['red-mid'].get_rect()  # all bird materials same size
        self.rect.x = a_settings.screen_width * 0.2
        self.rect.y = a_settings.screen_height * 0.4

        self.y_v = self.a_settings.ori_y_v
        self.rtt = self.a_settings.ori_rtt

        self.reset_bird_y_hen()
        self.reset_frame_idx()

    def reset_bird_y_hen(self):
        self.bird_y_hen = 0

    def reset_frame_idx(self):
        self.fi = 0

    def reset_flap(self):  # when flap
        self.y_v = self.a_settings.ori_y_v
        self.rtt = self.a_settings.ori_rtt

    def get_bird_y_hen(self):
        return self.bird_y_hen

    def change_frame_idx(self):
        self.fi += 1
        self.fi %= len(self.a_settings.bird_frames)

    def get_frame_idx(self):
        return self.fi

    def move_bird(self):
        self.bird_y_hen += self.a_settings.bird_y_v
        if self.bird_y_hen < self.a_settings.bird_y_range[0] or self.bird_y_hen > self.a_settings.bird_y_range[1]:
            self.a_settings.bird_y_v *= -1

    def get_image(self):
        image = self.ms.images['birds'][self.a_settings.bird_frames[self.fi]]
        image = pygame.transform.rotate(image, self.rtt)
        return image

    def get_coordinates(self):
        return self.rect.x, self.rect.y + self.get_bird_y_hen()

    def update_y_v(self):
        self.y_v = min(self.y_v + self.a_settings.g, self.a_settings.y_v_max)

    def update_rtt(self):
        self.rtt = max(self.rtt + self.a_settings.rtt_o, self.a_settings.rtt_max)

    def update(self, flap=False):
        if flap:
            self.reset_flap()

        self.update_y_v()
        self.update_rtt()
        self.rect.y += self.y_v
        self.change_frame_idx()
        # self.move_bird()

    def when_die(self):  # update like func for end window only
        if self.rect.y < self.ms.floor_y:
            self.rect.y += self.a_settings.y_v_max
            self.rtt = max(self.rtt + self.a_settings.rtt_o_die, self.a_settings.rtt_max_die)
