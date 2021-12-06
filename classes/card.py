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


            if (pygame.mouse.get_pressed()[2] == True) and (self.level <= 4):
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
                        self.placeOnGame = 'field'
                        if functionStatus[0] == 'normalSummon':
                            self.battlePosition = 'Attack'
                            self.facePosition = 'up'
                            if kindSummon == 'NormalLvl>4':
                                self.summonKind = ['Normal Summon', 'Tribute Summon']
                            else:
                                self.summonKind = 'Normal Summon'
                        elif functionStatus[0] == 'setSummon':
                            self.battlePosition = 'Defense'
                            self.summonKind = 'Set'
                            self.facePosition = 'down'
                        status = 'finished'
            if status == 'finished':
                break
        return 'finished'


    def tributes(self, tributes, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus):
        sacrifice = []
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

            if functionStatus[1] == '1Tributo':
                for i in self.owner.monstersZones():
                    if i[0] != None:
                        if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                            sacrifice.append(i)
            
            # 2 tributos:
            if functionStatus[1] == '2Tributo':
                if len(functionStatus) < 3: # recién añaidido
                    functionStatus.append(sacrifice)
                drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus)
                for i in self.owner.monstersZones():
                    if i[0] != None:
                        if i in sacrifice:
                            print(f"\n\n\nActualmente en sacrificio: {sacrifice}\n\n\n")
            # 1.1 puede retirarse el primero, en cuyo caso volver a 1
                            if (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                                sacrifice.remove(i)
                                print(f"\n\n\nActualmente en sacrificio con retiro: {sacrifice}\n\n\n")
            # 1. se elige el primero
            # 2. se elige el segundo
                        elif (myMouse[0] >= i[1].left) and (myMouse[0] <= i[1].left + i[1].width) and (myMouse[1]  >= i[1].top) and (myMouse[1] <= i[1].top + i[1].height) and (pygame.mouse.get_pressed()[0] == True):
                            sacrifice.append(i)
                            print(f"\n\n\nActualmente en sacrificio con adición: {sacrifice}\n\n\n")


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
                    if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'], 'NormalLvl>4') == 'finished':
                        status = 'finished'
                    if status == 'finished':
                        break


            if (self.level >= 7) and (self.owner.monstersInField() > 0):
                # 1. colorear potenciales tributos # esto lo hace también la siguiente función
                # 2. elegir tributos
                sacrifice = self.tributes(2, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', '2Tributo'])
                # 2.1 si se cancela, actualizar la imagen:
                if len(sacrifice) == 0:
                    break
                # 3. una vez lo tributos son elegidos enviarlos al gy
                elif len(sacrifice) == 2:
                    for i in sacrifice:
                        # print(f"\n\n\nTodo mi sacrificio: {i[0].name}\n\n\n")
                        self.owner.gy.append(i[0])
                        i[0] = None
                    drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, None) # aquí para actualizar que no hay monstruo sen campo, indispensable?
                # 4. poner el monstruo en campo
                    # invocar!
                    status = None
                    if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'], 'NormalLvl>4') == 'finished':
                        status = 'finished'
                    if status == 'finished':
                        break


    def setSummon(self, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones):
        print("Set Summon!")
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            myMouse = pygame.mouse.get_pos()
            print(myMouse)

            # 0. clic secundario para cancelar
            if pygame.mouse.get_pressed()[2] == True:
                print("Se cancela la S. S.")
                break

            if (self.level <= 4) and (self.owner.monstersInField() < 3):
                # 1. colorear zonas disponibles
                # drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'])
                # 2. elegir zona disponible

                # monsterZoneChosed = None
                status = None
                if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setSummon', 'zonasDisponibles'], 'SetlLvl<=4') == 'finished':
                    status = 'finished'
                if status == 'finished':
                    break

            
            if (self.level >= 5) and (self.level <= 6) and (self.owner.monstersInField() > 0):
                # 1. colorear potenciales tributos # esto lo hace también la siguiente función
                # 2. elegir tributos
                sacrifice = self.tributes(1, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setSummon', '1Tributo'])
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
                    if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setSummon', 'zonasDisponibles'], 'SetLvl!=4') == 'finished':
                        status = 'finished'
                    if status == 'finished':
                        break


            if (self.level >= 7) and (self.owner.monstersInField() > 0):
                # 1. colorear potenciales tributos # esto lo hace también la siguiente función
                # 2. elegir tributos
                sacrifice = self.tributes(2, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setSummon', '2Tributo'])
                # 2.1 si se cancela, actualizar la imagen:
                if len(sacrifice) == 0:
                    break
                # 3. una vez lo tributos son elegidos enviarlos al gy
                elif len(sacrifice) == 2:
                    for i in sacrifice:
                        # print(f"\n\n\nTodo mi sacrificio: {i[0].name}\n\n\n")
                        self.owner.gy.append(i[0])
                        i[0] = None
                    drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, None) # aquí para actualizar que no hay monstruo sen campo, indispensable?
                # 4. poner el monstruo en campo
                    # invocar!
                    status = None
                    if self.placeAMonster(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setSummon', 'zonasDisponibles'], 'SetLvl!=4') == 'finished':
                        status = 'finished'
                    if status == 'finished':
                        break



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
            
            # Set
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
            elif (self.cardType == 'TRAP') and (self.owner.cardsInSTZones() < 3):# falta evaluar que haya espacio
                # print(f"{self.name, self.level} can be set")
                self.optionSet[0] = positionY - 25
                positionY -= 25
                showOptions.append(self.optionSet)
        return showOptions


    def placeASTCard(self, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus, kindPlacingCard):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            myMouse = pygame.mouse.get_pos()
            print(f"\n\n\n\nPosción de mouse en placeASTCard: {myMouse}")
            drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, functionStatus)
            print("Ya salimos de dibujar y seguimos en placeASTCard")
            status = None


            if (pygame.mouse.get_pressed()[2] == True): # and ((kindPlacingCard == 'NormalLvl<=4') or (kindPlacingCard == 'SetLvl<=4')):
                print("Se cancela la activación/set de s/t")
                break
            

            for i in self.owner.sTZones():
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
                        self.placedThisTurn = True
                        self.placeOnGame = 'field'
                        # Set
                        if kindPlacingCard == 'ActiveST':
                            self.facePosition = 'up'
                            self.position = 'active'
                        elif kindPlacingCard == 'SetST':
                            self.facePosition = 'down'
                            self.position = 'set'
                            if self.cardType == 'SPELL':
                                self.canBeActivatedThisTurn = True
                            elif self.cardType == 'TRAP':
                                self.canBeActivatedThisTurn = False
                        status = 'finished'
            if status == 'finished':
                break
        return 'finished'


    def actSetST(self, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            myMouse = pygame.mouse.get_pos()
            print(myMouse)

            # 0. clic secundario para cancelar
            if pygame.mouse.get_pressed()[2] == True:
                print("Se cancela la activación/set de s/t")
                break

            # set
            if (self.icon != 'field') and (self.owner.sTInZones() < 3):
                # 1. colorear zonas disponibles
                # drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['normalSummon', 'zonasDisponibles'])
                drawing.drawingAll(myMouse, DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setST', 'zonasDisponibles'])
                # 2. elegir zona disponible

                # monsterZoneChosed = None
                status = None
                if self.placeASTCard(DISPLAYSURF, player, npc, currentlyPhase, cartaOpciones, ['setST', 'zonasDisponibles'], 'SetST') == 'finished':
                    status = 'finished'
                if status == 'finished':
                    break