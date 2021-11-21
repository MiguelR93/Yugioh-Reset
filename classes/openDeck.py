import pygame, sys
from pygame.locals import *

import csv
import classes.card as card
import classes.rush.cardsEffects as cardsEffects
# # from script.rush import *

def openDeck():
    try:
        exampleFile = open('deck/lukeDeck.csv')
    except FileNotFoundError:
        exampleFile = open('../deck/lukeDeck.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    deckOrigin = list(exampleData[1:])
    deckResult = []

    for i in deckOrigin:
    #     if "Dragonic Pressure" in i[1]:
    #         newObject = cardsEffects.DragonicPressure(
    #             i[0],
    #             i[1],
    #             i[2],
    #             i[3],
    #             i[4],
    #             i[5]
    #         )
    #         deckResult.append(newObject)
        
        if "normal" in i[8]:
        # elif "normal" in i[8]:
            newObject = card.MonsterNormal(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
                i[8],
                i[9],
                pygame.image.load("images/cards/monster.png")
            )
            deckResult.append(newObject)

        elif "effect" in i[8]:
            newObject = card.MonsterEffect(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
                i[8],
                i[9],
                i[10],
                pygame.image.load("images/cards/monsterEff.png")
            )
            deckResult.append(newObject)
            
        # elif ("SPELL" in i[2]) or ("TRAP" in i[2]):
        #     newObject = card.SpellTrap(
        #         i[0],
        #         i[1],
        #         i[2],
        #         i[3],
        #         i[4],
        #         i[5]
        #     )
        #     deckResult.append(newObject)

            
        elif ("TRAP" in i[2]):
            newObject = card.SpellTrap(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                pygame.image.load("images/cards/trap.png")
            )
            deckResult.append(newObject)

            
        elif ("SPELL" in i[2]):
            newObject = card.SpellTrap(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                pygame.image.load("images/cards/spell.png")
            )
            deckResult.append(newObject)

    
    # print(deckResult)
    # for i in deckResult:
    #     print(vars(i), end=',\n')
        # print(i, end=',\n')

    return deckResult


if __name__ == '__main__':
    openDeck()