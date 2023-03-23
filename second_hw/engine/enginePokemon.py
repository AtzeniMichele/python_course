from engine.state_machine import *
from pokemon.trainer import *


class CreateCharacter(State):
    previous = None
    counter = 0

    def run(self):
        #print(self.name)
        trainer = Trainer('', [])
        # name
        print('create your pokemon trainer')
        nickname = input()
        trainer.addName(nickname)
        print('Welcome ' + trainer.name)

        options = ['Bulbasaur', 'Charmender', 'Squirtle']
        print('Chooose one Pokemon among:')
        for i, opt in enumerate(options):
            print(i, ':', opt)
        choice = int(input('Choose option:'))

        pokemon = options[choice]
        trainer.addPokemon(pokemon)

        ## aggiungere items:
        trainer.addFullItems()
        print('added 10 potions and 10 pokeballs!')


    def update(self):
        Story('story').run(self.trainer)
        return self.trainer



    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)


class Story(State):
    #previous = None
    counter = 0

    def run(self, trainer):
        print('We are in the main story!')
        print(trainer.name)

    def update(self, choices):
        print(self.choices)

    def __str__(self):
        return '[State: ' + self.name + ']'

    def __repr__(self):
        return str(self)