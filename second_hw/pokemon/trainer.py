from pokemon.character import *
from pokemon.items import *


class Trainer:
    def __init__(self, name, pokemon_list, items={}):
        self.name = name
        self.pokemon_list = pokemon_list
        self.items = items

    def addPokemon(self, pokemon):
        if len(self.pokemon_list) < 6:
            # if pokemonName.lower() == 'bulbasaur':
            #     self.pokemon_list.append(Bulbasaur())
            # elif pokemonName.lower() == 'charmander':
            #     self.pokemon_list.append(Charmander())
            # elif pokemonName.lower() == 'squirtle':
            #     self.pokemon_list.append(Squirtle())
            # else:
            #     print('vecchio non esiste')
            self.pokemon_list.append(pokemon)

        else:
            print('Not enough space in your pokemon list!')

    def addName(self, nickname):
        self.name = nickname

    def addFullItems(self):
        self.items
        self.items['potions'] = Potions()
        self.items['pokeballs'] = Pokeballs()


    def addItems(self):
        # potions
        self.items['potions'].number = self.items['potions'].max
        self.items['pokeballs'].number = self.items['pokeballs'].max
