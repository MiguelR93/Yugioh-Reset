import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
from script import duel

pygame.init()
# main values
clock = pygame.time.Clock()
defenseFD = pygame.image.load("images/cards/1Face-Down.png")

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
        if (character == cartaOpciones.owner): #and isinstance(cartaOpciones, card.Monster) and (cartaOpciones.placeOnGame == "hand"):
            print(character.monstersInField(), cartaOpciones.owner.name)
            for i in cartaOpciones.options():
                # print(f"Esto está en options: {i}")
                pygame.draw.rect(DISPLAYSURF, i[1], (cartaOpciones.cardX, i[0], cartaOpciones.cardWidth, 25), 0)
                # optionsCardText
                optionCardText = cardOptionFont.render(f"{i[2]}", 0, (0, 0, 0))
                DISPLAYSURF.blit(optionCardText, (cartaOpciones.cardX, i[0]))


def drawingAll(mousePosition,DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus):
    print('Drawing All 2')
    DISPLAYSURF.fill((255, 255, 255))
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


    phases = (drawPhaseRect, mainPhaseRect, battlePhaseRect, endPhaseRect,)

    for i in phases: # phaseFont
        if currentlyPhase == i[1]:
            pygame.draw.rect(DISPLAYSURF, (255,0,0), i[0])
            phaseText = phaseFont.render(i[1], 0, (0,0, 255))
            DISPLAYSURF.blit(phaseText, (i[0].left,i[0].top+25))
        else:
            pygame.draw.rect(DISPLAYSURF, (0,0,0), i[0])
            phaseText = phaseFont.render(i[1], 0, (255, 255, 255))
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
    printHand(DISPLAYSURF, npc, cartaOpciones)

    pygame.draw.rect(DISPLAYSURF, (255,255,0), gameField, 0)


    # dibujando campo
    pygame.draw.rect(DISPLAYSURF, (255,255,0), gameField, 0)
    for i in player.monstersZones():
        if i[0] != None:
            print(f"Esto es el i que dibuja: {i}")
            if i[0].battlePosition == 'Attack':
                pygame.draw.rect(DISPLAYSURF, (0, 5, 0), (i[0].cardX, i[0].cardY, i[0].cardWidth, i[0].cardHeight), 0)
                DISPLAYSURF.blit(i[0].illustration, (i[0].cardX, i[0].cardY))
            elif (i[0].battlePosition == 'Defense') and (i[0].facePosition == 'down'):
                pygame.draw.rect(DISPLAYSURF, (0, 5, 0), (i[0].cardX, i[0].cardY, i[0].cardHeight, i[0].cardWidth), 0)
                DISPLAYSURF.blit(defenseFD, (i[0].cardX, i[0].cardY))


    # player
    DISPLAYSURF.blit(playersName, (150,63))
    DISPLAYSURF.blit(playersLP, (151,13))
    printHand(DISPLAYSURF, player, cartaOpciones)
        

    if (functionStatus!= None):
        if (functionStatus[0] == 'normalSummon') or (functionStatus[0] == 'setSummon'):
            if (functionStatus[1] == 'zonasDisponibles'):
                print(f"Zonas de monstruo{cartaOpciones.owner.monstersZones()}")
                for i in cartaOpciones.owner.monstersZones():
                    print(i)
                    if i[0] == None:
                        pygame.draw.rect(DISPLAYSURF, (0,0,0), i[1], 5)
            elif (functionStatus[1] == '1Tributo') or (functionStatus[1] == '2Tributo'):
                for i in cartaOpciones.owner.monstersZones():
                    if i[0] != None: # colorea los monstruos sacrificables
                        pygame.draw.rect(DISPLAYSURF, (255,0,0), i[1], 5)
                if len(functionStatus) == 3:
                    for i in functionStatus[2]: # colorea los sacrificios
                        pygame.draw.rect(DISPLAYSURF, (0,0,255), i[1], 5)


    pygame.display.update()
    clock.tick(15)