class Card():

    def __init__(self, id, name, cardType, text):
        self.id = id
        self.name = name
        self.cardType = cardType
        self.text = text


class CardEffect():
    def __init__(self, effect):
        self.effect = effect


class Monster(Card):
    
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text):
        super().__init__(id, name, cardType, text)
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


class MonsterNormal(Monster):

    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text)


class MonsterEffect(Monster):
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text)
        self.effect = effect


class SpellTrap(Card):
    icon = str
    effect = CardEffect("")

    def __init__(self, id, name, cardType, icon, effect, text):
        super().__init__(id, name, cardType, text)
        self.icon = icon
        self.effect = effect

        # # nuevos atributos: -------
        self.position = None # [active, set]
        self.placedThisTurn = None
        self.canBeActivatedThisTurn = None