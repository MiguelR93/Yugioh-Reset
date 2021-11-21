import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters
from script import duel
import classes.openDeck as openDeck

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
protagonista.deck = openDeck.openDeck()

# NPC:
# npc1
npc1X, npc1Y = 75, 320
npc1 = characters.Npc(1, "Kaiba", npc1X, npc1Y, pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), "Hola", "Duelo!")
npc1.deck = openDeck.openDeck()

# main loop:
def gameLoop():
    while True:
        # print("Hola!")
    # detecting input ------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        duel.duelStart(DISPLAYSURF, protagonista, npc1)

        pygame.display.update()
        clock.tick(60)

# while True:
#     # detecting input ------
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     DISPLAYSURF.blit(background.front00, (background.posBackground))

#     # # Characters -------
#     # Player: 75x160
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_LEFT:
#             if currentPlyayerAvatar != protagonista.avatarLeft:
#                 currentPlyayerAvatar = protagonista.avatarLeft
#             else:
#                 if playerX <= 0:
#                     playerX += 0
#                 elif (playerX == npc1X + 75) and (playerY == npc1Y):
#                     print("Aquí hay alguien")
#                     playerX += 0
#                 else:    
#                     playerX -= speedX
#         elif event.key == pygame.K_RIGHT:
#             if currentPlyayerAvatar != protagonista.avatarRight:
#                 currentPlyayerAvatar = protagonista.avatarRight
#             else:
#                 if playerX >= 1125: #1200-75
#                     playerX += 0
#                 elif (playerX + 75 == npc1X) and (playerY == npc1Y):
#                     print("Aquí hay alguien")
#                     playerX -= 0
#                 else: 
#                     playerX += speedX
#         elif event.key == pygame.K_UP:
#             if currentPlyayerAvatar != protagonista.avatarBack:
#                 currentPlyayerAvatar = protagonista.avatarBack
#             else:
#                 if playerY <= 0:
#                     playerY -= 0
#                 elif (playerX == npc1X) and (playerY == npc1Y + 80):
#                     print("Aquí hay alguien")
#                     playerY -= 0
#                 else: 
#                     playerY -= speedY
#         elif event.key == pygame.K_DOWN:
#             if currentPlyayerAvatar != protagonista.avatarFront:
#                 currentPlyayerAvatar = protagonista.avatarFront
#             else:
#                 if playerY >= 640: #800-160
#                     playerY += 0
#                 elif (playerX == npc1X) and (playerY + 80 == npc1Y):
#                     print("Aquí hay alguien")
#                     playerY += 0
#                 else: 
#                     playerY += speedY
    
#     protagonistaAvatar = DISPLAYSURF.blit(currentPlyayerAvatar, (playerX, playerY))
#     # protagonistaAvatar() # parece funcionar, pero cuál es el límite?
    
#     # NPC:
#     enemy1 = DISPLAYSURF.blit(npc1.avatarFront, (npc1X, npc1Y))
    
#     pygame.display.update()
#     clock.tick(60)


if __name__ == '__main__':
    gameLoop()