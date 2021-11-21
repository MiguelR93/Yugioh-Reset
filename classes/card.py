class Card():

    def __init__(self, id, name, cardType, text,
        illustration):
        self.id = id
        self.name = name
        self.cardType = cardType
        self.text = text
        self.illustration = illustration


class CardEffect():
    def __init__(self, effect):
        self.effect = effect


class Monster(Card):
    
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text,
        illustration):
        super().__init__(id, name, cardType, text,
        illustration)
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
    
    def normalSummon(self):
        print("Normal Summon!")


class MonsterNormal(Monster):

    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text,
    illustration):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text,
        illustration)


class MonsterEffect(Monster):
    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, illustration)
        self.effect = effect


class SpellTrap(Card):
    icon = str
    effect = CardEffect("")

    def __init__(self, id, name, cardType, icon, effect, text, illustration):
        super().__init__(id, name, cardType, text, illustration)
        self.icon = icon
        self.effect = effect

        # # nuevos atributos: -------
        self.position = None # [active, set]
        self.placedThisTurn = None
        self.canBeActivatedThisTurn = None