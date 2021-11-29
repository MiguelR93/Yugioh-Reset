import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
from script import duel

pygame.init()
# main values
clock = pygame.time.Clock()

# Fonts:
turnCounterFont = pygame.font.Font(None,60)
nameDuelFont = pygame.font.Font(None,100) # genérico

def printHand(DISPLAYSURF, character, characterHandY):
    CHARACTERHAND = 500
    for i in character.hand:
        # if isinstance(i, card.MonsterNormal):
        #     print("sí es monstruo nomral!")
        #     DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, characterHandY))
        # else:
        #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (CHARACTERHAND, characterHandY, 50, 50), 2)
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, characterHandY, 82, 118), 0)
        DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, characterHandY))
        i.cardX, i.cardY = CHARACTERHAND, characterHandY
        i.makeARect()
        CHARACTERHAND += (1150-500)/len(character.hand)


def drawingAll(DISPLAYSURF, player, npc):
    DISPLAYSURF.fill((255, 255, 255))
    # DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))
    playerFace = Rect(0,0,133,133)
    npcFace = Rect(1067,0,133,133)
    playerLifeAll = ((134,0),(533,0), (444,88), (134,88))
    npcLifeAll = ((1066,0),(667,0), (756,88), (1066,88))

    gameField = Rect(267,178,665,532)

    pygame.draw.rect(DISPLAYSURF, (255,0,0), playerFace)
    pygame.draw.rect(DISPLAYSURF, (0,0,255), npcFace)
    pygame.draw.polygon(DISPLAYSURF, (0,255,0), playerLifeAll, 0)
    pygame.draw.polygon(DISPLAYSURF, (0,255,0), npcLifeAll, 0)
    pygame.draw.rect(DISPLAYSURF, (255,255,0), gameField, 0)
    # # this should drawing all ;v
    # # Duel status: Lo moví porque aquí sí se actualiza :)
    tcText = turnCounterFont.render(f"Turno:", 0, (0, 0, 0), (255, 255, 255))
    tcTextNumber = turnCounterFont.render(f"{duel.TURNSCOUNTER}", 0, (0, 0, 0), (255, 255, 255))

    # Duel status:
    DISPLAYSURF.blit(tcText, (535,0))
    DISPLAYSURF.blit(tcTextNumber, (585,50))


    # # # characters
    # # player
    # playersName = nameDuelFont.render(f"{player.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    # playersDeck = nameDuelFont.render(f"{len(player.deck)}", 0, (0, 0, 0), (255, 255, 255))
    # playersGy = nameDuelFont.render(f"{len(player.gy)}", 0, (0, 0, 0), (255, 255, 255))
    # # npc
    # npcsName = nameDuelFont.render(f"{npc.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    # npcsDeck = nameDuelFont.render(f"{len(npc.deck)}", 0, (0, 0, 0), (255, 255, 255))
    # npcsGy = nameDuelFont.render(f"{len(npc.gy)}", 0, (0, 0, 0), (255, 255, 255))




    

    # # # characters
    # # player
    # DISPLAYSURF.blit(playersName, (0,730))
    # DISPLAYSURF.blit(playersDeck, (1100,600))
    # DISPLAYSURF.blit(playersGy, (1100,450))
    # # drawing player's hand
    # # PLAYERHAND = 500
    # # for i in player.hand:
    # #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (PLAYERHAND, 700, 50, 50))
    # #     PLAYERHAND += (1150-500)/len(player.hand)
    # printHand(DISPLAYSURF, player, 700)
        
    # # npc
    # DISPLAYSURF.blit(npcsName, (0,0))
    # DISPLAYSURF.blit(npcsDeck, (550,150))
    # DISPLAYSURF.blit(npcsGy, (550,300))
    # # drawing npc's hand
    # # NPCHAND = 500
    # # for i in npc.hand:
    # #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (NPCHAND, 0, 50, 50))
    # #     NPCHAND += (1150-500)/len(npc.hand)
    # printHand(DISPLAYSURF, npc, 0)


    # print("ya debería actualizarse ._.")
    pygame.display.update()
    clock.tick(3)