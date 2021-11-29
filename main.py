import pygame, sys
from pygame.locals import *
import classes.background as background
import classes.characters as characters
from script import duel
import classes.openDeck as openDeck
import script.gameStart as gameStart
import script.inTheStreet as inTheStreet

pygame.init()

# main values
DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption('Yu-Gi-Oh! Reset')
clock = pygame.time.Clock()

# # Characters -------
# speedX, speedY = 75, 80
# Player: 75x160
# playerX, playerY = 600, 320
protagonista = characters.Player(1, "Drakdio", 600, 320, pygame.image.load("./images/characters/kaibaF01.png"), pygame.image.load("./images/characters/kaibaR01.png"), pygame.image.load("./images/characters/kaibaL01.png"), pygame.image.load("./images/characters/kaibaB01.png"))
currentPlyayerAvatar = protagonista.avatarFront
# def protagonistaAvatar(): DISPLAYSURF.blit(currentPlyayerAvatar, (playerX, playerY)) # funcionaría?
protagonista.deck = openDeck.openDeck()

# NPC:
# npc1
npc1X, npc1Y = 75, 320
npc1 = characters.Npc(1, "Kaiba", 75, 320, pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), pygame.image.load("./images/characters/kaibaEvilF01.png"), "Hola", "Duelo!")
npc1.deck = openDeck.openDeck()

# main loop:
def mainLoop():
    while True:
        # print("Hola!")
    # detecting input ------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # myMouse = pygame.mouse.get_pos()
        # print(myMouse)

        # gameStart.gameStart(DISPLAYSURF)

        
        # inTheStreet.streetLoop(DISPLAYSURF, protagonista, npc1) # falta ver

        # duel.oldDuelStart(DISPLAYSURF, protagonista, npc1, myMouse)
        duel.duelStart(DISPLAYSURF, protagonista, npc1)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.mouse.set_visible(1)
    mainLoop()