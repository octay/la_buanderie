import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, ms, a_settings, x, y, upwards=True):
        pygame.sprite.Sprite.__init__(self)
        self.a_settings = a_settings
        self.ms = ms

        self.rect = self.ms.images['green-pipe'].get_rect()  # all bird materials same size
        self.rect.x = x

        if upwards:
            self.image = self.ms.images['pipes'][0]  # image variation for sprite.draw()
            self.rect.top = y
        else:
            self.image = self.ms.images['pipes'][1]
            self.rect.bottom = y

    def update(self):
        self.rect.x += self.a_settings.pipe_v

    def get_image(self):
        return self.image

    def get_coordinates(self):
        return self.rect

    def get_rect_x(self):
        return self.rect.x

    def get_rect_right(self):
        return self.rect.right
