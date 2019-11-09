import dinoHybrid
import pygame

dinoHybrid.gameInit()

#DefineIfTheGameIsRunningOrNot
isPlaying = True

#InfinitLoop
while isPlaying:

    #CloseTheGame
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:   
            isPlaying = False

    #ThingsToDo
    dinoHybrid.onUpdate()

