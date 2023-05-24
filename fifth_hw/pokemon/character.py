import random
import math
from pokemon.attack import *
import numpy as np


class Pokemon:
    def __init__(self, name, level, types, baseStats, actStats, moves, current_hp, national_pokedex_number):
        self.name = name
        self.level = level
        self.types = types
        self.baseStats = baseStats
        self.actStats = actStats
        self.moves = moves
        self.current_hp = current_hp
        self.national_pokedex_number = national_pokedex_number

    def useMove(self, attackType, defender, effectiveness):
        if attackType.current_pp > 0:
            rnd = random.random()
            success = rnd < attackType.accuracy
            if success:
                print('successfully attacking!')
                damage = self.computeDamage(attackType, defender, rnd, effectiveness)

                defender.current_hp = defender.current_hp - damage
                #attackType.current_pp = attackType.current_pp - 1
                ## se arriva a 0? rip 
                if defender.current_hp <= 0:
                    print('The attack hits ' + str(damage) + ', ' + defender.name + ' is defeated!')
                    return False, 0, damage
                else:
                    print('The attack hits ' + str(damage) + ', ' + defender.name + ' current hps are:' + str(
                        defender.current_hp))
                    return True, defender.current_hp, damage
            else:
                return True, defender.current_hp, 0

        else:
            print('this move cannot be used anymore!')

    def computeDamage(self, attackType, defender, rnd, effectiveness):
        if attackType.category == 'special':
            firstArg = ((2 * self.level + 10) / 250) * (
                        self.actStats['special'] / defender.actStats['special']) * attackType.power + 2
        else:
            firstArg = ((2 * self.level + 10) / 250) * (
                        self.actStats['attack'] / defender.actStats['defense']) * attackType.power + 2
        stability = self.computeStability(attackType)
        effect = self.computeEffect(effectiveness, attackType, defender)
        critical = self.computeCritical(rnd)
        luck = random.uniform(0.85, 1)
        modifier = stability * effect * critical * luck
        damage = math.floor(firstArg * modifier)
        return damage

    def computeEffect(self, effectiveness, attackType, defender):
        effects = np.zeros(len(defender.types))
        for j in range(len(defender.types)):
            #unique_combinations.append((attackType.type, defender.types[j]))
            for index, row in effectiveness.iterrows():
                if row['attack'] == attackType.type and row['defend'] == defender.types[j]:
                    effects[j] = row['effectiveness']
            # for key,value in effectiveness.items():
            #     if value['attack'] == attackType.type and value['defend'] == defender.types[j]:
            #         #effects.append(value['effectiveness'])
            #         effects[j] = value['effectiveness']
        #print(str(effects) + 'result: ' + str(np.prod(effects)))


        return np.prod(effects)




    def computeStability(self, attackType):
        if attackType.type in self.types:
            return 1.5
        else:
            return 1

    def computeCritical(self, rnd):
        if rnd < self.actStats['speed'] / 512:
            return 2
        else:
            return 1

    def levelUp(self, level):
        self.level = level
        for key,value in self.baseStats.items():
            if key == 'hp':
                self.current_hp = np.floor(self.baseStats['hp'] * 2 * level / 100) + level + 10
                self.actStats[key] = self.current_hp
            else:
                self.actStats[key] = np.floor(self.baseStats[key] * 2 * level / 100) + 5



class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__('bulbasaur', 1, ["grass", "poison"],
                         {"hp": 45, "attack": 49, "defense": 49, "speed": 45, "special": 65}, {"hp": 45, "attack": 49, "defense": 49, "speed": 45, "special": 65}, [Tackle(), RazorLeaf()],
                         45, 1)


class Charmander(Pokemon):
    def __init__(self):
        super().__init__('charmander', 1, ['fire'], {"hp": 39, "attack": 52, "defense": 43, "speed": 65, "special": 50}, {"hp": 39, "attack": 52, "defense": 43, "speed": 65, "special": 50},
                         [Tackle(), Ember()], 39, 4)


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__('squirtle', 1, ["water"], {"hp": 44, "attack": 48, "defense": 65, "speed": 43, "special": 50}, {"hp": 44, "attack": 48, "defense": 65, "speed": 43, "special": 50},
                         [Tackle(), WaterGun()], 44, 7)


class Caterpie(Pokemon):
    def __init__(self):
        super().__init__('caterpie', 1, ["bug"], {"hp": 45, "attack": 30, "defense": 35, "speed": 45, "special": 20}, {"hp": 45, "attack": 30, "defense": 35, "speed": 45, "special": 20},
                         [Twineedle()], 45, 10)


class Pidgey(Pokemon):
    def __init__(self):
        super().__init__('pidgey', 1, ["normal", "flying"],
                         {"hp": 40, "attack": 45, "defense": 40, "speed": 56, "special": 35}, {"hp": 40, "attack": 45, "defense": 40, "speed": 56, "special": 35}, [Tackle(), Peck()], 40,
                         16)

class Rattata(Pokemon):
    def __init__(self):
        super().__init__('rattata', 1, ["normal"],{"hp": 30, "attack": 56, "defense": 35, "speed": 72, "special": 25}, {"hp": 30, "attack": 56, "defense": 35, "speed": 72, "special": 25}, [Tackle()], 30, 19)
