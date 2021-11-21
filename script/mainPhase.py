import pygame, sys, time
from pygame.locals import *
import classes.background as background
import classes.card as card
import script.duel as duel 

pygame.init()

def mainPhase(DISPLAYSURF, player, npc):
    print("Inicio de la Main Phase >>>:)")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        myMouse2 = pygame.mouse.get_pos()
        print(myMouse2)

        # detectar la posición del mouse sobre una carta