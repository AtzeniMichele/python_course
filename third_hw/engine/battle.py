from engine.state_machine import *
from pokemon.character import *
import random


# selvaticPokemons = [Rattata(), Pidgey(), Caterpie()]

class Battle(State):
    trainer = None
    defeated = False
    selvaggioPokemon = None
    n_turn = 0

    def run(self, *args):
        self.n_turn = 0
        self.defeated = False
        forward = True
        self.selvaggioPokemon = random.choice(args[0])
        trainerPokemon = self.trainer.pokemon_list[0]
        effectiveness = args[1]
        #print('a wild ' + self.selvaggioPokemon.name + ' has appeared')

        while forward:
            self.n_turn += 1
            options = ['attack', 'change Pokemon', 'use item', 'run away']
            #print('choose an action:')
            #for i, opt in enumerate(options):
                # print(i, ':', opt)
            choice = 0  # int(input('Choose option:'))

            ## gestire le quattro azioni:
            if choice == 0:
                #print('Chooose one Pokemon move:')
                #for i, opt in enumerate(trainerPokemon.moves):
                    #print(i, ':', opt.name)
                # choice = int(input('Choose option:'))
                move = random.choice(trainerPokemon.moves)  # trainerPokemon.moves[choice]
                forward = trainerPokemon.useMove(move, self.selvaggioPokemon, effectiveness)

            elif choice == 1:
                self.trainer.pokemon_list[0] = trainerPokemon
                #print('Choose one Pokemon:')
                #for i, opt in enumerate(self.trainer.pokemon_list):
                    #print(i, ':', opt.name)
                choice = int(input('Choose option:'))
                trainerPokemon = self.trainer.pokemon_list[choice]
                self.trainer.pokemon_list[0], self.trainer.pokemon_list[choice] = self.trainer.pokemon_list[choice], \
                                                                                  self.trainer.pokemon_list[0]
            elif choice == 2:
                #print('Choose one Item:')
                for i, opt in enumerate(self.trainer.items):
                    print(i, ':', opt)
                choice = int(input('Choose option:'))
                if choice == 0 and self.trainer.items['potions'].number > 0:
                    # pozioni
                    self.trainer.items['potions'].number = self.trainer.items['potions'].number - 1
                    trainerPokemon.current_hp = min(trainerPokemon.current_hp + 20, trainerPokemon.baseStats['hp'])
                elif choice == 1 and self.trainer.items['pokeballs'].number > 0:
                    self.trainer.items['pokeballs'].number = self.trainer.items['pokeballs'].number - 1
                    catchProbability = 1 - (self.selvaggioPokemon.current_hp / self.selvaggioPokemon.baseStats['hp'])
                    if catchProbability > random.random():
                        self.trainer.addPokemon(self.selvaggioPokemon)
            elif choice == 3:
                if random.random() > 0.6:
                    self.trainer.pokemon_list[0] = trainerPokemon
                    forward = False


            if forward:
                #print('selvatic attacks')
                forward = self.selvaggioPokemon.useMove(random.choice(self.selvaggioPokemon.moves), trainerPokemon,
                                                        effectiveness)

                if not forward:
                    self.defeated = True

    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


## methods
battle = Battle('Battle')
