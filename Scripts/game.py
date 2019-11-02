import pygame as pg

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

#FPS
fps = pg.time.Clock()

#ImagesDinoRunning
running =   [pg.image.load('../Sprites/Dino/dino_11.png'), 
            pg.image.load('../Sprites/Dino/dino_22.png')]

#ImagesDinoJump
jumping =   pg.image.load('../Sprites/Dino/dino_jump.png')

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

def groundChange(): 
    global posGroundXDin, speedAdd, speed

    if speedAdd < 20:
        speedAdd = speed * 2.5

    posGroundXDin -= (10 + speedAdd)

    if posGroundXDin <= -1150:
        posGroundXDin = -50

    win.blit(ground, (posGroundXDin, posGroundY))
    win.blit(ground, (posGroundXDin + 1100, posGroundY))


def updateScreen():

    win.blit(bg, (-50, -50))  

    groundChange()

    actionDef()
    
    pg.display.update()

while runPlay:
#    global speed

    fps.tick(32)

    scoreDef()

    if speed < 8:
        speedDef()

    updateScreen()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            runPlay = False

pg.quit()