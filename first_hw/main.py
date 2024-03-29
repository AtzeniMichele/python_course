from pokemon.trainer import *
from pokemon.character import *


def main(): 

    trainer = Trainer('', [])
    # name 
    print('insert the name of your pokemon trainer')
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



    forward = True; 
    defender = Charmander()

    while(forward): 

        print('a selvatic Charmander appears')

        print('Choose your Pokemon attacker:')
        for i, opt in enumerate(trainer.pokemon_list): 
            print(i, ':', opt.name)
        choice = int(input('Choose option:'))
        attacker = trainer.pokemon_list[choice]

        print('Choose one Pokemon move:')
        for i, opt in enumerate(attacker.moves): 
            print(i, ':', opt.name)
        choice = int(input('Choose option:'))
        move = attacker.moves[choice]
        print(str(move.current_pp))

        ## case 1: 
        # noi attacchiamo 
        print('trainer attacks')

        forward = attacker.useMove(move, defender)
        print(str(move.current_pp))

        ## case 2: 
        # noi difendiamo 
        print('defender attacks')
        forward = defender.useMove(Ember(), attacker)







    



    return 

if __name__ == "__main__": 
    main()