import pygame, sys
from pygame.locals import *

class Character():
    # general:
    def __init__(self, id, name, playerX, playerY, avatar):
        self.id = id
        self.name = name
        self.avatar = avatar
        self.playerX = playerX
        self.playerY = playerY
        

class Player(Character):
    def __init__(self, id, name, playerX, playerY, avatar):
        super().__init__(id, name, playerX, playerY, avatar)