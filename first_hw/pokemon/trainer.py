from pokemon.character import *

class Trainer: 
    def __init__(self, name, pokemon_list, items = []):
        self.name = name
        self.pokemon_list = pokemon_list
        self.items = items
    
    def addPokemon(self, pokemonName): 
        if len(self.pokemon_list) < 6:
            if pokemonName.lower() == 'bulbasaur':
                self.pokemon_list.append(Bulbasaur())
            elif pokemonName.lower() == 'charmander':
                self.pokemon_list.append(Charmander())
            elif pokemonName.lower() == 'squirtle':
                self.pokemon_list.append(Squirtle())
            else: 
                print('vecchio non esiste')

        else: 
            print('Not enough space in your pokemon list!')
        

    def addName(self, nickname): 
        self.name = nickname
