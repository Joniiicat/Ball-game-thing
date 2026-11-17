import pygame as pg


class Ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        #TODO: Find/Make better image
        self.image = pg.image.load("Assets/ball.png")
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))