import pandas as pd

from engine.state_machine import *
from pokemon.character import *
import random
import copy
from dataset_eng import *


# selvaticPokemons = [Rattata(), Pidgey(), Caterpie()]

class Battle(State):
    trainer = None
    defeated = False
    selvaggioPokemon = None
    n_turn = 0
    hps_within_battle = []
    damages_within_battle = []
    moves_within_battle = []
    player_actstats = None
    opponent_actstats = None


    def run(self, *args):
        self.n_turn = 0
        self.hps_within_battle = []
        self.damages_within_battle = []
        self.moves_within_battle = []
        self.defeated = False
        #self.player_actstats = self.trainer.pokemon_list[0].actStats
        forward = True
        ## nuova scelta selvaggio pk:
        pokemons_df = args[0]
        rnd_line = pokemons_df.sample()
        # self.selvaggioPokemon = random.choice(args[0])
        self.selvaggioPokemon = Pokemon(name=rnd_line['name'].iloc[0], level=1, types=rnd_line['types'].iloc[0],
                                        baseStats=rnd_line['baseStats'].iloc[0],
                                        actStats=copy.deepcopy(rnd_line['baseStats'].iloc[0]),
                                        national_pokedex_number=rnd_line['national_pokedex_number'].iloc[0],
                                        current_hp=rnd_line['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(rnd_line['possible_moves'].iloc[0], k=2))
        self.selvaggioPokemon.levelUp(random.randint(1, 20))
        self.opponent_actstats = self.selvaggioPokemon.actStats
        effectiveness = args[1]
        print('a wild ' + self.selvaggioPokemon.name + ' has appeared')
        rf = args[2]
        win_proba = np.array([])
        ## ------------------- Pokemon Recommender System ---------------- ##
        for pkm in self.trainer.pokemon_list:

            str_player_types = '[' + ', '.join(pkm.types) + ']'
            str_opponent_types = '[' + ', '.join(self.selvaggioPokemon.types) + ']'
            x = {
                "player_hp": pkm.actStats['hp'],
                "player_attack": pkm.actStats['attack'],
                "player_defense": pkm.actStats['defense'],
                "player_speed": pkm.actStats['speed'],
                "player_special": pkm.actStats['special'],
                "player_types": [str_player_types],
                "opponent_hp": self.opponent_actstats['hp'],
                "opponent_attack": self.opponent_actstats['attack'],
                "opponent_defense": self.opponent_actstats['defense'],
                "opponent_speed": self.opponent_actstats['speed'],
                "opponent_special": self.opponent_actstats['special'],
                "opponent_types": [str_opponent_types],
            }

            x_df = pd.DataFrame(x)
            enc_res_player = encoding(x_df['player_types'], 'player', 'player_types')
            enc_res_opponent = encoding(x_df['opponent_types'], 'opponent', 'opponent_types')

            x_df = x_df.drop(['player_types', 'opponent_types'], axis=1)
            final_x = pd.concat([x_df, enc_res_player, enc_res_opponent], axis=1, join='inner')

            pkm_win_proba = rf.predict_proba(final_x)[0, 0]
            print(pkm.name + ': probability' + str(pkm_win_proba))
            win_proba = np.append(win_proba, np.array(pkm_win_proba))


        ## suggested/chosen pokemon:
        idx = np.argmax(win_proba)
        print('suggested pokemon is' + self.trainer.pokemon_list[idx].name)
        trainerPokemon = self.trainer.pokemon_list[idx]


        if (np.amax(win_proba) > 0.5):
            print('battle')
            choice = 0  # int(input('Choose option:'))
        else:
            print('escape')
            choice = 3
        ## -------------------------------------------------------------- ##



        while forward:
            self.n_turn += 1
            options = ['attack', 'change Pokemon', 'use item', 'run away']
            # print('choose an action:')
            # for i, opt in enumerate(options):
            # print(i, ':', opt)


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

            if self.n_turn == 100 and self.selvaggioPokemon.actStats['hp'] == self.selvaggioPokemon.current_hp and self.trainer.pokemon_list[0].actStats['hp'] == self.trainer.pokemon_list[0].current_hp:
                print('exceeded number of turns')
                forward = False
                self.defeated = None

    def update(self):
        pass

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


## methods
battle = Battle('Battle')
