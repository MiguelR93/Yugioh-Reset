import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
# import script.duel as duel 
from script import duel, drawing

pygame.init()

def mainPhase(DISPLAYSURF, player, npc):
    print("Inicio de la Main Phase >>>:)")
    cartaOpciones = None
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
        
        # cartaOpciones = None
        for i in player.hand: # Detecta sobre qué carta está el mouse
            # if (myMouse[0] >= i.cardX) and (myMouse[0] <= i.cardX + i.cardWidth) and (myMouse[1]  >= i.cardY) and (myMouse[1] <= i.cardY + i.cardHeight):
            if (myMouse[0] >= i.cardX) and (myMouse[0] <= i.cardX + i.cardWidth) and (myMouse[1]  >= i.cardY) and (myMouse[1] <= i.cardY + i.cardHeight) and (pygame.mouse.get_pressed()[0] == True) and (cartaOpciones == i):
                cartaOpciones = None
            elif (pygame.mouse.get_pressed()[2] == True):
                cartaOpciones = None
            elif (myMouse[0] >= i.cardX) and (myMouse[0] <= i.cardX + i.cardWidth) and (myMouse[1]  >= i.cardY) and (myMouse[1] <= i.cardY + i.cardHeight) and (pygame.mouse.get_pressed()[0] == True):
                # print(i.name)
                cartaOpciones = i

        if cartaOpciones != None: # esta función permite utilizar el comportamiento 'options' del objeto Card
            cartaOpciones.options()
            # detectando si estamos haciendo clic en una opción de una carta
        
        # if (cartaOpciones != None) and (type(cartaOpciones.options()) == None):
        # if (cartaOpciones != None) and (len(cartaOpciones.optionsAble) != 0):
            # for i in cartaOpciones.optionsAble:
        if cartaOpciones != None:
            for i in cartaOpciones.options():
                # print(f"{i}: es la opción :V")
                if (myMouse[0] >= cartaOpciones.cardX) and (myMouse[0] <= cartaOpciones.cardX + cartaOpciones.cardWidth) and (myMouse[1]  >= i[0]) and (myMouse[1] <= i[0] + 25) and (pygame.mouse.get_pressed()[0] == True):
                    print("No me presiones >:V", i[2])
                    # Aplicando las opciones
                    if i[2] == 'Normal S.':
                        print("En efecto, normal summon")
                        cartaOpciones.normalSummon(myMouse, DISPLAYSURF, player, npc, "MainPhase", cartaOpciones)

        # if cartaOpciones != None: # debe desplegarse una serie de opciones y cada opción debe pasar por el bucle: lo de abajo debería ser un bucle :V
        #     if (myMouse[0] >= cartaOpciones.cardX) and (myMouse[0] <= cartaOpciones.cardX + cartaOpciones.cardWidth) and (myMouse[1]  >= cartaOpciones.cardY) and (myMouse[1] <= cartaOpciones.cardY + cartaOpciones.cardHeight) and (pygame.mouse.get_pressed()[0] == True) and (cartaOpciones == i):
        #         pass

        drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, "MainPhase", cartaOpciones)

        # detectar la posición del mouse sobre una carta