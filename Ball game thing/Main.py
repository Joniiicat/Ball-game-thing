import pygame as pg
from pygame import sprite

from MazePrototype import Maze

#initialisation
pg.init()
screen = pg.display.set_mode((1080, 920))
clock = pg.time.Clock()
running = True
Gamepieces = sprite.Group(Maze(0,0))

#Main Loop
while running:

    #Closes the pygame instance when you close the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("purple")
    Gamepieces.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()