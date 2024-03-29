from random import random

from engine.state_machine import *

class Actions(State):
    previous = None
    trainer = None
    battle = False

    def run(self, *args):
        if args[0] == 'Pokemon Store':
            print('Pokemon Store')
            self.trainer.addItems()
            print('succesfully restored items!')
        elif args[0] == 'Pokemon Center':
            print('Pokemon Center')
            for pokemon in self.trainer.pokemon_list:
                pokemon.current_hp = pokemon.baseStats['hp']
                print('successfully restored ' + pokemon.name + ' hps!')
                for move in pokemon.moves:
                    move.current_pp = move.pp
                    print('successfully restored ' + move.name + ' pps!')
        elif args[0] == 'Explore':
            rnd = random()
            success = rnd > 0.8
            if success:
                print('success')
                self.battle = True
            print('Explore')


    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


## methods
pokemonStore = Actions('PokemonStore')
pokemonCenter = Actions('PokemonCenter')
explore = Actions('Explore')