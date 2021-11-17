from typing import get_type_hints
import pygame, sys
from pygame.locals import *

class Character():
    def __init__(self, id, name, playerX, playerY, avatar):
        # general:
        self.id = id
        self.name = name
        self.avatar = avatar
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

class Npc(Character):
    def __init__(self, id, name, playerX, playerY, avatar, firstFrase, duelFrase):
        super().__init__(id, name, playerX, playerY, avatar)
        
        #  on Street:
        self.firstFrase = firstFrase
        self.duelFrase = duelFrase
        

class Player(Character):
    def __init__(self, id, name, playerX, playerY, avatar):
        super().__init__(id, name, playerX, playerY, avatar)