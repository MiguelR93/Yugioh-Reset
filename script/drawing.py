import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
from script import duel

pygame.init()
# main values
clock = pygame.time.Clock()

# Fonts:
turnCounterFont = pygame.font.Font(None,40)
phaseFont = pygame.font.Font(None,40)
cardOptionFont = pygame.font.Font(None,18)
nameDuelFont = pygame.font.Font(None,40) # genérico

def printHand(DISPLAYSURF, character, cartaOpciones):
    # CHARACTERHAND = 500
    # for i in character.hand:
    #     pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, characterHandY, 82, 118), 0)
    #     DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, characterHandY))
    #     i.cardX, i.cardY = CHARACTERHAND, characterHandY
    #     i.makeARect()
    #     CHARACTERHAND += (1150-500)/len(character.hand)


    # CHARACTERHAND = 500
    for i in character.hand: # dibuja cada carta
        pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (i.cardX, i.cardY, i.cardWidth, i.cardHeight), 0)
        DISPLAYSURF.blit(i.illustration, (i.cardX, i.cardY))
    
    if cartaOpciones != None:
        # pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (cartaOpciones.cardX, cartaOpciones.cardY - 25, cartaOpciones.cardWidth, 25), 0) # oculto temporalmente
        if isinstance(cartaOpciones, card.Monster) and (cartaOpciones.placeOnGame == "hand") and (character == cartaOpciones.owner):
            print(character.monstersInField(), cartaOpciones.owner.name)
            for i in cartaOpciones.options():
                print(f"Esto está en options: {i}")
                pygame.draw.rect(DISPLAYSURF, i[1], (cartaOpciones.cardX, i[0], cartaOpciones.cardWidth, 25), 0)
                # optionsCardText
                optionCardText = cardOptionFont.render(f"{i[2]}", 0, (0, 0, 0))
                DISPLAYSURF.blit(optionCardText, (cartaOpciones.cardX, i[0]))



def drawingAll(mousePosition,DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones):
    DISPLAYSURF.fill((255, 255, 255))
    # DISPLAYSURF.blit(background.fieldDuel, (background.posBackground))
    playerFace = Rect(0,0,150,150)
    npcFace = Rect(1050,0,150,150)
    playerNameRect = Rect(150,50,250,50)
    npcNameRect = Rect(800,50,250,50)
    playerLifeAll = ((150,0),(550,0),(500,50),(151,50))
    npcLifeAll = ((1049,0),(651,0),(700,50),(1049,50))


    # card
    cardImageNameRect = Rect(0,200,250,50)
    cardImageRect = Rect(0,200,250,250)
    cardImageIconRect = Rect(0,450,250,50)
    cardImageAtkDefRect = Rect(0,500,250,50)
    cardImageTextRect = Rect(0,550,250,250)

    pygame.draw.rect(DISPLAYSURF, (0,200,0), cardImageRect)
    pygame.draw.rect(DISPLAYSURF, (200,0,0), cardImageNameRect)
    pygame.draw.rect(DISPLAYSURF, (0,0,200), cardImageIconRect)
    pygame.draw.rect(DISPLAYSURF, (200,200,0), cardImageAtkDefRect)
    pygame.draw.rect(DISPLAYSURF, (200,0,200), cardImageTextRect, )


    gameField = Rect(300,200,625,500)

    pygame.draw.rect(DISPLAYSURF, (255,0,0), playerFace)
    pygame.draw.rect(DISPLAYSURF, (0,0,255), npcFace)
    pygame.draw.rect(DISPLAYSURF, (255,0,0), playerNameRect)
    pygame.draw.rect(DISPLAYSURF, (0,0,255), npcNameRect)
    pygame.draw.polygon(DISPLAYSURF, (0,255,0), playerLifeAll, 0)
    pygame.draw.polygon(DISPLAYSURF, (0,255,0), npcLifeAll, 0)
    # pygame.draw.rect(DISPLAYSURF, (255,255,0), gameField, 0)
    # # this should drawing all ;v
    # # Duel status: Lo moví porque aquí sí se actualiza :)
    tcText = turnCounterFont.render(f"Turno:", 0, (0, 0, 0), (255, 255, 255))
    tcTextNumber = turnCounterFont.render(duel.turnCounterText(), 0, (0, 0, 0), (255, 255, 255))

    # Duel status:
    DISPLAYSURF.blit(tcText, (555,0))
    DISPLAYSURF.blit(tcTextNumber, (585,30))


    # Phases rect
    drawPhaseRect = [Rect(975,225,175,75), "DrawPhase"]
    mainPhaseRect = [Rect(975,325,175,75), "MainPhase"]
    battlePhaseRect = [Rect(975,425,175,75), "BattlePhase"]
    endPhaseRect = [Rect(975,525,175,75), "EndPhase"]

    # tcText = turnCounterFont.render(f"Turno:", 0, (0, 0, 0), (255, 255, 255))

    phases = (drawPhaseRect, mainPhaseRect, battlePhaseRect, endPhaseRect,)

    # pygame.draw.rect(DISPLAYSURF, (255,0,0), drawPhaseRect)
    # pygame.draw.rect(DISPLAYSURF, (255,0,0), mainPhaseRect)
    # pygame.draw.rect(DISPLAYSURF, (255,0,0), battlePhaseRect)
    # pygame.draw.rect(DISPLAYSURF, (255,0,0), endPhaseRect)
    for i in phases: # phaseFont
        if currentlyPhase == i[1]:
            pygame.draw.rect(DISPLAYSURF, (255,0,0), i[0])
            phaseText = phaseFont.render(i[1], 0, (0,0, 255))
            DISPLAYSURF.blit(phaseText, (i[0].left,i[0].top+25))
        else:
            pygame.draw.rect(DISPLAYSURF, (0,0,0), i[0])
            phaseText = phaseFont.render(i[1], 0, (255, 255, 255))
            # phaseText = phaseFont.render(":)", 0, (0,0, 255))
            DISPLAYSURF.blit(phaseText, (i[0].left,i[0].top+25))



    # # characters
    # player
    playersName = nameDuelFont.render(f"{player.name}", 0, (0, 0, 0))
    playersLP = nameDuelFont.render(f"{npc.lp}", 0, (0, 0, 0))
    playersDeck = nameDuelFont.render(f"{len(player.deck)}", 0, (0, 0, 0), (255, 255, 255))
    playersGy = nameDuelFont.render(f"{len(player.gy)}", 0, (0, 0, 0), (255, 255, 255))
    # npc
    npcsName = nameDuelFont.render(f"{npc.name}", 0, (0, 0, 0))
    npcsLP = nameDuelFont.render(f"{npc.lp}", 0, (0, 0, 0))
    npcsDeck = nameDuelFont.render(f"{len(npc.deck)}", 0, (0, 0, 0), (255, 255, 255))
    npcsGy = nameDuelFont.render(f"{len(npc.gy)}", 0, (0, 0, 0), (255, 255, 255))



    # # drawing characters
    # npc
    DISPLAYSURF.blit(npcsName, (975,63))
    DISPLAYSURF.blit(npcsLP, (975,13))
    # DISPLAYSURF.blit(npcsDeck, (550,150))
    # DISPLAYSURF.blit(npcsGy, (550,300))
    # drawing npc's hand
    # NPCHAND = 500
    # for i in npc.hand:
    #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (NPCHAND, 0, 50, 50))
    #     NPCHAND += (1150-500)/len(npc.hand)
    printHand(DISPLAYSURF, npc, cartaOpciones)

    pygame.draw.rect(DISPLAYSURF, (255,255,0), gameField, 0)


    # player
    DISPLAYSURF.blit(playersName, (150,63))
    DISPLAYSURF.blit(playersLP, (151,13))
    # DISPLAYSURF.blit(playersDeck, (1100,600))
    # DISPLAYSURF.blit(playersGy, (1100,450))
    # drawing player's hand
    # PLAYERHAND = 500
    # for i in player.hand:
    #     pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (PLAYERHAND, 700, 50, 50))
    #     PLAYERHAND += (1150-500)/len(player.hand)
    printHand(DISPLAYSURF, player, cartaOpciones)
        



    # print("ya debería actualizarse ._.")
    pygame.display.update()
    clock.tick(10)