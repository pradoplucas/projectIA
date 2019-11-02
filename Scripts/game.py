import pygame as pg
import random

#Size of Screen..
height = 400
width = 1000

#DinoPosition
posDinoX = 100
posDinoY = 180

#PosYGroundDontChange
posGroundY = 200

#GroundXPositionRespawn
posGroundXRp = 1050

#GroundXPositionDinamic
posGroundXDin = -50

#Velocity
speed = 1

#AddVelocity
speedAdd = 0

#Score
score = 0

#IsRunning!?
runPlay = True

#IsJumping
isJumping = False

val = 8

#
jumpCount = val

#CountFPS
countFPS = -1

#CountFPSScore
countFPSScore = 0

#
cactusIndex = True
cactusIndexA = False
cactusIndexB = False

#
cactusNumA = 0
cactusNumB = 0

#FPS
fps = pg.time.Clock()

#ImagesDinoRunning
running =   [pg.image.load('../Sprites/Dino/dino_11.png'), 
            pg.image.load('../Sprites/Dino/dino_22.png')]

#ImagesDinoJump
jumping =   pg.image.load('../Sprites/Dino/dino_jump.png')

#Ground
ground = pg.image.load('../Sprites/Scenario/ground.png')

cactus =    [pg.image.load('../Sprites/Cactus/1.png'),
            pg.image.load('../Sprites/Cactus/2.png'),
            pg.image.load('../Sprites/Cactus/3.png'),
            pg.image.load('../Sprites/Cactus/4.png'),
            pg.image.load('../Sprites/Cactus/5.png'),
            pg.image.load('../Sprites/Cactus/6.png'),
            pg.image.load('../Sprites/Cactus/7.png'),
            pg.image.load('../Sprites/Cactus/8.png'),
            pg.image.load('../Sprites/Cactus/9.png'),
            pg.image.load('../Sprites/Cactus/10.png'),
            pg.image.load('../Sprites/Cactus/11.png'),
            pg.image.load('../Sprites/Cactus/12.png'),
            pg.image.load('../Sprites/Cactus/13.png'),
            pg.image.load('../Sprites/Cactus/14.png'),
            pg.image.load('../Sprites/Cactus/15.png'),
            pg.image.load('../Sprites/Cactus/16.png'),
            pg.image.load('../Sprites/Cactus/17.png'),
            pg.image.load('../Sprites/Cactus/18.png'),
            pg.image.load('../Sprites/Cactus/19.png'),
            pg.image.load('../Sprites/Cactus/20.png'),
            pg.image.load('../Sprites/Cactus/21.png'),]

#Background
bg = pg.image.load('../Sprites/Scenario/bg.png')

###########################################

#PygameInit
pg.init()

#SetSizeScreen
win = pg.display.set_mode((width, height))

#SetTitle
pg.display.set_caption("Runner T-Rex")

#InitGround
win.blit(ground, (posGroundXDin, posGroundY))
win.blit(ground, (posGroundXDin + 1100, posGroundY))

def actionDef():
    global countFPS, isJumping, jumpCount, posDinoY, val, jumping

    keys = pg.key.get_pressed()

    countFPS += 1

    if countFPS >= 8:
        countFPS = 0

    if not(isJumping):
        win.blit(running[countFPS//4], (posDinoX, posDinoY))

        #if keys[pg.K_DOWN]:

        if keys[pg.K_UP]:
            isJumping = True

    else:
        if jumpCount >= -val:
            neg = 1
            if jumpCount < 0:
                neg = -1
            posDinoY -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            win.blit(jumping, (posDinoX, posDinoY))

        else:
            isJumping = False
            jumpCount = val
            
def scoreDef():
    global countFPSScore, score

    countFPSScore += 1

    if countFPSScore % 4 == 0:
        score += 1

def speedDef():
    global score, speed

    if score == 100:
        speed = 2  

    elif score == 300:
        speed = 3

    elif score == 600:
        speed = 4

    elif score == 1000:
        speed = 5

    elif score == 1500:
        speed = 6

    elif score == 2100:
        speed = 7

    elif score == 2800:
        speed = 8

###############################################################################

aux = True

def cactusGenerate():
    global  countFPSScore, cactusIndexA, cactusIndexB, cactusIndex, cactusNumA, cactusNumB, aux

    if countFPSScore % 50 == 0:
        if random.randint(0, 9) > 4:
            if cactusIndex:
                cactusIndexA = True
                aux = True
                cactusNumA = random.randint(0, 20)
            else:
                cactusIndexB = True
                aux = False
                cactusNumB = random.randint(0, 20)
  
'''
        if aux:
            cactusIndexB = False

        elif not aux:
            cactusIndexA = False
''' 

    if cactusIndexA:
        win.blit(cactus[cactusNumA], (posGroundXDin + 1100, posGroundY - 20))
        print('A')

    elif cactusIndexB:
        win.blit(cactus[cactusNumB], (posGroundXDin + 1100, posGroundY - 20))
        print('B')

###################################################################################################

def groundChange(): 
    global posGroundXDin, speedAdd, speed

    if speedAdd < 20:
        speedAdd = speed * 2.5

    posGroundXDin -= (10 + speedAdd)

    if posGroundXDin <= -1150:
        posGroundXDin = -50

    win.blit(ground, (posGroundXDin, posGroundY))
    win.blit(ground, (posGroundXDin + 1100, posGroundY))

    cactusGenerate()


def updateScreen():

    win.blit(bg, (-50, -50))  

    groundChange()

    actionDef()
    
    pg.display.update()

while runPlay:

    fps.tick(32)

    scoreDef()

    if speed < 8:
        speedDef()

    updateScreen()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            runPlay = False

pg.quit()