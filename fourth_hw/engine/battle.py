from engine.state_machine import *
from pokemon.character import *
import random


# selvaticPokemons = [Rattata(), Pidgey(), Caterpie()]

class Battle(State):
    trainer = None
    defeated = False
    selvaggioPokemon = None
    n_turn = 0
    hps_within_battle = []
    damages_within_battle = []
    moves_within_battle = []

    def run(self, *args):
        self.n_turn = 0
        self.hps_within_battle = []
        self.damages_within_battle = []
        self.moves_within_battle = []
        self.defeated = False
        forward = True
        ## nuova scelta selvaggio pk:
        pokemons_df = args[0]
        rnd_line = pokemons_df.sample()
        # self.selvaggioPokemon = random.choice(args[0])
        self.selvaggioPokemon = Pokemon(name=rnd_line['name'].iloc[0], level=1, types=rnd_line['types'].iloc[0],
                                        baseStats=rnd_line['baseStats'].iloc[0],
                                        actStats=rnd_line['baseStats'].iloc[0],
                                        national_pokedex_number=rnd_line['national_pokedex_number'].iloc[0],
                                        current_hp=rnd_line['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(rnd_line['possible_moves'].iloc[0], k=2))
        self.selvaggioPokemon.levelUp(random.randint(1, 20))
        trainerPokemon = self.trainer.pokemon_list[0]
        effectiveness = args[1]
        print('a wild ' + self.selvaggioPokemon.name + ' has appeared')

        while forward:
            self.n_turn += 1
            options = ['attack', 'change Pokemon', 'use item', 'run away']
            # print('choose an action:')
            # for i, opt in enumerate(options):
            # print(i, ':', opt)
            choice = 0  # int(input('Choose option:'))

            ## gestire le quattro azioni:
            if choice == 0:
                # print('Chooose one Pokemon move:')
                # for i, opt in enumerate(trainerPokemon.moves):
                # print(i, ':', opt.name)
                # choice = int(input('Choose option:'))
                move = random.choice(trainerPokemon.moves)  # trainerPokemon.moves[choice]
                forward, _, damage = trainerPokemon.useMove(move, self.selvaggioPokemon, effectiveness)
                # self.hps_within_battle.append(hps)
                self.damages_within_battle.append(damage)
                self.moves_within_battle.append(move.name)

            elif choice == 1:
                self.trainer.pokemon_list[0] = trainerPokemon
                # print('Choose one Pokemon:')
                # for i, opt in enumerate(self.trainer.pokemon_list):
                # print(i, ':', opt.name)
                choice = int(input('Choose option:'))
                trainerPokemon = self.trainer.pokemon_list[choice]
                self.trainer.pokemon_list[0], self.trainer.pokemon_list[choice] = self.trainer.pokemon_list[choice], \
                                                                                  self.trainer.pokemon_list[0]
            elif choice == 2:
                print('Choose one Item:')
                for i, opt in enumerate(self.trainer.items):
                    print(i, ':', opt)
                choice = int(input('Choose option:'))
                if choice == 0 and self.trainer.items['potions'].number > 0:
                    # pozioni
                    self.trainer.items['potions'].number = self.trainer.items['potions'].number - 1
                    trainerPokemon.current_hp = min(trainerPokemon.current_hp + 20, trainerPokemon.actStats['hp'])
                elif choice == 1 and self.trainer.items['pokeballs'].number > 0:
                    self.trainer.items['pokeballs'].number = self.trainer.items['pokeballs'].number - 1
                    catchProbability = 1 - (self.selvaggioPokemon.current_hp / self.selvaggioPokemon.actStats['hp'])
                    if catchProbability > random.random():
                        self.trainer.addPokemon(self.selvaggioPokemon)
            elif choice == 3:
                if random.random() > 0.6:
                    self.trainer.pokemon_list[0] = trainerPokemon
                    forward = False

            if forward:
                print('selvatic attacks')
                forward, hps, _ = self.selvaggioPokemon.useMove(random.choice(self.selvaggioPokemon.moves),
                                                                trainerPokemon,
                                                                effectiveness)
                self.hps_within_battle.append(hps)

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
