import pygame, sys
from pygame.locals import *


class Player():

    def __init__(self, id, name, playerX, playerY, avatar):
        self.id = id
        self.name = name
        self.avatar = avatar
        self.playerX = playerX
        self.playerY = playerY
        self.speed = 5