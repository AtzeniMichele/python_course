from engine.enginePokemon import CreateCharacter, Story
from engine.state_machine import FiniteStateMachine
from pokemon.trainer import *
from pokemon.character import *


def main():
    # trainer = Trainer('', [])
    # # name
    # print('create your pokemon trainer')
    # nickname = input()
    # trainer.addName(nickname)
    # print('Welcome ' + trainer.name)
    #
    # options = ['Bulbasaur', 'Charmender', 'Squirtle']
    # print('Chooose one Pokemon among:')
    # for i, opt in enumerate(options):
    #     print(i, ':', opt)
    # choice = int(input('Choose option:'))
    #
    # pokemon = options[choice]
    # trainer.addPokemon(pokemon)
    #
    # ## aggiungere items:
    # trainer.addFullItems()
    # print('added 10 potions and 10 pokeballs!')

    Machine = FiniteStateMachine()

    Machine.add_state(cc)
    Machine.add_state(story)

    Machine.add_transition(cc, story)

    Machine.set_start_state(cc)

    Machine.initialize()
    Machine.draw()

    cc.run()
    target = Machine.update()
    story.run()
    Machine.draw()

    Machine.do_transition(target, Machine.get_transition_attributes(target, 'dur'))

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
