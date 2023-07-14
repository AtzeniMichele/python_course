from engine.story import *
from engine.create_character import *
from engine.actions import *
from engine.battle import *
from engine.exit import *
from json_handler import *
from pokemon.trainer import *
import pickle
import pandas as pd


def main():
    # game init

    ## moves:
    moves_df = pd.read_json('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/moves.json', lines=True)
    moves_df = moves_df.dropna(subset=['name', 'type', 'category', 'power', 'accuracy', 'pp'])

    ## pokemons:
    pokemons_df = pd.read_json('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/pokemons.json',
                               lines=True)

    ##filtering moves
    pokemons_moves = []
    for pokemon_index, pokemon_row in pokemons_df.iterrows():
        filtered_moves = []
        for move_index, move_row in moves_df.iterrows():
            if move_row['type'] in pokemon_row['types'] or move_row['type'] == 'normal':
                move = Attack(name=move_row['name'], type=move_row['type'], category=move_row['category'], power=move_row['power'],
                        accuracy=move_row['accuracy'], pp=move_row['pp'], current_pp=move_row['pp'])
                filtered_moves.append(move)
        pokemons_moves.append(filtered_moves)
    pokemons_df['possible_moves'] = pokemons_moves

    ## effectiveness:
    effectiveness_df = pd.read_json(
        'C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/type_effectiveness.json', lines=True)
    #
    # ## moves
    # moves_dict = json_handler('moves')
    # moves_list = []
    # for key, value in moves_dict.items():
    #     if not any([element is None for element in value.values()]):
    #         moves_list.append(
    #             Attack(name=value['name'], type=value['type'], category=value['category'], power=value['power'],
    #                    accuracy=value['accuracy'], pp=value['pp'], current_pp=value['pp']))
    #
    ## pokemons
    # pokemon_dict = json_handler('pokemons')
    # pokemon_list = []
    # for pokemon_key, pokemon_value in pokemon_dict.items():
    #     possible_moves = []
    #     for i, move in enumerate(moves_list):
    #         if move.type in pokemon_value['types'] or move.type == 'normal':
    #             possible_moves.append(moves_list[i])
    #     # print(len(possible_moves))
    #     pokemon_list.append(Pokemon(name=pokemon_value['name'], level=1, types=pokemon_value['types'],
    #                                 baseStats=pokemon_value['baseStats'],
    #                                 national_pokedex_number=pokemon_value['national_pokedex_number'],
    #                                 current_hp=pokemon_value['baseStats']['hp'],
    #                                 moves=random.choices(possible_moves, k=2)))
    #
    # effective_dict = json_effectiveness_handler('type_effectiveness')

    ##init variables
    startersAttributes = [pokemons_df.loc[pokemons_df['name'] =='bulbasaur'], pokemons_df.loc[pokemons_df['name'] =='charmander'], pokemons_df.loc[pokemons_df['name'] =='squirtle']]
    starterList = [Pokemon(name=startersAttributes[0]['name'].iloc[0], level=1, types=startersAttributes[0]['types'].iloc[0],
                                        baseStats=startersAttributes[0]['baseStats'].iloc[0],
                                        actStats=startersAttributes[0]['baseStats'].iloc[0],
                                        national_pokedex_number=startersAttributes[0]['national_pokedex_number'].iloc[0],
                                        current_hp=startersAttributes[0]['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(startersAttributes[0]['possible_moves'].iloc[0], k=2)),
                   Pokemon(name=startersAttributes[1]['name'].iloc[0], level=1, types=startersAttributes[1]['types'].iloc[0],
                                        baseStats=startersAttributes[1]['baseStats'].iloc[0],
                                        actStats=startersAttributes[1]['baseStats'].iloc[0],
                                        national_pokedex_number=startersAttributes[1]['national_pokedex_number'].iloc[0],
                                        current_hp=startersAttributes[1]['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(startersAttributes[1]['possible_moves'].iloc[0], k=2)),
                   Pokemon(name=startersAttributes[2]['name'].iloc[0], level=1, types=startersAttributes[2]['types'].iloc[0],
                                        baseStats=startersAttributes[2]['baseStats'].iloc[0],
                                        actStats=startersAttributes[2]['baseStats'].iloc[0],
                                        national_pokedex_number=startersAttributes[2]['national_pokedex_number'].iloc[0],
                                        current_hp=startersAttributes[2]['baseStats'].iloc[0]['hp'],
                                        moves=random.choices(startersAttributes[2]['possible_moves'].iloc[0], k=2))]
    nGame = 0

    # while nGame < 2:

    # forward = True
    # # init machine
    # machine = FiniteStateMachine()
    # machine.add_state(cc, trainer=Trainer('', []))
    # machine.add_state(story)
    # machine.add_state(pokemonStore, name='Pokemon Store')
    # machine.add_state(pokemonCenter, name='Pokemon Center')
    # machine.add_state(explore, name='Explore')
    # machine.add_state(battle, name='Battle')
    # machine.add_state(close)
    #
    # machine.add_transition(cc, story)
    # machine.add_transition(story, pokemonStore)
    # machine.add_transition(pokemonStore, story)
    # machine.add_transition(story, pokemonCenter)
    # machine.add_transition(pokemonCenter, story)
    # machine.add_transition(story, explore)
    # machine.add_transition(explore, story)
    # machine.add_transition(explore, battle)
    # machine.add_transition(battle, story)
    # machine.add_transition(battle, pokemonCenter)
    # machine.add_transition(story, close)
    #
    # machine.set_start_state(cc)
    # machine.initialize()
    #
    # machine.draw()
    # continueGame = True
    #
    # # create character
    # machine.eval_current(machine.get_state_attributes('trainer'), starterList[0])
    #
    # # go in the main story
    # story.trainer = machine.get_state_attributes('trainer')
    # machine.do_transition(story)
    # machine.eval_current()
    # # machine.draw()

    while nGame < 1000:
        print('-------------newGame! ' + str(nGame) + "---------------")

        forward = True
        # init machine
        machine = FiniteStateMachine()
        machine.add_state(cc, trainer=Trainer('', []))
        machine.add_state(story)
        machine.add_state(pokemonStore, name='Pokemon Store')
        machine.add_state(pokemonCenter, name='Pokemon Center')
        machine.add_state(explore, name='Explore')
        machine.add_state(battle, name='Battle')
        machine.add_state(close)

        machine.add_transition(cc, story)
        machine.add_transition(story, pokemonStore)
        machine.add_transition(pokemonStore, story)
        machine.add_transition(story, pokemonCenter)
        machine.add_transition(pokemonCenter, story)
        machine.add_transition(story, explore)
        machine.add_transition(explore, story)
        machine.add_transition(explore, battle)
        machine.add_transition(battle, story)
        machine.add_transition(battle, pokemonCenter)
        machine.add_transition(story, close)

        machine.set_start_state(cc)
        machine.initialize()

        #machine.draw()
        continueGame = True

        # create character
        machine.eval_current(machine.get_state_attributes('trainer'), starterList[0])

        # go in the main story
        story.trainer = machine.get_state_attributes('trainer')
        machine.do_transition(story)
        machine.eval_current()
        # machine.draw()

        for starter in starterList:

            story.trainer.pokemon_list[0] = starter
            nBattles = 0
            while nBattles < 150:

                # actions
                action_input = ['Go to pokemon store', 'Go to pokemon center', 'Explore', 'Exit']
                # print('What do you want to do?:')
                # for i, opt in enumerate(action_input):
                # print(i, ':', opt)
                choice = 2  # int(input('Choose option:'))

                if choice == 0:
                    pokemonStore.trainer = story.trainer
                    machine.do_transition(pokemonStore)
                    machine.eval_current(machine.get_state_attributes('name'))

                    # return to the story
                    story.trainer = pokemonStore.trainer
                    machine.do_transition(story)
                    # machine.draw()
                elif choice == 1:
                    pokemonCenter.trainer = story.trainer
                    machine.do_transition(pokemonCenter)
                    machine.eval_current(machine.get_state_attributes('name'))
                    # return to the story
                    story.trainer = pokemonCenter.trainer
                    machine.do_transition(story)

                    # machine.draw()
                elif choice == 2:
                    explore.trainer = story.trainer
                    machine.do_transition(explore)
                    machine.eval_current(machine.get_state_attributes('name'))
                    if explore.battle:
                        battle.trainer = story.trainer
                        machine.do_transition(battle)
                        machine.eval_current(pokemons_df, effectiveness_df)
                        story.trainer = battle.trainer
                        results.append({
                            "n_game": nGame,
                            "starter": starter.name,
                            "starter_level": starter.level,
                            "starter_types": starter.types,
                            "nbattle": nBattles,
                            "defeated": battle.defeated,
                            "enc_pkm": battle.selvaggioPokemon.name,
                            "enc_pkm_level": battle.selvaggioPokemon.level,
                            "enc_pkm_types": battle.selvaggioPokemon.types,
                            "nturn": battle.n_turn,
                            "hps_within_battle":battle.hps_within_battle, # trainer pokemon
                            "damages_within_battle":battle.damages_within_battle, # trainer pokemon
                            "moves_within_battle":battle.moves_within_battle, # trainer pokemon
                            "hp_perc": battle.trainer.pokemon_list[0].current_hp /
                                       battle.trainer.pokemon_list[0].actStats['hp'] * 100
                        })
                        if True:
                            pokemonCenter.trainer = battle.trainer
                            machine.do_transition(pokemonCenter)
                            machine.eval_current(machine.get_state_attributes('name'))
                            story.trainer = pokemonCenter.trainer
                            nBattles += 1

                    machine.do_transition(story)
                    # machine.draw()
                elif choice == 3:
                    machine.do_transition(close)
                    machine.eval_current()
                    # machine.draw()
            continueGame = False
        nGame += 1
    df = pd.DataFrame(results)
    df.to_csv('PokemonResult.csv', index=False)
    # with open("pokemon_game_results.p", "wb") as fb:
    #     pickle.dump(results, fb)
    return


if __name__ == "__main__":
    results = []
    main()
