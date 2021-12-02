import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
# import script.duel as duel 
from script import duel, drawing

pygame.init()

def battlePhase(DISPLAYSURF, player, npc):
    print("Inicio de la Battle Phase >>>:)")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        myMouse = pygame.mouse.get_pos()
        print(myMouse)
        
        if (myMouse[0] >= 975) and (myMouse[0] <= 975 + 175) and (myMouse[1]  >= 525) and (myMouse[1] <= 525 + 75):
            print("Sobre EP")
            if pygame.mouse.get_pressed()[0] == True:
                # return "EndPhase"
                break
        
        drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, "BattlePhase", None, None)