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
        rnd = random.random()
        success = rnd < attackType.accuracy
        if success:
            Pokemon.computeDamage(attackType,defender,rnd)
        else: 
            null

    def computeDamage(self, attackType, defender, rnd):
        ## TODO: modifica in base al tipo d attacco (special o fisico) 
        firstArg = ((2 * self.level +10) / 250) * (self.baseStats['attack'] / defender.baseStats['defense']) * attackType['pow'] + 2
        stability = Pokemon.computeStability(attackType)
        effect = 1
        critical = Pokemon.computeCritical(rnd)
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
        super().__init__('bulbasaur', 1, ["grass","poison"],{"hp": 45, "attack": 49, "defense": 49, "speed": 45, "special": 65},  ["tackle", "razor leaf"], 45, 1)
