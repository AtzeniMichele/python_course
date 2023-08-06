from engine.story import *
from engine.create_character import *
from engine.actions import *
from engine.battle import *
from engine.exit import *
from pokemon.trainer import *


def main():
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

    machine.draw()

    # create character
    machine.eval_current(machine.get_state_attributes('trainer'))

    # go in the main story
    story.trainer = machine.get_state_attributes('trainer')
    machine.do_transition(story)
    machine.eval_current()
    #machine.draw()

    while forward:

        # actions
        action_input = ['Go to pokemon store', 'Go to pokemon center', 'Explore', 'Exit']
        print('What do you want to do?:')
        for i, opt in enumerate(action_input):
            print(i, ':', opt)
        choice = int(input('Choose option:'))

        if choice == 0:
            pokemonStore.trainer = story.trainer
            machine.do_transition(pokemonStore)
            machine.eval_current(machine.get_state_attributes('name'))

            # return to the story
            story.trainer = pokemonStore.trainer
            machine.do_transition(story)
            #machine.draw()
        elif choice == 1:
            pokemonCenter.trainer = story.trainer
            machine.do_transition(pokemonCenter)
            machine.eval_current(machine.get_state_attributes('name'))
            # return to the story
            story.trainer = pokemonCenter.trainer
            machine.do_transition(story)

            #machine.draw()
        elif choice == 2:
            explore.trainer = story.trainer
            machine.do_transition(explore)
            machine.eval_current(machine.get_state_attributes('name'))
            if explore.battle:
                battle.trainer = story.trainer
                machine.do_transition(battle)
                machine.eval_current()
                story.trainer = battle.trainer
                if battle.defeated:
                    pokemonCenter.trainer = battle.trainer
                    machine.do_transition(pokemonCenter)
                    machine.eval_current(machine.get_state_attributes('name'))
                    story.trainer = pokemonCenter.trainer
                          
            machine.do_transition(story)
            #machine.draw()
        elif choice == 3:
            machine.do_transition(close)
            machine.eval_current()
            #machine.draw()

    return


if __name__ == "__main__":
    main()
