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
    trainers_pokemon = []
    print('Chooose one Pokemon among:')
    for i, opt in enumerate(options): 
        print(i, ':', opt)
    choice = int(input('Choose option:'))
    ## TODO: comparare nome e poi trasformare in indice -> not in o in

    pokemon = options[choice]
    trainer.addPokemon(pokemon)

    ## TODO: confrontare velocità per chi attacca per primo 
    # TODO: che pokemon scegliere
    # TODO: che mossa scegliere
    # TODO: aggiornare i pp
    # TODO: continuare lo script 

    ## case 1: 
    # noi attacchiamo 
    print('trainer attack')
    defender = Charmander()
    attacker = trainer.pokemon_list[0]

    attacker.useMove(Tackle(), defender)

    ## case 2: 
    # noi difendiamo 
    print('defender attack')
    defender.useMove(Ember(), attacker)







    



    return 

if __name__ == "__main__": 
    main()