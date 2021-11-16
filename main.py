import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters

pygame.init()

clock = pygame.time.Clock()

# # background ----
# posBackground = (0,0)
# background00 = pygame.image.load("./images/background00.png")
# front00 = pygame.image.load("./images/front00.png")

DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Yu-Gi-Oh! Reset')

while True:
    DISPLAYSURF.blit(background.front00, (background.posBackground))
    
    # characters ------
    # player
    DISPLAYSURF.blit(characters.Player.avatar, (characters.Player.playerX, characters.Player.playerY))
    characters.Player.movement()

    # detecting input ------
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    clock.tick(60)