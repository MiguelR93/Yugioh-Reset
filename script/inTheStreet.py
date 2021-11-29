import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters
from script import duel
import classes.openDeck as openDeck

pygame.init()
clock = pygame.time.Clock()


def streetLoop(DISPLAYSURF, protagonista, npc):
    print("En la función de la calle")
    currentPlyayerAvatar = protagonista.avatarFront
    while True:
        print("En el bucle de la calle")
        DISPLAYSURF.blit(background.front00, (background.posBackground))
        # detecting input ------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            # # Characters -------
            # Player: 75x160
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if currentPlyayerAvatar != protagonista.avatarLeft:
                        currentPlyayerAvatar = protagonista.avatarLeft
                    else:
                        if protagonista.playerX <= 0:
                            protagonista.playerX += 0
                        elif (protagonista.playerX == npc.playerX + 75) and (protagonista.playerY == npc.playerY):
                            print("Aquí hay alguien")
                            protagonista.playerX += 0
                        else:    
                            protagonista.playerX -= protagonista.speedX
                elif event.key == pygame.K_RIGHT:
                    if currentPlyayerAvatar != protagonista.avatarRight:
                        currentPlyayerAvatar = protagonista.avatarRight
                    else:
                        if protagonista.playerX >= 1125: #1200-75
                            protagonista.playerX += 0
                        elif (protagonista.playerX + 75 == npc.playerX) and (protagonista.playerY == npc.playerY):
                            print("Aquí hay alguien")
                            protagonista.playerX -= 0
                        else: 
                            protagonista.playerX += protagonista.speedX
                elif event.key == pygame.K_UP:
                    if currentPlyayerAvatar != protagonista.avatarBack:
                        currentPlyayerAvatar = protagonista.avatarBack
                    else:
                        if protagonista.playerY <= 0:
                            protagonista.playerY -= 0
                        elif (protagonista.playerX == npc.playerX) and (protagonista.playerY == npc.playerY + 80):
                            print("Aquí hay alguien")
                            protagonista.playerY -= 0
                        else: 
                            protagonista.playerY -= protagonista.speedY
                elif event.key == pygame.K_DOWN:
                    if currentPlyayerAvatar != protagonista.avatarFront:
                        currentPlyayerAvatar = protagonista.avatarFront
                    else:
                        if protagonista.playerY >= 640: #800-160
                            protagonista.playerY += 0
                        elif (protagonista.playerX == npc.playerX) and (protagonista.playerY + 80 == npc.playerY):
                            print("Aquí hay alguien")
                            protagonista.playerY += 0
                        else: 
                            protagonista.playerY += protagonista.speedY
                
            # duel
            if event.type == pygame.KEYDOWN: # agregar que player esté mirando al npc
                if (event.key == pygame.K_RETURN) and (protagonista.playerX - 75 == npc.playerX):
                    print("Duelo!")
                    duel.duelStart(DISPLAYSURF, protagonista, npc, (0,0))
                elif (event.key == pygame.K_RETURN) and (protagonista.playerX + 75 == npc.playerX):
                    print("Duelo!")
                elif (event.key == pygame.K_RETURN) and (protagonista.playerY - 80 == npc.playerY):
                    print("Duelo!")
                elif (event.key == pygame.K_RETURN) and (protagonista.playerY + 80 == npc.playerY):
                    print("Duelo!")
        
        protagonistaAvatar = DISPLAYSURF.blit(currentPlyayerAvatar, (protagonista.playerX, protagonista.playerY))
        # protagonistaAvatar() # parece funcionar, pero cuál es el límite?
        
        # NPC:
        enemy1 = DISPLAYSURF.blit(npc.avatarFront, (npc.playerX, npc.playerY))
        
        pygame.display.update()
        clock.tick(60)