import pygame, sys
from pygame.locals import *
import classes.background as background

pygame.init()
# main values
clock = pygame.time.Clock()


def duelStart(DISPLAYSURF, player, npc):
    print("Time to duel!")
    nameDuelFont = pygame.font.Font(None,100)
    
    # # characters
    # player
    playersName = nameDuelFont.render(f"{player.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    playersDeck = nameDuelFont.render(f"{len(player.deck)}", 0, (0, 0, 0), (255, 255, 255))
    playersGy = nameDuelFont.render(f"{len(player.gy)}", 0, (0, 0, 0), (255, 255, 255))
    # npc
    npcsName = nameDuelFont.render(f"{npc.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    npcsDeck = nameDuelFont.render(f"{len(npc.deck)}", 0, (0, 0, 0), (255, 255, 255))
    npcsGy = nameDuelFont.render(f"{len(npc.gy)}", 0, (0, 0, 0), (255, 255, 255))
    # npc

    while True:
        DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # # characters
        # player
        DISPLAYSURF.blit(playersName, (0,730))
        DISPLAYSURF.blit(playersDeck, (1100,600))
        DISPLAYSURF.blit(playersGy, (1100,450))
        # npc
        DISPLAYSURF.blit(npcsName, (0,0))
        DISPLAYSURF.blit(npcsDeck, (550,150))
        DISPLAYSURF.blit(npcsGy, (550,300))

        pygame.display.update()
        clock.tick(60)


# if __name__ == '__main__':
#     duelStart()