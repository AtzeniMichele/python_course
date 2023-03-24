from engine.story import *
from engine.create_character import *
from engine.state_machine import FiniteStateMachine
from pokemon.trainer import *
from pokemon.character import *


def main():
    # init machine
    machine = FiniteStateMachine()
    machine.add_state(cc, trainer=Trainer('', []))
    machine.add_state(story)
    machine.add_transition(cc, story)
    machine.set_start_state(cc)
    machine.initialize()

    # machine.draw()

    # create character
    machine.eval_current(machine.get_state_attributes('trainer'))

    # go in the main story
    story.trainer = machine.get_state_attributes('trainer')
    machine.do_transition(story)
    machine.eval_current()
    # machine.draw()

    forward = True;

    # while forward:
    #
    #     print('compare un Charmander selvatico')
    #
    #     print('Chooose one Pokemon attacker:')
    #     for i, opt in enumerate(trainer.pokemon_list):
    #         print(i, ':', opt.name)
    #     choice = int(input('Choose option:'))
    #     attacker = trainer.pokemon_list[choice]
    #
    #     print('Chooose one Pokemon move:')
    #     for i, opt in enumerate(attacker.moves):
    #         print(i, ':', opt.name)
    #     choice = int(input('Choose option:'))
    #     move = attacker.moves[choice]
    #     print(str(move.current_pp))
    #
    #     ## case 1:
    #     # noi attacchiamo
    #     print('trainer attack')
    #     defender = Charmander()
    #
    #     forward = attacker.useMove(move, defender)
    #     print(str(move.current_pp))
    #
    #     ## case 2:
    #     # noi difendiamo
    #     print('defender attack')
    #     forward = defender.useMove(Ember(), attacker)

    return


if __name__ == "__main__":
    cc = CreateCharacter('create_character')
    story = Story('Story')
    main()
