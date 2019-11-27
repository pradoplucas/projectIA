import pygame
import random
import numpy as np
import dinoClasse as dn
import dinoRedeNeural as rn
import dinoAlgGenetico as ag

#####################__VARIABLES_TO_AI__######################
# Inicializando a rede neural do jogo
# 5 camadas de entrada, 5 camadas ocultas e 1 saída
dino = []
entradas = np.zeros(5)
entradasCerebro = np.zeros(5)
stringGeracaoEpoca = ''

isGenetic = False

#Speed
speed = 1

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
restartAll = False

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
auxMountainAppear = 0

#
mountainExist = False

#
mountainCount = 1100

#
textScore = 0

#
textSuperJump = 0

#DefineIfTheGameIsRunningOrNot
isPlaying = True

##############################################################

##########################__IMAGES__##########################
#Background247
background = pygame.image.load('../Sprites/Scenario/bg.png')

#Ground
ground =            pygame.image.load('../Sprites/Scenario/ground.png')

#Mountain
mountain =            pygame.image.load('../Sprites/Scenario/mountain1.png')

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

logoMenu = pygame.image.load('../Sprites/Scenario/logo.png')

##############################################################

#######################__PYGAME_INIT__########################
#Init // Screen // Caption
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner T-Rex")

fontGiant = pygame.font.Font('freesansbold.ttf', 24)
fontBig = pygame.font.Font('freesansbold.ttf', 16)
fontMedium = pygame.font.Font('freesansbold.ttf', 12)
fontSmall = pygame.font.Font('freesansbold.ttf', 8) 
##############################################################

def main():
    global countFrames, isPlaying

    #FPS
    framesPerSecond = pygame.time.Clock()

    if menu(framesPerSecond):
        print(stringGeracaoEpoca + ' 1')

        #Iniciar dinossauros
        for i in range(ag.TamanhoPopulacao):
            dino.append(dn.DinoClasse())

        #InfinitLoop
        while isPlaying:
            #DefineTheFPSOfGmae
            framesPerSecond.tick(FPS)
        
            #NumberOfFrames
            countFrames += 1

            #ThingsToDo
            onUpdate()

            #CloseTheGame
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:   
                    isPlaying = False

            #Update
            pygame.display.update()

def onUpdate():
    global restartAll, dino

    #SetBackgroundInEachFrame
    window.blit(background, (-50, -50))

    textNumGeracaoEpoca= fontBig.render(str(f'{stringGeracaoEpoca} {ag.NumGeracaoEpoca + 1}'), True, (83, 83, 83), (247, 247, 247)) 
    window.blit(textNumGeracaoEpoca, (13, 10))

    #DefineTheScore
    setScore()

    #DefineTheSpeed
    setSpeed()

    #UpdateGround
    updateGround()

    #ChangesInDinoPosition
    for i in range(ag.TamanhoPopulacao):
        updateDino(i)

    #FunctionsRelatedWithCactus
    cactusDef()

    #
    birdDef()

    #
    setObstacleSize()

    #Ações de colisão
    for i in range(ag.TamanhoPopulacao):
        onColliderCactus(i)
        onColliderBird(i)
        #onColliderMountain(i)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        for i in range(ag.TamanhoPopulacao):
            dino[i].dead = True

    #Verificação se todos os dinos morreram
    cont = 0
    for i in range(ag.TamanhoPopulacao):
        if dino[i].dead:
            cont += 1 
        if cont == ag.TamanhoPopulacao:
            restartAll = True

    if restartAll:
        if isGenetic:
            ag.GeneticChanges(dino)

        ag.NumGeracaoEpoca += 1
        onRestartAll()

def menu(framesPerSecond):
    global isGenetic, stringGeracaoEpoca, isPlaying
    auxMenu = True

    while auxMenu:
        framesPerSecond.tick(30)

        #SetBackgroundInEachFrame
        window.blit(logoMenu, (0, 0))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP1] or keys[pygame.K_1]:
            auxMenu = False
            isGenetic = False
            ag.TamanhoPopulacao = 1
            stringGeracaoEpoca = 'Época'


        elif keys[pygame.K_KP2] or keys[pygame.K_2]:
            auxMenu = False
            isGenetic = True
            ag.TamanhoPopulacao = 150
            stringGeracaoEpoca = 'Geração'

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:   
                return False

        pygame.display.update()
    
    return True

def onRestartAll():
    global restartAll, speed, countFrames, countGround, score, dino, cactusAExist, cactusBExist, cactusCountA, cactusCountB
    global birdExist, birdCount, birdPlace, auxCountBird, auxCactusCollider, auxMountainAppear, mountainExist, mountainCount
    global dino

    #Apenas para ter noção do que tá acontecendo
    print(f'Geração {ag.NumGeracaoEpoca + 1}')
    
    pygame.time.delay(500)

    restartAll = False
    
    speed = 1

    countFrames = 0

    countGround = 1000

    score = 0

    for i in range(ag.TamanhoPopulacao):
        dino[i].score = 0
        dino[i].IsJumping = False
        dino[i].IsSuperJumping = False
        dino[i].IsLower = False
        dino[i].dead = False
        dino[i].height = 0
        dino[i].auxSuperJump = 0
        dino[i].allowSuperJump = True

    cactusAExist = False
    cactusBExist = False

    cactusCountA = 1000
    cactusCountB = 1000

    auxCactusCollider = -1

    birdExist = False

    birdCount = 1100

    birdPlace = -1

    auxCountBird = 0

    #
    auxMountainAppear = 0

    #
    mountainExist = False

    #
    mountainCount = 1100

    #
    widthObstacle = 0

    #
    heightObstacle = 0

    #
    distanceObstacle = 0

def setScore():
    global countFrames, score, textScore

    score = countFrames // 4
    
    #Setando score para cada dino
    for i in range(ag.TamanhoPopulacao):
        if not dino[i].dead:
            dino[i].score = score
    
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

def updateDino(i):
    global dino, entradasAntesAcao

    if not dino[i].dead:
        # Alimentando entrada da rede Neural
        entradas[0] = speed
        entradas[1] = dino[i].height
        entradas[2] = widthObstacle
        entradas[3] = heightObstacle
        entradas[4] = distanceObstacle

        #Calculando Previsão
        saidas, ocultas = dino[i].cerebro.predict(entradas)
        pular = saidas[0] > 0.7
        abaixar = saidas[0] < 0.4
        #superJumping = saidas[2] == 0.0
        #print(saidas)
        '''
        if not pular:
            abaixar = saidas[1] > 0.9
        elif not abaixar:
            superJumping = saidas[2] > 0.9
        '''
        #keys = pygame.key.get_pressed()

        if dino[i].updateSprite == 8:
            dino[i].updateSprite = 0

        if not dino[i].IsJumping and not dino[i].IsSuperJumping:
            dino[i].Y = 180
            
            if not dino[i].IsLower:
                dino[i].posY = 185
                dino[i].X = 100

                dino[i].posColX = dino[i].X + 40
                dino[i].posColY = dino[i].Y + 35

                window.blit(dino[i].RunningImage[dino[i].updateSprite//4], (dino[i].X, dino[i].Y))

            else:
                dino[i].posY = + 20
                dino[i].X = 90

                dino[i].posColX = dino[i].X + 70
                dino[i].posColY = dino[i].Y + 30

                window.blit(dino[i].LowerImage[dino[i].updateSprite//4], (dino[i].X, dino[i].Y))            

            #if keys[pygame.K_UP]:
            if pular:
                entradasAntesAcao = entradas
                jumpDef(i)

            #elif keys[pygame.K_DOWN]:
            elif abaixar:
                lowerDef(i)

            '''
            #elif keys[pygame.K_SPACE] and allowSuperJump:
            elif superJumping and dino[i].allowSuperJump:
                superJumpDef(i)
            
            else:
                dinoIsLower = False
            '''
        elif dino[i].IsJumping and not dino[i].IsSuperJumping:  # DinoIsJumping
            #if keys[pygame.K_DOWN]:
            if abaixar:
                lowerDef(i)
            
            if dino[i].CountJump >= -7.5:
                upDown = 1
                
                if dino[i].CountJump < 0:
                    upDown = -1
                
                dino[i].Y -= (dino[i].CountJump ** 2) * 0.5 * upDown

                dino[i].CountJump -= 1

            else:
                dino[i].IsJumping = False
                dino[i].CountJump = 7.5

            dino[i].posY = dino[i].Y + 5

            dino[i].posColX = dino[i].X + 30
            dino[i].posColY = dino[i].Y + 30

            window.blit(dino[i].JumpingImage, (dino[i].X, dino[i].Y))

        elif dino[i].IsSuperJumping:  # DinoIsSUperJumping
            #if keys[pygame.K_DOWN]:
            if abaixar:
                lowerDef(i)

            if dino[i].CountJump >= -9:
                upDown = 1
                
                if dino[i].CountJump < 0:
                    upDown = -1
                
                dino[i].Y -= (dino[i].CountJump ** 2) * 0.5 * upDown

                dino[i].CountJump -= 1

            else:
                dino[i].IsSuperJumping = False
                dino[i].CountJump = 9

            dino[i].posY = dino[i].Y + 5

            dino[i].posColX = dino[i].X + 40
            dino[i].posColY = dino[i].Y + 35

            window.blit(dino[i].JumpingImage, (dino[i].X, dino[i].Y))

        dino[i].updateSprite += 1

        dino[i].height = dino[i].Y

        if countGround % 500 == 0:
            if dino[i].auxSuperJump != 7:
                dino[i].auxSuperJump += 1

            if dino[i].auxSuperJump == 7:
                dino[i].allowSuperJump = True

        #window.blit(pygame.image.load('../Sprites/redes.png'), (dino[i].posColX, dino[i].posColY))

        '''
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
        '''

def jumpDef(i):
    global dino    
    dino[i].IsJumping = True
    dino[i].CountJump = 7.5

def lowerDef(i):
    global dino
    if not dino[i].IsSuperJumping and not dino[i].IsJumping:
        dinoIsLower = True 

    elif dino[i].IsSuperJumping or dino[i].IsJumping:
        dino[i].CountJump -= 3

def superJumpDef(i):

    '''
    global dino
    dino[i].IsSuperJumping = True
    dino[i].CountJump = 9
    dino[i].allowSuperJump = False
    dino[i].auxSuperJump = 0
    '''

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
        if auxMountainAppear == 2:
            auxMountainAppear = 0
            #mountainExist = True
            #mountainCount = 1100

            setBird()

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
    #setBird()

    #
    updateBird()

def setBird():
    global birdExist, birdCount, birdPlace, auxCountBird
    #if score > 500:
    #if countGround % 1000 == 0:
    #    auxCountBird += 1

    #if random.randint(0, 9) >= 0 and auxCountBird == 2:

    auxCountBird = 0
    birdExist = True
    birdCount = 1100
    birdPlace = random.randint(1, 2)

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
            birdCount = 1100


    else:
        birdCount = 1100

def setObstacleSize():
    global widthCactus, heightCactusBegin, heightCactusEnd, auxCactusCollider
    global widthObstacle, heightObstacle, distanceObstacle, dino

    widthCactusA = cactusImage[cactusNumA].get_size()[0]
    widthCactusB = cactusImage[cactusNumB].get_size()[0]

    if (cactusCountA < cactusCountB) and (cactusCountA < birdCount) and (cactusCountA < mountainCount) and (dino[0].posColX < cactusCountA + widthCactusA):
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
        distanceObstacle = cactusCountA - dino[0].posX

        auxCactusCollider = cactusCountA - 50

    elif (cactusCountA > cactusCountB) and (birdCount > cactusCountB) and (mountainCount > cactusCountB) and (dino[0].posColX < cactusCountB + widthCactusB):
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
        distanceObstacle = cactusCountB - dino[0].posX

        auxCactusCollider = cactusCountB - 50

    else:
        auxCactusCollider = 950

    if (mountainCount < cactusCountA) and (mountainCount < cactusCountB) and (mountainCount < birdCount) and (dino[0].posColX < mountainCount + 140):
        widthObstacle = 140
        heightObstacle = 110
        distanceObstacle = mountainCount - dino[0].posX

    if (birdCount < cactusCountA) and (birdCount < cactusCountB) and (birdCount < mountainCount) and (dino[0].posColX < birdCount + 60):
        widthObstacle = 60
        heightObstacle = posBirdY
        distanceObstacle = birdCount - dino[0].posX

def onColliderCactus(i):
    global restartAll, dino, entradasAntesAcao

    if (dino[i].posColX > auxCactusCollider) and (dino[i].posColY > (245 - heightCactusBegin)) and (dino[i].posColX < (auxCactusCollider + (widthCactus / 2))):
        #restartAll = True
        dino[i].dead = True
        
        if not isGenetic:        
            if dino[i].IsJumping:
                dino[i].cerebro.train(entradasAntesAcao, [0])
            else:
                dino[i].cerebro.train(entradas, [1])

    elif (dino[i].posColX > (auxCactusCollider + (widthCactus / 2))) and (dino[i].posColY > (245 - heightCactusEnd)) and ((dino[i].posColX - 25) < (auxCactusCollider + widthCactus)):
        #restartAll = True
        dino[i].dead = True
        
        if not isGenetic:
            if dino[i].IsJumping:
                dino[i].cerebro.train(entradasAntesAcao, [0])
            else:
                dino[i].cerebro.train(entradas, [1])

def onColliderBird(i):
    global restartAll

    if dino[i].IsLower:
        if (dino[i].posColX > (birdCount - 50)) and (dino[i].posColX < ((birdCount + 60) - 50)) and (dino[i].posColY > (posBirdY + 10)) and (dino[i].posColY < (posBirdY + 42)):
            #restartAll = True
            dino[i].dead = True

            if not isGenetic:        
                if dino[i].IsJumping:
                    dino[i].cerebro.train(entradasAntesAcao, [0])
                else:
                    dino[i].cerebro.train(entradas, [1])

    elif dino[i].IsJumping:
        if (dino[i].posColX > (birdCount - 50)) and (dino[i].posColX < ((birdCount + 60) - 50)) and ((dino[i].posColY - 20) > (posBirdY + 10)) and ((dino[i].posColY - 20) < (posBirdY + 42)):
            dino[i].dead = True  

            if not isGenetic:        
                if dino[i].IsJumping:
                    dino[i].cerebro.train(entradasAntesAcao, [0])
                else:
                    dino[i].cerebro.train(entradas, [1])

    else:
        if (dino[i].posColX > (birdCount - 50)) and (dino[i].posColX < ((birdCount + 60) - 50)) and (dino[i].posColY > (posBirdY + 10)) and ((dino[i].posColY - 20) < (posBirdY + 42)):
            dino[i].dead = True

            if not isGenetic:        
                if dino[i].IsJumping:
                    dino[i].cerebro.train(entradasAntesAcao, [0])
                else:
                    dino[i].cerebro.train(entradas, [1])

if __name__ == '__main__':
    main()

pygame.quit()
