import pygame, sys, time
from pygame.locals import *
from script import drawing, duel

pygame.init()

class Card():

    def __init__(self, id, name, cardType, text, illustration, owner):
        self.id = id
        self.name = name
        self.cardType = cardType
        self.text = text
        self.illustration = illustration
        self.placeOnGame = None # experimento
        self.cardX = None
        self.cardY = None
        self.cardWidth = 81
        self.cardHeight = 118
        self.rectangulo = None
        self.owner = owner
        # show options ----------
        # self.optionsAble = []
        self.cardOptionsHeight = 25 # experimento
        self.optionRead = [None, (100, 125, 0), 'Leer']
        self.optionSet = [None, (255, 125, 100), 'Set']
        self.optionActiveEff = [None, (255, 100, 0), 'Activar']
    
    # def makeARect(self): # momentaneamente silenciado hasta hallarlo necesario
    #     self.rectangulo = pygame.Rect(self.cardX, self.cardY, 81, 118)

    
    # def options(self):
    #     # print("Aquí!")
    #     print(f"Estás en {self.name}")

class CardEffect():
    def __init__(self, effect):
        self.effect = effect


class Monster(Card):
    
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, illustration, owner):
        super().__init__(id, name, cardType, text, illustration, owner)
        self.attribute = attribute
        self.level = int(level)
        self.typeMonster = typeMonster
        self.frontier = frontier

        self.attack = int(attack)
        self.defense = int(defense)
        self.currentAtk = self.attack
        self.currentDef = self.defense
        
        # # nuevos atributos: -------
        self.battlePosition = None # [attack, defense]
        self.summonKind = None # [normalSummon, set, flipSummon, tributeSummon, specialSummon]
        self.summonedThisTurn = None
        self.canAttackThisTurn = 1
        self.canChangeItsPosition = None

        # show options ----------
        self.optionSummon = [None, (255, 125, 255), 'Normal S.']
        self.optionAttack = [None, (255, 125, 125), 'Atacar']
        self.optionFlipSummon = [None, (0, 125, 0), 'Flip Summon']
        self.optionChangePosition = [None, (255, 0, 0), 'Cambiar pos.']
    
    def options(self):
        showOptions = []
        positionY = self.cardY
        print("Read this card")
        self.optionRead[0] = positionY - 25
        positionY -= 25
        showOptions.append(self.optionRead)
        
        
        if self.placeOnGame == "hand":
            # Normal summon
            if (self.level <= 4) and (self.owner.monstersInField() < 3):
                print(f"{self.name, self.level} can be normal summoned")
                self.optionSummon[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSummon)
            elif ((self.level == 5) or (self.level == 6)) and (self.owner.monstersInField() > 0):
                print(f"{self.name, self.level} can be normal summoned")
                self.optionSummon[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSummon)
            elif (self.level >= 7) and (self.owner.monstersInField() > 1):
                print(f"{self.name, self.level} can be normal summoned")
                self.optionSummon[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSummon)
            # set
            if (self.level <= 4) and (self.owner.monstersInField() < 3):
                print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
            elif ((self.level == 5) or (self.level == 6)) and (self.owner.monstersInField() > 0):
                print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
            elif (self.level >= 7) and (self.owner.monstersInField() > 1):
                print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
        # self.optionsAble = showOptions # esto debería reemplazar el return siguiente, ojo, self.optionsAble está desactivado
        return showOptions


    # def normalSummon(self):
    def normalSummon(self,DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones):
        print("Normal Summon!")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            myMouse = pygame.mouse.get_pos()
            print(myMouse)

            # 0. clic secundario para cancelar
            if pygame.mouse.get_pressed()[2] == True:
                print("Se cancela la N. S.")
                break

            if (self.level <= 4) and (self.owner.monstersInField() < 3):
                # 1. colorear zonas disponibles
                drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'])
                # 2. elegir zona disponible

                # monsterZoneChosed = None
                status = None
                for i in self.owner.monstersZones():
                    if i[0] == None:
                        print(f"Zonas disponibles: {i}")
                        if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                            print("Esta zona está disponible!")
                            print(self.name)
                            self.owner.hand.remove(self)
                            i[0] = self
                            self.cardX, self.cardY = i[1].left, i[1].top
                            duel.cartaOpciones = None
                            self.owner.orderCardsInHand()
                            self.summonedThisTurn = True
                            self.canChangeItsPosition = False
                            status = 'finished'
                            # break # volverá?
                if status == 'finished':
                    break
                ## 2.1 Si zona NO está disponible, volver al paso 2
                ## 2.2 Si zona está disponible ir a 3
                # 3. invocar al monstruo en la zona elegida
                # 4. FIN
            if (self.level >= 5) and (self.level <= 6) and (self.owner.monstersInField() > 0):
                drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', '1Tributo'])


class MonsterNormal(Monster):

    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, illustration, owner):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text,
        illustration, owner)


class MonsterEffect(Monster):
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration, owner):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, illustration, owner)
        self.effect = effect


class SpellTrap(Card):
    icon = str
    effect = CardEffect("")

    def __init__(self, id, name, cardType, icon, effect, text, illustration, owner):
        super().__init__(id, name, cardType, text, illustration, owner)
        self.icon = icon
        self.effect = effect

        # # nuevos atributos: -------
        self.position = None # [active, set]
        self.placedThisTurn = None
        self.canBeActivatedThisTurn = None



    def options(self):
        showOptions = []
        positionY = self.cardY
        print("Read this card")
        self.optionRead[0] = positionY - 25
        positionY -= 25
        showOptions.append(self.optionRead)

        if self.placeOnGame == "hand":
            # Activar
            if (self.cardType == 'SPELL')and (self.owner.cardsInSTZones() < 3) and (self.icon == 'normal') : # falta evaluar que haya espacio
                print('Puedes activar')
                # print(f"{self.name, self.level} can be normal summoned")
                self.optionActiveEff[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionActiveEff)
            # elif self.cardType == 'TRAP':
            #     # print('NO Puedes activar')
            #     pass
            
            # Set
            # if (self.cardType == 'SPELL') and (self.owner.cardsInSTZones() < 3) and (self.icon == 'normal') :# falta evaluar que haya espacio
                # print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
            elif (self.cardType == 'TRAP') and (self.owner.cardsInSTZones() < 3):# falta evaluar que haya espacio
                # print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
        return showOptions