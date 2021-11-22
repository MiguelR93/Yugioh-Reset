import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card

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


def drawingAll(nameDuelFont, DISPLAYSURF, player, npc):
    DISPLAYSURF.fill((255, 255, 255))
    DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))
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



    # Duel status:
    DISPLAYSURF.blit(tcText, (880,0))

    # # characters
    # player
    DISPLAYSURF.blit(playersName, (0,730))
    DISPLAYSURF.blit(playersDeck, (1100,600))
    DISPLAYSURF.blit(playersGy, (1100,450))
    # drawing player's hand
    # PLAYERHAND = 500
    # for i in player.hand:
    #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (PLAYERHAND, 700, 50, 50))
    #     PLAYERHAND += (1150-500)/len(player.hand)
    printHand(DISPLAYSURF, player, 700)
        
    # npc
    DISPLAYSURF.blit(npcsName, (0,0))
    DISPLAYSURF.blit(npcsDeck, (550,150))
    DISPLAYSURF.blit(npcsGy, (550,300))
    # drawing npc's hand
    # NPCHAND = 500
    # for i in npc.hand:
    #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (NPCHAND, 0, 50, 50))
    #     NPCHAND += (1150-500)/len(npc.hand)
    printHand(DISPLAYSURF, npc, 0)


    # print("ya debería actualizarse ._.")
    pygame.display.update()
    clock.tick(3)


def duelStart(DISPLAYSURF, player, npc, myMouse):
    # global TURNSCOUNTER
    print("Time to duel!")
    nameDuelFont = pygame.font.Font(None,100)

    players['p1'] = player
    players['p2'] = npc
    
    players['p1'].oponent = npc
    players['p2'].oponent = player

    while True:
        # print(myMouse) # funciona!
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
            
            myMouse = pygame.mouse.get_pos()
            print(myMouse)
            


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
        
            for a, i in enumerate(players[i].hand):
                # detecta si el mouse está sobre alguna carta de la mano
                # if myMouse == (i.rectangulo.left, i.rectangulo.top):
                #     print("Estás en la figura")
                #     littleSleep()
                if (myMouse[0] >= i.rectangulo.left) and (myMouse[0] <= i.rectangulo.left + i.rectangulo.width) and (myMouse[1] >= i.rectangulo.top) and (myMouse[1] <= i.rectangulo.top + i.rectangulo.height):
                    # print(f"dentro del rectángulo {a}")
                    i.options()
                    # littleSleep()
                # else:
                #     print(f"Rectángulo: {i.rectangulo.left}, {i.rectangulo.top}")
                #     littleSleep()

            drawingAll(nameDuelFont, DISPLAYSURF, player, npc)

            


# if __name__ == '__main__':
#     duelStart()