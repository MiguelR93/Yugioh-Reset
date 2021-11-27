# Crea la partida del jugador

import pygame, sys
from pygame.locals import *
import main

pygame.init()


# Colors -----------
WHITE = (255, 255, 255)



# def firstWindow():
#     firstFont = pygame.font.Font(None, 30)
#     newGame = firstFont.render("Nueva partida", (0,0,255))
#     return newGame

def gameStart(DISPLAYSURF):
    backColor = None
    backColor2 = None
    backPlace = 0
    firstFont = pygame.font.Font(None, 80)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (backPlace == 1):
                    backPlace -= 1
                elif (event.key == pygame.K_RIGHT) and (backPlace == 0):
                    backPlace += 1        

        DISPLAYSURF.fill((255,0,0))
        if backPlace == 0:
            backColor, backColor2 = WHITE, None
        elif backPlace == 1:
            backColor, backColor2 = None, WHITE
        newGame = firstFont.render("Nueva partida", 0, (0,0,255), backColor)
        continueGame = firstFont.render("Continuar partida", 0, (0,0,255), backColor2)
        DISPLAYSURF.blit(newGame, (50, 350))
        DISPLAYSURF.blit(continueGame, (650, 350))
      
        
        pygame.display.update()
        main.clock.tick(60)