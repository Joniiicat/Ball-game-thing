import pygame as pg
import Physics

#initialisation
pg.init()
screen = pg.display.set_mode((1920, 1080))
clock = pg.time.Clock()
running = True

#Main Loop
while running:
    v = Physics.Vector2(1,1)
    print(v.mag())
    print(v.hat().x)
    print(v.hat().y)

    #Closes the pygame instance when you close the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("purple")
    pg.display.flip()
    clock.tick(60)
pg.quit()