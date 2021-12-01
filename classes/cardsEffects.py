import classes.card as card
import classes.listCardEff as listCardEff

class DragonicPressure(card.SpellTrap):
    # NOTA: LA CARTA SE ENVÍA AL GY INCLUSO SI EL EFF NO SE RESUELVE Y ADEMÁS CUENTA COMO ESTUVIERA EN LA MANO
    # NOTA: LA CARTA DEBE PASAR DE LA MANO AL CAMPO Y LUEGO ACTIVAR SU EFF, DESPUÉS SER ENVIADA AL GY
    # NOTA: SUMMONLOOP FUNCIONA CON CARTAS DE LA MANO, CAMBIAR ESO
    def __init__(self, id, name, cardType, icon, effect, text, illustration, owner):
        super().__init__(id, name, cardType, icon, effect, text, illustration, owner)

    # def cardEffect(self, playerTurn):
    #     # TEXT: 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'

    #     # 1. CONDICIÓN: A) Debe evaluar si hay monstruos en el campo; B) Debe evaluar si el jugador tiene al menos 3 dragones en mano; RESULTADO: Debe destruir los monstruos del campo (si es que hay alguno) y contar si destruyó alguno
    #     # 2 CONDICIÓN: A) haber destruido al menos un monstruo con este efecto; B) ver si hay algún monstruo de nvl <= 4 en GY del jugador; RESULTADO: el jugador elige un monstruo nvl <= 4 de su GY y lo invoca en posición de defensa boca arriba

    #     print("Esta carta destruye a todos los monstruos en el campo, pero requiere que haya al menos uno en este y 3 dragones en tu mano para activarla")
    #     # listCardEff.counterMonsterInField(playerTurn)
    #     # listCardEff.counterDragonInHand(playerTurn)
    #     if (listCardEff.counterMonsterInField(playerTurn) > 0) and (listCardEff.counterDragonInHand(playerTurn) >= 3):
    #         listCardEff.sendDragonInHandToGY(playerTurn)
    #         # destroyAllMonsterInField()
    #     #     listCardEff.counterMonsterDestroyed(playerTurn)
    #     # else:
    #     #     print("No puedes activar esta carta!")
    #     # if (listCardEff.counterMonsterDestroyed(playerTurn) > 0) and (listCardEff.counterMonsterDragonNvlFourOrLessInGY(playerTurn) >= 1):
    #         # listCardEff.specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn)
    #         destroyed = listCardEff.counterMonsterDestroyed(playerTurn)
    #         if (destroyed > 0) and (listCardEff.counterMonsterDragonNvlFourOrLessInGY(playerTurn) > 0):
    #             listCardEff.specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn)
    #     else:
    #         print("No puedes activar esta carta!")

# class RushDragonDragears(card.MonsterEffect):
#         def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration):
#             super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration)

class PhoenixDragon(card.MonsterEffect):
        def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration, owner):
            super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text, effect, illustration, owner)