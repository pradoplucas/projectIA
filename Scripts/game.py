import pygame as pg
import random

###########VariablesToAI###########

#Velocity
speed = 1

#WidthOfCactus
widthCactus = 0

#HeightOfBeginCactus
heightCactusBegin = 0

#HeightOfEndCactus
heightCactusEnd = 0


###################################

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

#AddVelocity
speedAdd = 0

#Score
score = 0

#IsRunning!?
runPlay = True

#IsJumping
isJumping = False

#ValJump
val = 7.5

#Jump
jumpCount = val

#CountFPS
countFPS = -1

#CountFPSScore
countFPSScore = 0

#
cactusIndexA = False
cactusIndexB = False

cactusCountA = -50
cactusCountB = -50

#
cactusNumA = 0
cactusNumB = 0

#
posCactusY = 200

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
            pg.image.load('../Sprites/Cactus/21.png'),
            pg.image.load('../Sprites/Cactus/22.png'),
            pg.image.load('../Sprites/Cactus/23.png'),
            pg.image.load('../Sprites/Cactus/24.png'),
            pg.image.load('../Sprites/Cactus/25.png'),
            pg.image.load('../Sprites/Cactus/26.png'),
            pg.image.load('../Sprites/Cactus/27.png'),
            pg.image.load('../Sprites/Cactus/28.png'),
            pg.image.load('../Sprites/Cactus/29.png'),
            pg.image.load('../Sprites/Cactus/30.png'),
            pg.image.load('../Sprites/Cactus/31.png'),
            pg.image.load('../Sprites/Cactus/32.png'),
            pg.image.load('../Sprites/Cactus/33.png'),
            pg.image.load('../Sprites/Cactus/34.png')]

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

def cactusGenerate():
    global  countFPSScore, cactusIndexA, cactusIndexB, cactusNumA, cactusNumB, cactusCountA, cactusCountB, posCactusY

    if (posGroundXDin == -50):
        if random.randint(0, 9) >= 3:

            cactusCountA = 1049
            cactusIndexA = True

            cactusNumA = random.randint(0, 33)

    elif (posGroundXDin == -600):
        if random.randint(0, 9) >= 3:

            cactusCountB = 1049
            cactusIndexB = True

            cactusNumB = random.randint(0, 33)

    if cactusIndexA and (cactusCountA > -49):

        if cactus[cactusNumA].get_size()[1] < 60:
            posCactusY = 5

        else:
            posCactusY = 20

        win.blit(cactus[cactusNumA], (cactusCountA, posGroundY - posCactusY))
        cactusCountA -= (10 + speedAdd)

    else:
        cactusIndexA = False
        cactusCountA = -50

    if cactusIndexB and (cactusCountB > -49):

        if cactus[cactusNumB].get_size()[1] < 60:
            posCactusY = 5

        else:
            posCactusY = 20

        win.blit(cactus[cactusNumB], (cactusCountB, posGroundY - posCactusY))
        cactusCountB -= (10 + speedAdd)

    else:
        cactusIndexB = False
        cactusCountB = -50

    if cactusCountA > cactusCountB:
        widthCactus = cactus[cactusNumB].get_size()[0]

        if (cactusNumB >= 0) and (cactusNumB <= 17):
            heightCactusBegin = 45

            if (cactusNumB >= 0) and (cactusNumB <= 10):
                heightCactusEnd = 45

            else:
                heightCactusEnd = 62
        
        else:
            heightCactusBegin = 62

            if (cactusNumB >= 18) and (cactusNumB <= 28):
                heightCactusEnd = 45

            else:
                heightCactusEnd = 62

    else:
        widthCactus = cactus[cactusNumA].get_size()[0]

        if (cactusNumA >= 0) and (cactusNumA <= 17):
            heightCactusBegin = 45

            if (cactusNumA >= 0) and (cactusNumA <= 10):
                heightCactusEnd = 45

            else:
                heightCactusEnd = 62
        
        else:
            heightCactusBegin = 62

            if (cactusNumA >= 18) and (cactusNumA <= 28):
                heightCactusEnd = 45

            else:
                heightCactusEnd = 62

##Verificar se o cacto passou do Dino..
#Definir variáveis do Dino para a IA..

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


#def onCollider():


while runPlay:

    fps.tick(32)

    scoreDef()

    if speed < 8:
        speedDef()

    win.blit(pg.image.load('teste.png'), (0, 0))

    updateScreen()

    win.blit(pg.image.load('teste.png'), (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            runPlay = False

pg.quit()