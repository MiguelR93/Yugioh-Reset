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
            self.deck[0].placeOnGame = "hand" # experimento
            self.hand.append(self.deck[0]) # añade la carta del deck a la mano
            self.deck.remove(self.deck[0]) # quita del deck la carta añadida a la mano
            
            self.orderCardsInHand() # new!


    def orderCardsInHand(self):
        CHARACTERHAND = 500
        for i in self.hand:
            # pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (CHARACTERHAND, 700, 82, 118), 0)
            # DISPLAYSURF.blit(i.illustration, (CHARACTERHAND, 700))
            i.cardX, i.cardY = CHARACTERHAND, self.handY
            # i.makeARect() # momentaneamente silenciado hasta hallarle necesidad
            CHARACTERHAND += (1150-500)/len(self.hand)


    def monstersInField(self):
        monsters = [
            self.rigthMz, 
            self.centerMz, 
            self.leftMz
        ]
        monstersCounter = 0
        for i in monsters:
            if i != None:
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
            if i != None:
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