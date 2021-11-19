import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters

pygame.init()

# main values
DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Yu-Gi-Oh! Reset')
clock = pygame.time.Clock()

# # Characters -------
speedX, speedY = 75, 80
# Player: 75x160
playerX, playerY = 600, 320
protagonista = characters.Player(1, "Drakdio", playerX, playerY, pygame.image.load("./images/characters/kaibaF01.png"), pygame.image.load("./images/characters/kaibaR01.png"), pygame.image.load("./images/characters/kaibaL01.png"), pygame.image.load("./images/characters/kaibaB01.png"))
currentPlyayerAvatar = protagonista.avatarFront
# def protagonistaAvatar(): DISPLAYSURF.blit(currentPlyayerAvatar, (playerX, playerY)) # funcionaría?


# NPC:
# npc1
npc1X, npc1Y = 75, 320
npc1 = characters.Npc(1, "Kaiba", npc1X, npc1Y, pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), "Hola", "Duelo!")
# npc2
npc2X, npc2Y = 5*75, 400
npc2 = characters.Npc(1, "Kaiba", npc1X, npc1Y, pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), "Hola", "Duelo!")
# npc3
npc3X, npc3Y = 3*75, 480
npc3 = characters.Npc(1, "Kaiba", npc1X, npc1Y, pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), "Hola", "Duelo!")
npcList = [[npc1, npc1X, npc1Y], [npc2, npc2X, npc2Y], [npc3, npc3X, npc3Y]]



while True:
    # detecting input ------
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background.front00, (background.posBackground))

    # # Characters -------
    # Player: 75x160
    if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_LEFT:
        #     if currentPlyayerAvatar != protagonista.avatarLeft:
        #         currentPlyayerAvatar = protagonista.avatarLeft
        #     else:
        #         if playerX <= 0:
        #             playerX += 0
        #         elif (playerX == npc1X + 75) and (playerY == npc1Y):
        #             print("Aquí hay alguien")
        #             playerX += 0
        #         else:    
        #             playerX -= speedX

        # elif event.key == pygame.K_RIGHT:
        #     if currentPlyayerAvatar != protagonista.avatarRight:
        #         currentPlyayerAvatar = protagonista.avatarRight
        #     else:
        #         if playerX >= 1125: #1200-75
        #             playerX += 0
        #         elif (playerX + 75 == npc1X) and (playerY == npc1Y):
        #             print("Aquí hay alguien")
        #             playerX -= 0
        #         else: 
        #             playerX += speedX

        # elif event.key == pygame.K_UP:
        #     if currentPlyayerAvatar != protagonista.avatarBack:
        #         currentPlyayerAvatar = protagonista.avatarBack
        #     else:
        #         if playerY <= 0:
        #             playerY -= 0
        #         elif (playerX == npc1X) and (playerY == npc1Y + 80):
        #             print("Aquí hay alguien")
        #             playerY -= 0
        #         else: 
        #             playerY -= speedY

        # elif event.key == pygame.K_DOWN:
        #     if currentPlyayerAvatar != protagonista.avatarFront:
        #         currentPlyayerAvatar = protagonista.avatarFront
        #     else:
        #         if playerY >= 640: #800-160
        #             playerY += 0
        #         elif (playerX == npc1X) and (playerY + 80 == npc1Y):
        #             print("Aquí hay alguien")
        #             playerY += 0
        #         else: 
        #             playerY += speedY
    
        if event.key == pygame.K_LEFT:
            if currentPlyayerAvatar != protagonista.avatarLeft:
                currentPlyayerAvatar = protagonista.avatarLeft
            else:
                if (playerX == npc1X + 75) and (playerY == npc1Y):
                    print("Aquí hay alguien")
                    playerX += 0
                else:
                    if playerX <= 0:
                        playerX += 0
                    else:    
                        playerX -= speedX

        elif event.key == pygame.K_RIGHT:
            if currentPlyayerAvatar != protagonista.avatarRight:
                currentPlyayerAvatar = protagonista.avatarRight
            else:
                if (playerX + 75 == npc1X) and (playerY == npc1Y):
                    print("Aquí hay alguien")
                    playerX -= 0
                else:
                    if playerX >= 1125: #1200-75
                        playerX += 0
                    else: 
                        playerX += speedX

        elif event.key == pygame.K_UP:
            if currentPlyayerAvatar != protagonista.avatarBack:
                currentPlyayerAvatar = protagonista.avatarBack
            else:
                if (playerX == npc1X) and (playerY == npc1Y + 80):
                    print("Aquí hay alguien")
                    playerY -= 0
                else:
                    if playerY <= 0:
                        playerY -= 0
                    else: 
                        playerY -= speedY
                    
        elif event.key == pygame.K_DOWN:
            if currentPlyayerAvatar != protagonista.avatarFront:
                currentPlyayerAvatar = protagonista.avatarFront
            else:
                if (playerX == npc1X) and (playerY + 80 == npc1Y):
                    print("Aquí hay alguien")
                    playerY += 0
                else:
                    if playerY >= 640: #800-160
                        playerY += 0
                    else: 
                        playerY += speedY

    protagonistaAvatar = DISPLAYSURF.blit(currentPlyayerAvatar, (playerX, playerY))
    # protagonistaAvatar() # parece funcionar, pero cuál es el límite?
    
    # NPC:
    # enemy1 = DISPLAYSURF.blit(npc1.avatarFront, (npc1X, npc1Y))
    for i in npcList:
        i = DISPLAYSURF.blit(i[0].avatarFront, (i[1], i[2]))
    
    pygame.display.update()
    clock.tick(60)