import pygame, sys
from pygame.locals import *

kaiba = pygame.image.load("./images/characters/kaibaF01.png")

class Player():
    id = 1
    name = "Drakdio"
    avatar = pygame.image.load("./images/characters/kaibaF01.png")
    playerX = 600
    playerY = 400
    speed = 5

    def __init__(self) -> None:
        pass

    def movement():
        print("movimiento de Kaiba")
        # while True:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             print("Izquierda, player!")
        #             if self.playerX <= 0:
        #                 self.playerX += 0
        #             else:    
        #                 self.playerX -= self.speed
                # elif event.key == pygame.K_RIGHT:
                #     print("Derecha, player!")
        #             if self.playerX >800:
        #                 self.playerX += 0
        #             else: 
        #                 self.playerX += self.speed