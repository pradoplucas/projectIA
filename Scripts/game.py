import pygame as pg

#Size of Screen..
height = 400
width = 1000

#DinoPosition
posDinoX = 100
posDinoY = 180

#IsRunning!?
runPlay = True

#CountFPS
countFPS = -1

#FPS
fps = pg.time.Clock()

#ImagesDinoRunning
running =   [pg.image.load('../Sprites/Dino/dino_11.png'), 
            pg.image.load('../Sprites/Dino/dino_22.png')]

#Ground
ground = pg.image.load('../Sprites/Scenario/ground.png')

#Background
bg = pg.image.load('../Sprites/Scenario/bg.png')

###########################################

#PygameInit
pg.init()

#SetSizeScreen
win = pg.display.set_mode((width, height))

#SetTitle
pg.display.set_caption("Runner T-Rex")


def updateScreen():

    global countFPS

    win.blit(bg, (-50, -50))  

    countFPS += 1

    if countFPS >= 8:
        countFPS = 0
    
    win.blit(ground, (0, 200))

    win.blit(running[countFPS//4], (posDinoX, posDinoY))
    
    pg.display.update()

while runPlay:
    fps.tick(32)

    updateScreen()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            runPlay = False

pg.quit()