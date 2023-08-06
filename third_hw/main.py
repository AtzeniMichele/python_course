from engine.story import *
from engine.create_character import *
from engine.actions import *
from engine.battle import *
from engine.exit import *
from json_handler import *
from pokemon.trainer import *
import pickle


def main():
    # game init

    ## moves
    moves_dict = json_handler('moves')
    moves_list = []
    for key, value in moves_dict.items():
        if not any([element is None for element in value.values()]):
            moves_list.append(
                Attack(name=value['name'], type=value['type'], category=value['category'], power=value['power'],
                       accuracy=value['accuracy'], pp=value['pp'], current_pp=value['pp']))

    ## pokemons
    pokemon_dict = json_handler('pokemons')
    pokemon_list = []
    for pokemon_key, pokemon_value in pokemon_dict.items():
        possible_moves = []
        for i, move in enumerate(moves_list):
            if move.type in pokemon_value['types'] or move.type == 'normal':
                possible_moves.append(moves_list[i])
        # print(len(possible_moves))
        pokemon_list.append(Pokemon(name=pokemon_value['name'], level=1, types=pokemon_value['types'],
                                    baseStats=pokemon_value['baseStats'],
                                    national_pokedex_number=pokemon_value['national_pokedex_number'],
                                    current_hp=pokemon_value['baseStats']['hp'],
                                    moves=random.choices(possible_moves, k=2)))

    effective_dict = json_effectiveness_handler('type_effectiveness')

    ##init variables
    starterList = [Bulbasaur(), Charmander(), Squirtle()]

    nGame  = 0

    #while nGame < 2:

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

    while nGame < 500:
        print('Game' + str(nGame))

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

        # machine.draw()
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
                #print('What do you want to do?:')
                #for i, opt in enumerate(action_input):
                    #print(i, ':', opt)
                choice = 2 #int(input('Choose option:'))

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
                        machine.eval_current(pokemon_list, effective_dict)
                        story.trainer = battle.trainer
                        results.append({
                            "n_game": nGame,
                            "starter": starter.name,
                            "nbattle": nBattles,
                            "defeated" : battle.defeated,
                            "enc:pkm": battle.selvaggioPokemon.name,
                            "nturn": battle.n_turn,
                            "hp_perc" : battle.trainer.pokemon_list[0].current_hp / battle.trainer.pokemon_list[0].baseStats['hp'] * 100
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
    with open("pokemon_game_results_final.p", "wb") as fb:
        pickle.dump(results, fb)
    return





if __name__ == "__main__":
    results = []
    main()
