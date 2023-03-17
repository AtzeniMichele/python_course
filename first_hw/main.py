from pokemon.trainer import *
from pokemon.character import *

def main(): 

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
    ## TODO: comparare nome e poi trasformare in indice -> not in o in

    pokemon = options[choice]
    trainer.addPokemon(pokemon)

    ## TODO: confrontare velocità per chi attacca per primo 
    # TODO: continuare lo script 

    print('Chooose one Pokemon attacker:')
    for i, opt in enumerate(trainer.pokemon_list): 
        print(i, ':', opt)
    choice = int(input('Choose option:'))
    attacker = trainer.pokemon_list[choice].name

    print('Chooose one Pokemon move:')
    for i, opt in enumerate(attacker.moves): 
        print(i, ':', opt)
    choice = int(input('Choose option:'))
    move = attacker.moves[choice].name
    print(str(move.current_pp))

    print('compare un Charmander selvatico')

    ## case 1: 
    # noi attacchiamo 
    print('trainer attack')
    defender = Charmander()

    attacker.useMove(move, defender)
    print(str(move.current_pp))

    ## case 2: 
    # noi difendiamo 
    print('defender attack')
    defender.useMove(Ember(), attacker)







    



    return 

if __name__ == "__main__": 
    main()