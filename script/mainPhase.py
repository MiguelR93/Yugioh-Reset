import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
# import script.duel as duel 
from script import duel, drawing

pygame.init()

def mainPhase(DISPLAYSURF, player, npc):
    duel.cartaOpciones
    print("Inicio de la Main Phase >>>:)")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        myMouse = pygame.mouse.get_pos()
        print(myMouse)

        # detectando que elija BP
        if (myMouse[0] >= 975) and (myMouse[0] <= 975 + 175) and (myMouse[1]  >= 425) and (myMouse[1] <= 425 + 75):
            print("Sobre BP")
            if pygame.mouse.get_pressed()[0] == True:
                # break # ir a BP
                return "BattlePhase"
        if (myMouse[0] >= 975) and (myMouse[0] <= 975 + 175) and (myMouse[1]  >= 525) and (myMouse[1] <= 525 + 75):
            print("Sobre EP")
            if pygame.mouse.get_pressed()[0] == True:
                # break # ir a BP
                return "EndPhase"
        

        for i in player.hand: # Detecta sobre qué carta está el mouse
            if (myMouse[0] >= i.cardX) and (myMouse[0] <= i.cardX + i.cardWidth) and (myMouse[1]  >= i.cardY) and (myMouse[1] <= i.cardY + i.cardHeight) and (pygame.mouse.get_pressed()[0] == True) and (duel.cartaOpciones == i):
                duel.cartaOpciones = None
            elif (pygame.mouse.get_pressed()[2] == True):
                duel.cartaOpciones = None
            elif (myMouse[0] >= i.cardX) and (myMouse[0] <= i.cardX + i.cardWidth) and (myMouse[1]  >= i.cardY) and (myMouse[1] <= i.cardY + i.cardHeight) and (pygame.mouse.get_pressed()[0] == True):
                # print(i.name)
                duel.cartaOpciones = i

        if duel.cartaOpciones != None: # esta función permite utilizar el comportamiento 'options' del objeto Card
            duel.cartaOpciones.options()
            # detectando si estamos haciendo clic en una opción de una carta
        

        if duel.cartaOpciones != None:
            for i in duel.cartaOpciones.options():
                try:
                    print(f"{i}: es la opción :V")
                    print(duel.cartaOpciones)
                    if (myMouse[0] >= duel.cartaOpciones.cardX) and (myMouse[0] <= duel.cartaOpciones.cardX + duel.cartaOpciones.cardWidth) and (myMouse[1]  >= i[0]) and (myMouse[1] <= i[0] + 25) and (pygame.mouse.get_pressed()[0] == True):
                        print("No me presiones >:V", i[2])
                        # Aplicando las opciones
                        if i[2] == 'Normal S.':
                            print("En efecto, normal summon")
                            duel.cartaOpciones.normalSummon(DISPLAYSURF, player, npc, "MainPhase", duel.cartaOpciones)
                            print(player.hand)
                            print(f"\n\nAhora duel.cartaOpciones es: {duel.cartaOpciones}")
                except AttributeError as e:
                    print(e)
                    pass


        drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, "MainPhase", duel.cartaOpciones, None)