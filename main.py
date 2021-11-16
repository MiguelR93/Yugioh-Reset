import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters

pygame.init()

clock = pygame.time.Clock()

# # Characters -------
# Player:
playerX, playerY = 600, 400
speed = 5


DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Yu-Gi-Oh! Reset')

while True:
    # detecting input ------
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background.front00, (background.posBackground))
    
    # characters ------
    # player
    protagonista = characters.Player(1, "Drakdio", playerX, playerY, pygame.image.load("./images/characters/kaibaF01.png"))
    # protagonista.movimiento()
            
    if event.type == pygame.KEYDOWN:
        print(playerX)
        if event.key == pygame.K_LEFT:
            print("Izquierda, player!")
            if playerX <= 0:
                playerX += 0
            else:    
                playerX -= speed
        elif event.key == pygame.K_RIGHT:
            print("Derecha, player!")
            if playerX >= 1200:
                playerX += 0
            else: 
                playerX += speed
        elif event.key == pygame.K_UP:
            print("Arriba, player!")
            if playerY <= 0:
                playerY -= 0
            else: 
                playerY -= speed
        elif event.key == pygame.K_DOWN:
            print("Abajo, player!")
            if playerY >= 800:
                playerY += 0
            else: 
                playerY += speed
    
    protagonistaAvatar = DISPLAYSURF.blit(protagonista.avatar, (playerX, protagonista.playerY))
    
    pygame.display.update()
    clock.tick(60)