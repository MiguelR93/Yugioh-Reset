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
        self.facePosition = None
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


    def placeAMonster(self, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus, kindSummon):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            myMouse = pygame.mouse.get_pos()
            drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus)
            status = None


            if (pygame.mouse.get_pressed()[2] == True) and (kindSummon == 'NormalLvl<=4'):
                print("Se cancela la N. S.")
                break

            for i in self.owner.monstersZones():
                if i[0] == None: # solamente se mostrarán las zonas disponibles
                    # print(f"Zonas disponibles: {i}")
                    if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True): # 2.2 Si zona está disponible ir a 3
                        # print("Esta zona está disponible!")
                        # print(self.name)
                        # 3. invocar al monstruo en la zona elegida:
                        i[0] = self # agrega al monstruo al campo
                        self.owner.hand.remove(self) # quita al monstruo de la mano
                        self.cardX, self.cardY = i[1].left, i[1].top # cambia las coordenadas del monstruo
                        duel.cartaOpciones = None # vuelve a estar en blanco
                        self.owner.orderCardsInHand() # ordena las cartas en mano
                        self.summonedThisTurn = True # atributos que deben cambiar al invocarse el monsturo
                        self.canChangeItsPosition = False # atributos que deben cambiar al invocarse el monsturo
                        self.battlePosition = 'Attack'
                        self.summonKind = 'Normal Summon'
                        self.placeOnGame = 'field'
                        self.facePosition = 'up'
                        status = 'finished'
            if status == 'finished':
                break
        return 'finished'


    def tributes(self, tributes, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            myMouse = pygame.mouse.get_pos()
            drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus)

            if pygame.mouse.get_pressed()[2] == True:
                print("Se cancela la N. S.")
                break

            # status = None

            sacrifice = []
            for i in self.owner.monstersZones():
                if i[0] != None:
                    if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                        sacrifice.append(i)
            
            if len(sacrifice) == tributes:
                break


            # if status == 'finished':
            #     break
        # print(f"Esto es lo que vas a sacrificar: {sacrifice}")
        return sacrifice


    # def normalSummon(self):
    def normalSummon(self, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones):
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
                # drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'])
                # 2. elegir zona disponible

                # monsterZoneChosed = None
                status = None
                if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'], 'NormalLvl<=4') == 'finished':
                    status = 'finished'
                if status == 'finished':
                    break

            
            if (self.level >= 5) and (self.level <= 6) and (self.owner.monstersInField() > 0):
                # 1. colorear potenciales tributos # esto lo hace también la siguiente función
                # 2. elegir tributos
                sacrifice = self.tributes(1, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', '1Tributo'])
                # 2.1 si se cancela, actualizar la imagen:
                if len(sacrifice) == 0:
                    break
                # 3. una vez lo tributos son elegidos enviarlos al gy
                elif len(sacrifice) == 1:
                    for i in sacrifice:
                        # print(f"\n\n\nTodo mi sacrificio: {i[0].name}\n\n\n")
                        self.owner.gy.append(i[0])
                        i[0] = None
                    drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, None) # aquí para actualizar que no hay monstruo sen campo, indispensable?
                # 4. poner el monstruo en campo
                    # invocar!
                    status = None
                    if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'], 'NormalLvl!=4') == 'finished':
                        status = 'finished'
                    if status == 'finished':
                        break

                # drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', '1Tributo'])
                # sacrifice = []
                # for i in self.owner.monstersZones():
                #     if i[0] != None:
                #         if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                #             sacrifice.append(i)
                # status = None
                # continueTributeSummon = None
                # if len(sacrifice) == 1:
                #     # print(f"Tributar: {sacrifice}")
                #     for i in sacrifice:
                #         self.owner.gy.append(i[0]) # cambiar sus datos!
                #         i[0] = None
                #         print(f"\n\nEn el campo: {i}")
                #         drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, None) # con esto ya se remueve el monstruo del campo
                #         continueTributeSummon = True
                    
                # if continueTributeSummon == True:
                #     drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'])

                #     for i in self.owner.monstersZones():
                #         if i[0] == None:
                #             print(f"Zonas disponibles: {i}")
                #             if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                #                 print("Esta zona está disponible!")
                #                 print(self.name)
                #                 self.owner.hand.remove(self)
                #                 i[0] = self
                #                 self.cardX, self.cardY = i[1].left, i[1].top
                #                 duel.cartaOpciones = None
                #                 self.owner.orderCardsInHand()
                #                 self.summonedThisTurn = True
                #                 self.canChangeItsPosition = False 
                #                 status = 'finished'
                # if status == 'finished':
                #     break

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