from engine.state_machine import *
from pokemon.attack import Ember
from pokemon.character import Charmander


class Battle(State):
    trainer = None
    defeated = False

    def run(self, *args):
        forward = True
        defender = Charmander()
        while forward:
            print('compare un Charmander selvatico')

            print('Chooose one Pokemon attacker:')
            for i, opt in enumerate(self.trainer.pokemon_list):
                print(i, ':', opt.name)
            choice = int(input('Choose option:'))
            attacker = self.trainer.pokemon_list[choice]

            print('Chooose one Pokemon move:')
            for i, opt in enumerate(attacker.moves):
                print(i, ':', opt.name)
            choice = int(input('Choose option:'))
            move = attacker.moves[choice]
            print(str(move.current_pp))

            ## case 1:
            # noi attacchiamo
            print('trainer attack')

            forward = attacker.useMove(move, defender)
            print(str(move.current_pp))

            if forward:
                ## case 2:
                # noi difendiamo
                print('defender attack')
                forward = defender.useMove(Ember(), attacker)
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