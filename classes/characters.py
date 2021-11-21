import pygame, sys
from pygame.locals import *

class Character():
    def __init__(self, id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack):
        # general:
        self.id = id
        self.name = name
        self.avatarFront = avatarFront
        self.avatarRight = avatarRight
        self.avatarLeft = avatarLeft
        self.avatarBack = avatarBack
        self.playerX = playerX
        self.playerY = playerY

        # on duel:
        self.oponent = None
        self.lp = 8000
        self.victory = None

        # gameZone:
        self.deck = []
        self.hand = []
        self.gy = []
        self.checkCards = []
        self.rigthMz = None
        self.centerMz = None
        self.leftMz = None
        self.fieldSCZ = None
        self.rigthSTZ = None
        self.centerSTZ = None
        self.leftSTZ = None

    def drawPhase(self):
        if self.cardsInHand() >= 5:
            self.drawACard()
        else:
            while (len(self.hand) < 5) and (self.victory == True) and (self.oponent.victory == True): # el anterior era: while (len(self.hand) < 5) and (duel.victory() == True):
                self.drawACard()


    def cardsInHand(self):
        return len(self.hand)


    def drawACard(self):
        if len(self.deck) == 0:
            print("No hay cartas en el deck")
            self.victory = False
        else:
            self.hand.append(self.deck[0]) # añade la carta del deck a la mano
            self.deck.remove(self.deck[0]) # quita del deck la carta añadida a la mano


class Npc(Character):
    def __init__(self, id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack, firstFrase, duelFrase):
        super().__init__(id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack)
        
        #  on Street:
        self.firstFrase = firstFrase
        self.duelFrase = duelFrase
        

class Player(Character):
    def __init__(self, id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack):
        super().__init__(id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack)