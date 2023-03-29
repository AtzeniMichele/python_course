import random
import math
from pokemon.attack import *


class Pokemon:
    def __init__(self, name, level, types, baseStats, moves, current_hp, national_pokedex_number):
        self.name = name
        self.level = level
        self.types = types
        self.baseStats = baseStats
        self.moves = moves
        self.current_hp = current_hp
        self.national_pokedex_number = national_pokedex_number

    def useMove(self, attackType, defender):
        if attackType.current_pp > 0:
            rnd = random.random()
            success = rnd < attackType.accuracy
            if success:
                print('successfully attacking!')
                damage = self.computeDamage(attackType, defender, rnd)

                defender.current_hp = defender.current_hp - damage
                attackType.current_pp = attackType.current_pp - 1
                ## se arriva a 0? rip 
                if defender.current_hp <= 0:
                    print('The attack hits ' + str(damage) + ', ' + defender.name + ' is defeated!')
                    return False
                else:
                    print('The attack hits ' + str(damage) + ', ' + defender.name + ' current hps are:' + str(
                        defender.current_hp))
                    return True

        else:
            print('this move cannot be used anymore!')

    def computeDamage(self, attackType, defender, rnd):
        if attackType.category == 'special':
            firstArg = ((2 * self.level + 10) / 250) * (
                        self.baseStats['special'] / defender.baseStats['special']) * attackType.power + 2
        else:
            firstArg = ((2 * self.level + 10) / 250) * (
                        self.baseStats['attack'] / defender.baseStats['defense']) * attackType.power + 2
        stability = self.computeStability(attackType)
        effect = 1
        critical = self.computeCritical(rnd)
        luck = random.uniform(0.85, 1)
        modifier = stability * effect * critical * luck
        damage = math.floor(firstArg * modifier)
        return damage

    def computeStability(self, attackType):
        if attackType.type in self.types:
            return 1.5
        else:
            return 1

    def computeCritical(self, rnd):
        if rnd < self.baseStats['speed'] / 512:
            return 2
        else:
            return 1


class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__('bulbasaur', 1, ["grass", "poison"],
                         {"hp": 45, "attack": 49, "defense": 49, "speed": 45, "special": 65}, [Tackle(), RazorLeaf()],
                         45, 1)


class Charmander(Pokemon):
    def __init__(self):
        super().__init__('charmander', 1, ['fire'], {"hp": 39, "attack": 52, "defense": 43, "speed": 65, "special": 50},
                         [Tackle(), Ember()], 39, 4)


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__('squirtle', 1, ["water"], {"hp": 44, "attack": 48, "defense": 65, "speed": 43, "special": 50},
                         [Tackle(), WaterGun()], 44, 7)


class Caterpie(Pokemon):
    def __init__(self):
        super().__init__('caterpie', 1, ["bug"], {"hp": 45, "attack": 30, "defense": 35, "speed": 45, "special": 20},
                         [Twineedle()], 45, 10)


class Pidgey(Pokemon):
    def __init__(self):
        super().__init__('pidgey', 1, ["normal", "flying"],
                         {"hp": 40, "attack": 45, "defense": 40, "speed": 56, "special": 35}, [Tackle(), Peck()], 40,
                         16)

class Rattata(Pokemon):
    def __init__(self):
        super().__init__('rattata', 1, ["normal"],{"hp": 30, "attack": 56, "defense": 35, "speed": 72, "special": 25}, [Tackle()], 30, 19)
