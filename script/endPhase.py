import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
# import script.duel as duel 
from script import duel, drawing

pygame.init()

def endPhase(DISPLAYSURF, player, npc):
    print("Inicio de la End Phase >>>:)")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        myMouse = pygame.mouse.get_pos()
        print(myMouse)

        break