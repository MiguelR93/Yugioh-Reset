import pygame, sys, random
from pygame.locals import *
import script.duel as duel

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
        self.speedX = 75
        self.speedY = 80

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
        self.handY = None # new!


    def drawPhase(self):
        if self.cardsInHand() >= 5:
            self.drawACard()
        else:
            while (len(self.hand) < 5) and (duel.victory() == True):
                self.drawACard()


    def cardsInHand(self):
        return len(self.hand)


    def drawACard(self):
        if len(self.deck) == 0:
            print("No hay cartas en el deck")
            self.victory = False
        else:
            # self.deck[0].placeOnGame = "hand" # experimento
            self.hand.append(self.deck[0]) # añade la carta del deck a la mano
            self.deck.remove(self.deck[0]) # quita del deck la carta añadida a la mano
            self.hand[-1].placeOnGame = "hand" # experimento
            
            self.orderCardsInHand() # new!


    def orderCardsInHand(self):
        CHARACTERHAND = 500
        for i in self.hand:
            # pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, 700, 82, 118), 0)
            # DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, 700))
            i.cardX, i.cardY = CHARACTERHAND, self.handY
            # i.makeARect() # momentaneamente silenciado hasta hallarle necesidad
            CHARACTERHAND += (1150-500)/len(self.hand)

    def monstersZones(self):
        monsters = [
            self.rigthMz, 
            self.centerMz, 
            self.leftMz
        ]
        return monsters

    def sTZones(self):
        stZones = [
            self.rigthSTZ, 
            self.centerSTZ, 
            self.leftSTZ
        ]
        return stZones
    
    def sTInZones(self):
        st = [
            self.rigthSTZ, 
            self.centerSTZ, 
            self.leftSTZ
        ]
        sTCounter = 0
        for i in st:
            if i[0] != None:
                sTCounter += 1
        return sTCounter

    def monstersInField(self):
        monsters = [
            self.rigthMz, 
            self.centerMz, 
            self.leftMz
        ]
        monstersCounter = 0
        for i in monsters:
            if i[0] != None:
                monstersCounter += 1
        return monstersCounter
    
    def cardsInSTZones(self):
        sTZones = [
            self.rigthSTZ,
            self.centerSTZ,
            self.leftSTZ
        ]
        stCounter = 0
        for i in sTZones:
            if i[0] != None:
                stCounter += 1
        return stCounter

    # def printHand(DISPLAYSURF, character, characterHandY): # lo traje para incluir su bloque de código a la función drawACard
    #     CHARACTERHAND = 500
    #     for i in character.hand:
    #         pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, characterHandY, 82, 118), 0)
    #         DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, characterHandY))
    #         i.cardX, i.cardY = CHARACTERHAND, characterHandY
    #         i.makeARect()
    #         CHARACTERHAND += (1150-500)/len(character.hand)

    def shuffleDeck(self):
        random.shuffle(self.deck)


class Npc(Character):
    def __init__(self, id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack, firstFrase, duelFrase):
        super().__init__(id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack)
        
        #  on Street:
        self.firstFrase = firstFrase
        self.duelFrase = duelFrase
        self.handY = 100

        # gameZone:
        self.fieldSCZ = [None, Rect(800, 325, 125, 125)]
        self.leftMz = [None, Rect(675, 325, 125, 125)]
        self.centerMz = [None, Rect(550, 325, 125, 125)]
        self.rigthMz = [None, Rect(425, 325, 125, 125)]
        self.leftSTZ = [None, Rect(675, 200, 125, 125)]
        self.centerSTZ = [None, Rect(550, 200, 125, 125)]
        self.rigthSTZ = [None, Rect(425, 200, 125, 125)]

    # def drawACard(self):
    #     if len(self.deck) == 0:
    #         print("No hay cartas en el deck")
    #         self.victory = False
    #     else:
    #         self.deck[0].placeOnGame = "hand" # experimento
    #         self.hand.append(self.deck[0]) # añade la carta del deck a la mano
    #         self.deck.remove(self.deck[0]) # quita del deck la carta añadida a la mano


    # def orderCardsInHand(self):
    #     CHARACTERHAND = 500
    #     for i in self.hand:
    #         # pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, 700, 82, 118), 0)
    #         # DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, 700))
    #         i.cardX, i.cardY = CHARACTERHAND, 700
    #         i.makeARect()
    #         CHARACTERHAND += (1150-500)/len(self.hand)
        

class Player(Character):
    def __init__(self, id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack):
        super().__init__(id, name, playerX, playerY, avatarFront, avatarRight, avatarLeft, avatarBack)
        self.handY = 700

        # gameZone:
        self.fieldSCZ = [None, Rect(300, 450, 125, 125)]
        self.leftMz = [None, Rect(425, 450, 125, 125)]
        self.centerMz = [None, Rect(550, 450, 125, 125)]
        self.rigthMz = [None, Rect(675, 450, 125, 125)]
        self.leftSTZ = [None, Rect(425, 575, 125, 125)]
        self.centerSTZ = [None, Rect(550, 575, 125, 125)]
        self.rigthSTZ = [None, Rect(675, 575, 125, 125)]
