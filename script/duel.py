import pygame, sys, time
from pygame.locals import *
import classes.background as background

pygame.init()
# main values
clock = pygame.time.Clock()

# duel values
TURNSCOUNTER = 0
players = {}


# Duel tools ----------------
def littleSleep(): time.sleep(1)


def victory():
    if players['p1'].victory == False:
        return False
    elif players['p2'].victory == False:
        return False
    else:
        return True


def turnStarts():
    global TURNSCOUNTER
    TURNSCOUNTER += 1


def currentlyTurn():
    return TURNSCOUNTER


def drawingAll(nameDuelFont, DISPLAYSURF, player, npc):
    # this should drawing all ;v
    # Duel status: Lo moví porque aquí sí se actualiza :)
    tcText = nameDuelFont.render(f"Turno: {TURNSCOUNTER}", 0, (0, 0, 0), (255, 255, 255))

    # # characters
    # player
    playersName = nameDuelFont.render(f"{player.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    playersDeck = nameDuelFont.render(f"{len(player.deck)}", 0, (0, 0, 0), (255, 255, 255))
    playersGy = nameDuelFont.render(f"{len(player.gy)}", 0, (0, 0, 0), (255, 255, 255))
    # npc
    npcsName = nameDuelFont.render(f"{npc.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
    npcsDeck = nameDuelFont.render(f"{len(npc.deck)}", 0, (0, 0, 0), (255, 255, 255))
    npcsGy = nameDuelFont.render(f"{len(npc.gy)}", 0, (0, 0, 0), (255, 255, 255))

    DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))


    # Duel status:
    DISPLAYSURF.blit(tcText, (880,0))

    # # characters
    # player
    DISPLAYSURF.blit(playersName, (0,730))
    DISPLAYSURF.blit(playersDeck, (1100,600))
    DISPLAYSURF.blit(playersGy, (1100,450))
    # drawing player's hand
    PLAYERHAND = 500
    for i in player.hand:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (PLAYERHAND, 700, 50, 50))
        PLAYERHAND += 100
    # npc
    DISPLAYSURF.blit(npcsName, (0,0))
    DISPLAYSURF.blit(npcsDeck, (550,150))
    DISPLAYSURF.blit(npcsGy, (550,300))
    # drawing npc's hand
    NPCHAND = 500
    for i in npc.hand:
        pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (NPCHAND, 0, 50, 50))
        NPCHAND += 100


    # print("ya debería actualizarse ._.")
    pygame.display.update()
    clock.tick(1)


def duelStart(DISPLAYSURF, player, npc):
    # global TURNSCOUNTER
    print("Time to duel!")
    nameDuelFont = pygame.font.Font(None,100)

    players['p1'] = player
    players['p2'] = npc
    
    players['p1'].oponent = npc
    players['p2'].oponent = player

    while True:
        # # duel starts!
        # shuffle players' deck
        for i in players:
            players[i].shuffleDeck()
        # Every player draws until have 4 cards
        for i in players:
            while len(players[i].hand) < 4:
                players[i].drawACard()
                drawingAll(nameDuelFont, DISPLAYSURF, player, npc)
        for i in players:
            turnStarts()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # print(f"Empieza el turno de {players[i].name}")
            # turnStarts()
            # print(currentlyTurn())
            # print(f"Fase de robo de {players[i].name}")
            # print(f"Fase principal de {players[i].name}")
            # print(f"Fase de batalla de {players[i].name}")
            # print(f"Fase final de {players[i].name}")
            # # littleSleep()

            # # Duel status: Lo moví porque aquí sí se actualiza :)
            # tcText = nameDuelFont.render(f"Turno: {TURNSCOUNTER}", 0, (0, 0, 0), (255, 255, 255))

            # # # characters
            # # player
            # playersName = nameDuelFont.render(f"{player.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
            # playersDeck = nameDuelFont.render(f"{len(player.deck)}", 0, (0, 0, 0), (255, 255, 255))
            # playersGy = nameDuelFont.render(f"{len(player.gy)}", 0, (0, 0, 0), (255, 255, 255))
            # # npc
            # npcsName = nameDuelFont.render(f"{npc.name}: {npc.lp}", 0, (0, 0, 0), (255, 255, 255))
            # npcsDeck = nameDuelFont.render(f"{len(npc.deck)}", 0, (0, 0, 0), (255, 255, 255))
            # npcsGy = nameDuelFont.render(f"{len(npc.gy)}", 0, (0, 0, 0), (255, 255, 255))
            # # npc


            
            
            # DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))


            # # Duel status:
            # DISPLAYSURF.blit(tcText, (880,0))

            # # # characters
            # # player
            # DISPLAYSURF.blit(playersName, (0,730))
            # DISPLAYSURF.blit(playersDeck, (1100,600))
            # DISPLAYSURF.blit(playersGy, (1100,450))
            # # npc
            # DISPLAYSURF.blit(npcsName, (0,0))
            # DISPLAYSURF.blit(npcsDeck, (550,150))
            # DISPLAYSURF.blit(npcsGy, (550,300))


            # print("ya debería actualizarse ._.")
            # pygame.display.update()
            # clock.tick(1)

            


            # # turns!
            # drawPhase:
            print(players[i].hand) #solo para comprobar que shuffle deck funciona :)
            players[i].drawPhase()
            print(players[i].hand) #solo para comprobar que shuffle deck funciona :)
            drawingAll(nameDuelFont, DISPLAYSURF, player, npc)
            # MainPhase:
            print("ahora en Main Phase")
            # BattlePhase
            print("ahora en Battle Phase")
            # End Phase
            print("ahora en End Phase")

            drawingAll(nameDuelFont, DISPLAYSURF, player, npc)

            


# if __name__ == '__main__':
#     duelStart()