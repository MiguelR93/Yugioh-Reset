import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters

pygame.init()

clock = pygame.time.Clock()

# # Characters -------
# Player: 75x160
playerX, playerY = 600, 320
speedX, speedY = 75, 160
protagonista = characters.Player(1, "Drakdio", playerX, playerY, pygame.image.load("./images/characters/kaibaF01.png"))


DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Yu-Gi-Oh! Reset')

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
        if event.key == pygame.K_LEFT:
            if playerX <= 0:
                playerX += 0
            else:    
                playerX -= speedX
        elif event.key == pygame.K_RIGHT:
            if playerX >= 1125: #1200-75
                playerX += 0
            else: 
                playerX += speedX
        elif event.key == pygame.K_UP:
            if playerY <= 0:
                playerY -= 0
            else: 
                playerY -= speedY
        elif event.key == pygame.K_DOWN:
            if playerY >= 640: #800-160
                playerY += 0
            else: 
                playerY += speedY
    
    protagonistaAvatar = DISPLAYSURF.blit(protagonista.avatar, (playerX, playerY))
    
    pygame.display.update()
    clock.tick(60)