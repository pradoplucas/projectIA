import pygame
import random

#####################__VARIABLES_TO_AI__######################

#Speed
speed = 1

#
heightDino = 0

#
widthObstacle = 0

#
heightObstacle = 0

#
distanceObstacle = 0

##############################################################


#####################__GLOBAL_VARIABLES__#####################

#
widthCactus = 0

#
heightCactusBegin = 0

#
heightCactusEnd = 0

#
restart = False

#CenterOfTheDinoPosition
posDinoX = 129 #DontReallyNeedBecauseItsFixed
posDinoY = 0

heightDino = posDinoY

#DimensionsOfScreen
width = 900
height = 400

#FPS
FPS = 30

#CountOfFrames
countFrames = 0

#CountGroundScreen
countGround = 1000

#Score
score = 0

#ChangeTheDinoSprite
updateDinoSprite = 0

#VerifyIfDinoIsJumpinp
dinoIsJumping = False

#DinoIsLower
dinoIsLower = False

#HightOfJump
dinoCountJump = 0

#PlaceToSetDinoImage
dinoX = 100
dinoY = 180

#VerifyIfCactusExists
cactusAExist = False
cactusBExist = False

#NumberOfCactusImage
cactusNumA = -1
cactusNumB = -1

#TimeOfCactusInScreen
cactusCountA = -1
cactusCountB = -1

#PlaceCactusCollider
auxCactusCollider = -1

#LastGroundUpdate
auxCountGround = -1

#PositionToDinoCollide
posDinoColX = 0
posDinoColY = 0

#VerifyIfBirdExist
birdExist = False

#TimeOfBirdScreen
birdCount = -1

#PlaceToSetBirdInScreen
birdPlace = -1

#Bird2000Px
auxCountBird = 0

#PositionYToBird
posBirdY = 0

#ChangeTheBirdSprite
updateBirdSprite = 0

#
dinoIsSuperJumping = False

#
auxMountainAppear = 0

#
mountainExist = False

#
mountainCount = 1100

#
allowSuperJump = True

#
auxSuperJump = 0

#
textScore = 0

#
textSuperJump = 0

##############################################################

##########################__IMAGES__##########################
#Background247
background =        pygame.image.load('../Sprites/Scenario/bg.png')

#Ground
ground =            pygame.image.load('../Sprites/Scenario/ground.png')

#Mountain
mountain =            pygame.image.load('../Sprites/Scenario/mountain1.png')

#DinoRunning
dinoRunningImage =  [pygame.image.load('../Sprites/Dino/dino_11.png'), 
                    pygame.image.load('../Sprites/Dino/dino_22.png')]

#DinoLower
dinoLowerImage =  [pygame.image.load('../Sprites/Dino/down_1.png'), 
                    pygame.image.load('../Sprites/Dino/down_2.png')]

#DinoJumping
dinoJumpingImage =  pygame.image.load('../Sprites/Dino/dino_jump.png')

#BirdImage
birdImage =     [pygame.image.load('../Sprites/Bird/bird_1.png'), 
                pygame.image.load('../Sprites/Bird/bird_2.png')]

#34DifferentCactus
cactusImage =       [pygame.image.load('../Sprites/Cactus/1.png'),
                    pygame.image.load('../Sprites/Cactus/2.png'),
                    pygame.image.load('../Sprites/Cactus/3.png'),
                    pygame.image.load('../Sprites/Cactus/4.png'),
                    pygame.image.load('../Sprites/Cactus/5.png'),
                    pygame.image.load('../Sprites/Cactus/6.png'),
                    pygame.image.load('../Sprites/Cactus/7.png'),
                    pygame.image.load('../Sprites/Cactus/8.png'),
                    pygame.image.load('../Sprites/Cactus/9.png'),
                    pygame.image.load('../Sprites/Cactus/10.png'),
                    pygame.image.load('../Sprites/Cactus/11.png'),
                    pygame.image.load('../Sprites/Cactus/12.png'),
                    pygame.image.load('../Sprites/Cactus/13.png'),
                    pygame.image.load('../Sprites/Cactus/14.png'),
                    pygame.image.load('../Sprites/Cactus/15.png'),
                    pygame.image.load('../Sprites/Cactus/16.png'),
                    pygame.image.load('../Sprites/Cactus/17.png'),
                    pygame.image.load('../Sprites/Cactus/18.png'),
                    pygame.image.load('../Sprites/Cactus/19.png'),
                    pygame.image.load('../Sprites/Cactus/20.png'),
                    pygame.image.load('../Sprites/Cactus/21.png'),
                    pygame.image.load('../Sprites/Cactus/22.png'),
                    pygame.image.load('../Sprites/Cactus/23.png'),
                    pygame.image.load('../Sprites/Cactus/24.png'),
                    pygame.image.load('../Sprites/Cactus/25.png'),
                    pygame.image.load('../Sprites/Cactus/26.png'),
                    pygame.image.load('../Sprites/Cactus/27.png'),
                    pygame.image.load('../Sprites/Cactus/28.png'),
                    pygame.image.load('../Sprites/Cactus/29.png'),
                    pygame.image.load('../Sprites/Cactus/30.png'),
                    pygame.image.load('../Sprites/Cactus/31.png'),
                    pygame.image.load('../Sprites/Cactus/32.png'),
                    pygame.image.load('../Sprites/Cactus/33.png'),
                    pygame.image.load('../Sprites/Cactus/34.png')]

##############################################################

#######################__PYGAME_INIT__########################
#Init // Screen // Caption
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner T-Rex")

fontBig = pygame.font.Font('freesansbold.ttf', 16)
fontMedium = pygame.font.Font('freesansbold.ttf', 12)
fontSmall = pygame.font.Font('freesansbold.ttf', 8) 
##############################################################

def main():
    global countFrames

    #DefineIfTheGameIsRunningOrNot
    isPlaying = True

    #FPS
    framesPerSecond = pygame.time.Clock()

    #InfinitLoop
    while isPlaying:

        #DefineTheFPSOfGmae
        framesPerSecond.tick(FPS)
    
        #CloseTheGame
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:   
                isPlaying = False

        #NumberOfFrames
        countFrames += 1

        #ThingsToDo
        onUpdate()

        #Update
        pygame.display.update()

def onUpdate():
    #SetBackgroundInEachFrame
    window.blit(background, (-50, -50))

    #DefineTheScore
    setScore()

    #DefineTheSpeed
    setSpeed()

    #UpdateGround
    updateGround()

    #ChangesInDinoPosition
    updateDino()

    #FunctionsRelatedWithCactus
    cactusDef()

    #
    birdDef()

    #
    setObstacleSize()

    #
    onColliderCactus()

    #
    onColliderMountain()

    #
    onColliderBird()

    if restart:
        onRestart()

def onRestart():
    global restart, speed, countFrames, countGround, score, dinoIsJumping, dinoIsLower, cactusAExist, cactusBExist, cactusCountA, cactusCountB
    global birdExist, birdCount, birdPlace, auxCountBird, auxCactusCollider, auxMountainAppear, mountainExist, mountainCount, allowSuperJump, auxSuperJump

    pygame.time.delay(500)

    restart = False
    
    speed = 1

    countFrames = 0

    countGround = 1000

    score = 0

    dinoIsJumping = False

    dinoIsSuperJumping = False

    dinoIsLower = False

    cactusAExist = False
    cactusBExist = False

    cactusCountA = 1000
    cactusCountB = 1000

    auxCactusCollider = -1

    birdExist = False

    birdCount = 1250

    birdPlace = -1

    auxCountBird = 0

    #
    auxMountainAppear = 0

    #
    mountainExist = False

    #
    mountainCount = 1100

    #
    allowSuperJump = True

    #
    auxSuperJump = 0

def setScore():
    global countFrames, score, textScore, font

    score = countFrames // 4

    textScore = fontBig.render(str(score), True, (83, 83, 83), (247, 247, 247)) 

    window.blit(fontMedium.render('Score', True, (83, 83, 83), (247, 247, 247)) , (width - 50, 10))
    window.blit(textScore, (width - 50, 25))

def setSpeed():
    global speed, score

    if score == 100:
        speed = 2

    elif score == 400:
        speed = 4

    elif score == 1200:
        speed = 8

def updateGround():
    global countGround, speed, auxCountGround

    if speed == 1:
        countGround -= (10)
        auxCountGround = 10
        
    elif speed == 2:
        if countGround != 10:
            countGround -= (12.5)
            auxCountGround = 12.5
        else:
            countGround -= (10)
            auxCountGround = 10

    elif speed == 4:
        if countGround != 12.5:
            countGround -= (20)
            auxCountGround = 20
        else:
            countGround -= (12.5)
            auxCountGround = 12.5

    elif speed == 8:
        if countGround != 20:
            countGround -= (25)
            auxCountGround = 25
        else:
            countGround -= (20)
            auxCountGround = 20

    window.blit(ground, (countGround - 1050, 200))
    window.blit(ground, (countGround - 50, 200))

    if countGround == 0:
        countGround = 1000

    #velocidades possíveis [10, 12.5, 20, 25] = 4

def updateDino():
    global updateDinoSprite, dinoIsJumping, dinoIsLower, posDinoY, dinoCountJump, dinoX, dinoY, posDinoColX, posDinoColY, dinoIsSuperJumping, allowSuperJump, auxSuperJump, textSuperJump
    
    keys = pygame.key.get_pressed()

    if updateDinoSprite == 8:
        updateDinoSprite = 0

    if not dinoIsJumping and not dinoIsSuperJumping:
        dinoY = 180
        
        if not dinoIsLower:
            posDinoY = 185
            dinoX = 100

            posDinoColX = dinoX + 40
            posDinoColY = dinoY + 35

            window.blit(dinoRunningImage[updateDinoSprite//4], (dinoX, dinoY))

        else:
            posDinoY = + 20
            dinoX = 90

            posDinoColX = dinoX + 70
            posDinoColY = dinoY + 30

            window.blit(dinoLowerImage[updateDinoSprite//4], (dinoX, dinoY))            

        if keys[pygame.K_UP]:
            dinoIsJumping = True
            dinoCountJump = 7.5

        elif keys[pygame.K_DOWN]:
            dinoIsLower = True

        elif keys[pygame.K_SPACE] and allowSuperJump:
            dinoIsSuperJumping = True
            dinoCountJump = 9
            allowSuperJump = False
            auxSuperJump = 0

        else:
            dinoIsLower = False

    elif dinoIsJumping: #DinoIsJumping
        if dinoCountJump >= -7.5:
            upDown = 1
            
            if dinoCountJump < 0:
                upDown = -1
            
            dinoY -= (dinoCountJump ** 2) * 0.5 * upDown

            dinoCountJump -= 1

        else:
            dinoIsJumping = False
            dinoCountJump = 7.5

        posDinoY = dinoY + 5

        posDinoColX = dinoX + 40
        posDinoColY = dinoY + 35

        window.blit(dinoJumpingImage, (dinoX, dinoY))

    elif dinoIsSuperJumping: #DinoIsSUperJumping
        if dinoCountJump >= -9:
            upDown = 1
            
            if dinoCountJump < 0:
                upDown = -1
            
            dinoY -= (dinoCountJump ** 2) * 0.5 * upDown

            dinoCountJump -= 1

        else:
            dinoIsSuperJumping = False
            dinoCountJump = 9

        posDinoY = dinoY + 5

        posDinoColX = dinoX + 40
        posDinoColY = dinoY + 35

        window.blit(dinoJumpingImage, (dinoX, dinoY))  

    #TestReferenceToAI
    #window.blit(pygame.image.load('../Sprites/redes.png'), (posDinoColX, posDinoColY))

    updateDinoSprite += 1

    if countGround % 500 == 0:

        if auxSuperJump != 7:
            auxSuperJump += 1

        if auxSuperJump == 7:
            allowSuperJump = True

    text = '['
    auxText = ''

    for i in range(auxSuperJump):
        text += '#'

    for i in range(7 - auxSuperJump):
        auxText += '_'

    text = text + auxText + ']'

    #if(auxSuperJump == 7):
    #    text = '[#ready#]'


    textSuperJump = fontBig.render(str(text), True, (83, 83, 83), (247, 247, 247)) 

    window.blit(fontMedium.render('SuperJump', True, (83, 83, 83), (247, 247, 247)) , (13, 10))

    window.blit(textSuperJump, (10, 25)) 

def cactusDef():
    #DefineWichCactusWillAppear
    setCactus()

    #UpdateCactus
    updateCactus()

def setCactus():

    global cactusAExist, cactusBExist, cactusNumA, cactusNumB, cactusCountA, cactusCountB, auxMountainAppear, mountainCount, mountainExist

    if countGround == 1000:
        if random.randint(0, 9) >= 3:
            cactusAExist = True
            cactusCountA = 1000
            cactusNumA = random.randint(0, 33)

    elif countGround == 500:
        auxMountainAppear += 1
        if auxMountainAppear == 4:
            auxMountainAppear = 0
            mountainExist = True
            mountainCount = 1100

        else:
            if random.randint(0, 9) >= 3:
                cactusBExist = True
                cactusCountB = 1000
                cactusNumB = random.randint(0, 33)

def updateCactus():
    global cactusAExist, cactusBExist, cactusNumA, cactusNumB, cactusCountA, cactusCountB, mountainExist, mountainCount

    #ToA
    if cactusAExist:
        cactusCountA -= auxCountGround

        #if (cactusCountA != 10 and cactusCountA != 12.5 and 
        #    cactusCountA != 20 and cactusCountA != 25):
        if cactusCountA > 25:           
            if cactusImage[cactusNumA].get_size()[1] < 60:
                posCactusY = 5

            else:
                posCactusY = 20

            window.blit(cactusImage[cactusNumA], (cactusCountA - 50, 200 - posCactusY))

        else:
            cactusAExist= False
            cactusCountA = 1000

    else:
        cactusCountA = 1000

    #ToB
    if cactusBExist:
        cactusCountB -= auxCountGround
        
        #if (cactusCountB != 10 and cactusCountB != 12.5 and 
        #    cactusCountB != 20 and cactusCountB != 25):

        if cactusCountB > 25:
            if cactusImage[cactusNumB].get_size()[1] < 60:
                posCactusY = 5

            else:
                posCactusY = 20

            window.blit(cactusImage[cactusNumB], (cactusCountB - 50, 200 - posCactusY))

        else:
            cactusBExist = False
            cactusCountB = 1000

    else:
        cactusCountB = 1000


    if mountainExist:
        mountainCount -= auxCountGround

        #if (mountainCount != 10 and mountainCount != 12.5 and 
        #    mountainCount != 20 and mountainCount != 25):

        if mountainCount > 25:
            window.blit(mountain, (mountainCount - 190, 110))

        else:
            mountainExist = False
            mountainCount = 1100

    else:
        mountainCount = 1100 

def birdDef():
    #
    setBird()

    #
    updateBird()

def setBird():
    global birdExist, birdCount, birdPlace, auxCountBird
    if score > 500:
        if countGround % 1000 == 0:
            auxCountBird += 1

            if random.randint(0, 9) >= 0 and auxCountBird == 2:
                auxCountBird = 0
                birdExist = True
                birdCount = 1250
                birdPlace = random.randint(0, 2)

def updateBird():
    global birdCount, posBirdY, updateBirdSprite, birdExist

    if birdExist:
        birdCount -= auxCountGround

        #if (birdCount != 10 and birdCount != 12.5 and 
        #    birdCount != 20 and birdCount != 25):
        if birdCount > 25:
            if updateBirdSprite == 8:
                updateBirdSprite = 0

            if birdPlace == 0:
                posBirdY = 120

            elif birdPlace == 1:
                posBirdY = 160

            else:
                posBirdY = 190

            window.blit(birdImage[updateBirdSprite//4], (birdCount - 50, posBirdY))

            updateBirdSprite += 1

        else:
            birdExist= False
            birdCount = 1250


    else:
        birdCount = 1250

def setObstacleSize():
    global widthCactus, heightCactusBegin, heightCactusEnd, auxCactusCollider
    global widthObstacle, heightObstacle, distanceObstacle

    widthCactusA = cactusImage[cactusNumA].get_size()[0]
    widthCactusB = cactusImage[cactusNumB].get_size()[0]

    if (cactusCountA < cactusCountB) and (cactusCountA < birdCount) and (cactusCountA < mountainCount) and (posDinoColX < cactusCountA + widthCactusA):
        widthCactus = cactusImage[cactusNumA].get_size()[0]

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

        widthObstacle = widthCactus
        heightObstacle = 242 - ((heightCactusBegin + heightCactusEnd) / 2)
        distanceObstacle = cactusCountA - posDinoX

        auxCactusCollider = cactusCountA - 50

    elif (cactusCountA > cactusCountB) and (birdCount > cactusCountB) and (mountainCount > cactusCountB) and (posDinoColX < cactusCountB + widthCactusB):
        widthCactus = cactusImage[cactusNumB].get_size()[0]        

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

        widthObstacle = widthCactus
        heightObstacle = 242 - ((heightCactusBegin + heightCactusEnd) / 2)
        distanceObstacle = cactusCountB - posDinoX

        auxCactusCollider = cactusCountB - 50

    else:
        auxCactusCollider = 950

    if (mountainCount < cactusCountA) and (mountainCount < cactusCountB) and (mountainCount < birdCount) and (posDinoColX < mountainCount + 140):
        widthObstacle = 140
        heightObstacle = 110
        distanceObstacle = mountainCount - posDinoX

    if (birdCount < cactusCountA) and (birdCount < cactusCountB) and (birdCount < mountainCount) and (posDinoColX < birdCount + 60):
        widthObstacle = 60
        heightObstacle = posBirdY
        distanceObstacle = birdCount - posDinoX

def onColliderCactus():
    global restart

    if (posDinoColX > auxCactusCollider) and (posDinoColY > (245 - heightCactusBegin)) and (posDinoColX < (auxCactusCollider + (widthCactus / 2))):
        restart = True

    elif (posDinoColX > (auxCactusCollider + (widthCactus / 2))) and (posDinoColY > (245 - heightCactusEnd)) and ((posDinoColX - 25) < (auxCactusCollider + widthCactus)):
        restart = True

def onColliderBird():
    global restart

    if dinoIsLower:
        if (posDinoColX > (birdCount - 50)) and (posDinoColX < ((birdCount + 60) - 50)) and (posDinoColY > (posBirdY + 10)) and (posDinoColY < (posBirdY + 42)):
            restart = True

    elif dinoIsJumping:
        if (posDinoColX > (birdCount - 50)) and (posDinoColX < ((birdCount + 60) - 50)) and ((posDinoColY - 20) > (posBirdY + 10)) and ((posDinoColY - 20) < (posBirdY + 42)):
            restart = True   

    else:
        if (posDinoColX > (birdCount - 50)) and (posDinoColX < ((birdCount + 60) - 50)) and (posDinoColY > (posBirdY + 10)) and ((posDinoColY - 20) < (posBirdY + 42)):
            restart = True   

def onColliderMountain():
    global restart

    if mountainExist:
        if (posDinoColX > (mountainCount - 190)) and (posDinoColY > 192) and (posDinoColX < ((mountainCount - 175) + 50)):
            restart = True 

        elif (posDinoColX > ((mountainCount - 190) + 50)) and (posDinoColY > 110) and (posDinoColX < ((mountainCount - 190) + 90)):
            restart = True 

        elif (posDinoColX > ((mountainCount - 190) + 90)) and (posDinoColY > 192) and (posDinoColX < ((mountainCount - 190) + 140)):
            restart = True 

main()

pygame.quit()