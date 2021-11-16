import pygame, sys
from pygame.locals import *

kaiba = pygame.image.load("./images/characters/kaibaF01.png")

class Player():
    id = 1
    name = "Drakdio"
    avatar = pygame.image.load("./images/characters/kaibaF01.png")
    playerX = 600
    playerY = 400

    # def __init__(self) -> None:
    #     pass
    # def player():
    #     while True:
    #         pass