import copy

from engine.state_machine import *
from pokemon.character import *
from pokemon.trainer import Trainer


class CreateCharacter(State):

    def run(self, *args):
        #trainer = Trainer('', [])
        trainer = args[0]
        # name
        #print('create your pokemon trainer')
        nickname = 'ash' #input()
        trainer.addName(nickname)
        #print('Welcome ' + trainer.name)

        options = ['Bulbasaur', 'Charmender', 'Squirtle']
        pokemonlist = [Bulbasaur(), Charmander(), Squirtle()]
        #print('Chooose one Pokemon among:')
        #for i, opt in enumerate(options):
            #print(i, ':', opt)
        #choice = int(input('Choose option:'))
        pokemons_df = args[1]
        rnd_line = pokemons_df.sample()
        pokemon = Pokemon(name=rnd_line['name'].iloc[0], level=1, types=rnd_line['types'].iloc[0],
                                        baseStats=rnd_line['baseStats'].iloc[0],
                                        actStats=copy.deepcopy(rnd_line['baseStats'].iloc[0]),
                                        national_pokedex_number=rnd_line['national_pokedex_number'].iloc[0],
                                        current_hp=rnd_line['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(rnd_line['possible_moves'].iloc[0], k=2))
        trainer.addPokemon(pokemon)
        trainer.pokemon_list[0].levelUp(random.randint(1, 20))

        ## aggiungere items:
        trainer.addFullItems()
        #print('added 10 potions and 10 pokeballs!')

    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)

# methods

cc = CreateCharacter('Create Character')
