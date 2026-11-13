import pygame as pg
import Physics
from pygame import sprite

from MazePrototype import Maze

#initialisation
pg.init()
screen = pg.display.set_mode((1080, 920))
clock = pg.time.Clock()
running = True
Gamepieces = sprite.Group(Maze(0,0))

RotationRate = 0.0

def Inputs():
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        return -1
    elif keys[pg.K_d]:
        return 1

#Main Loop
while running:
    v = Physics.Vector2(1,1)
    print(v.mag())
    print(v.hat().x)
    print(v.hat().y)
    inp = Inputs()

    #Closes the pygame instance when you close the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("purple")
    Gamepieces.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()