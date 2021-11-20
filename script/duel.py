import pygame, sys
from pygame.locals import *
import classes.background as background

pygame.init()
# main values
clock = pygame.time.Clock()


def duelStart(DISPLAYSURF, player, npc):
    print("Time to duel!")
    nameDuelFont = pygame.font.Font(None,100)
    playersName = nameDuelFont.render(f"{player.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    # playersName = nameDuelFont.render(player.name, 0, (0, 0, 0), (255, 255, 255))
    # npcsName = nameDuelFont.render(npc.name, 0, (0, 0, 0), (255, 255, 255))
    npcsName = nameDuelFont.render(f"{npc.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    while True:
        DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.blit(playersName, (0,0))
        DISPLAYSURF.blit(npcsName, (0,730))
        pygame.display.update()
        clock.tick(60)


# if __name__ == '__main__':
#     duelStart()