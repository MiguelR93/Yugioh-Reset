import pygame, sys
from pygame.locals import *

kaiba = pygame.image.load("./images/characters/kaibaF01.png")

class Player():
    # id = 1
    # name = "Drakdio"
    # avatar = pygame.image.load("./images/characters/kaibaF01.png")
    # playerX = 600
    # playerY = 400
    # speed = 5

    # def __init__(self, playerX, playerY) -> None:
    #     self.playerX = playerX
    #     self.playerY = playerY

    def __init__(self, id, name, playerX, playerY, avatar):
        self.id = id
        self.name = name
        self.avatar = avatar
        self.playerX = playerX
        self.playerY = playerY
        self.speed = 5

    def movimiento(self):
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


        # while True:
        #     for event in pygame.event.get():
        #         if event.type == QUIT:
        #             pygame.quit()
        #             sys.exit()

        #         if event.type == pygame.KEYDOWN:
        #             print(self.playerX)
        #             if event.key == pygame.K_LEFT:
        #                 print("Izquierda, player!")
        #                 if self.playerX <= 0:
        #                     self.playerX += 0
        #                 else:    
        #                     self.playerX -= self.speed
        #             elif event.key == pygame.K_RIGHT:
        #                 print("Derecha, player!")
        #                 if self.playerX >= 800:
        #                     self.playerX += 0
        #                 else: 
        #                     self.playerX += self.speed
        #             else:
        #                 pass