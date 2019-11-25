import dinoRedeNeural as rn
import pygame

# Classe para a auxiliar na manipulacão dos dinossauros
class DinoClasse(object):
    def __init__(self):
        #Rede Neural para o Dino
        self.cerebro = rn.Neural(5,5,1)

        #Variáveis gerais para o dino
        self.score = 0
        self.height = 0
        self.posX = 129
        self.posY = 0
        self.dead = False
        
        #Variáveis de relacionadas a uma ação que o dino pode fazer
        self.IsJumping = False
        self.IsSuperJumping = False
        self.IsLower= False
        self.countJump = 0
        self.allowSuperJump = True
        self.auxSuperJump = 0
        
        #PlaceToSetDinoImage
        self.X = 100
        self.Y = 180

        #PositionToDinoCollide
        self.posColX = 0
        self.posColY = 0

        #Variáveis relacionadas as Sprites Sprites para o dino
        self.updateSprite = 0
        #self.RunningImage = 0
        self.RunningImage = [pygame.image.load('../Sprites/Dino/dino_11.png'),
                                 pygame.image.load('../Sprites/Dino/dino_22.png')]
        self.LowerImage = [pygame.image.load('../Sprites/Dino/down_1.png'),
                               pygame.image.load('../Sprites/Dino/down_2.png')]
        self.JumpingImage = pygame.image.load('../Sprites/Dino/dino_jump.png')
        

