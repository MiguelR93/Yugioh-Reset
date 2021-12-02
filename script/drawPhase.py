import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
# import script.duel as duel 
from script import duel, drawing

pygame.init()

def drawPhase(DISPLAYSURF, player, npc, character):
    print("Inicio de la Draw Phase >>>:)")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        myMouse = pygame.mouse.get_pos()
        print(myMouse)

        print(character.hand) #solo para comprobar que shuffle deck funciona :)
        character.drawPhase()
        print(character.hand) #solo para comprobar que shuffle deck funciona :)
        drawing.drawingAll(myMouse,DISPLAYSURF, player, npc, "DrawPhase", None, None)

        # drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, "DrawPhase", None)
        break # al final de todo