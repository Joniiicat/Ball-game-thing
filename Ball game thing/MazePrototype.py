import pygame as pg


class Maze(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)


        self.image = pg.image.load("Sprite-0002.png")
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()