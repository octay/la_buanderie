class Settings:
    def __init__(self):
        # basic
        self.screen_width, self.screen_height = 288, 512
        self.fps = 30

        # settings of floor
        self.floor_v = 4  # it is fine cuz i use -= to update

        # settings of bird
        self.bird_y_v = 1
        self.bird_y_range = (-8, 8)  # this two variation is for menu window
        self.f_re = 5  # repeat each pic 5 frames
        self.bird_frames = [0] * self.f_re + [1] * self.f_re + [2] * self.f_re + [1] * self.f_re
        # settings of bird in game window
        self.ori_y_v = -10
        self.y_v_max = 10  # max v
        self.g = 1
        self.ori_rtt = 45
        self.rtt_max = -20
        self.rtt_o = -3
        self.rtt_o_die = -15
        self.rtt_max_die = -90

        # settings of pipe
        self.pipe_v = -4
        self.pipe_d = 150
        self.pipe_n = 4
        self.pipe_y_gw_bh = (0.3, 0.7)  # y coordination range of pipe in game windows based on screen_height
        self.pipe_gap = (120, 140)  # pipe up and down gap range

        # settings of score number gap
        self.s_y = 0.1
        self.s_fr = 1.1
        self.each_score = 1

        # settings of end window
        self.end_remain = 0.6  # min time end window show
