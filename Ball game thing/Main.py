import pygame as pg
import Physics
from pygame import sprite
import math

from Maze import Maze
from Ball import Ball


center_x = 1080// 2
center_y =  920// 2

#initialisation
pg.init()
screen = pg.display.set_mode((1080, 920))
clock = pg.time.Clock()
running = True
Gamepieces = sprite.Group(Maze(center_x,center_y), Ball(center_x,center_y))


#Constants
RotationRate = 4.0

#global Vars
CurrRot = 0.0
ballspeedx = 0
ballspeedy = 5

def Inputs():
    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        return -1
    elif keys[pg.K_d]:
        return 1
    else:
        return 0

def Rotate(inp):
    global CurrRot
    CurrRot += RotationRate * inp

    if math.fabs(CurrRot) > 360:
        CurrRot = 0

#Main Loop
while running:
    inp = Inputs()
    maze = Gamepieces.sprites()[0]
    ball = Gamepieces.sprites()[1]

    if inp != 0:
        Rotate(inp)
        maze.rotate(CurrRot)

    Ball.moveball(ball, ballspeedy, ballspeedy)

    #Closes the pygame instance when you close the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("white")
    Gamepieces.draw(screen)
    pg.display.flip()
    clock.tick(60)
pg.quit()