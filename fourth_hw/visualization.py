import pickle
import matplotlib
import numpy as np
import pandas as pd

pokemonsDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/pokemons.json', lines=True)
print(pokemonsDf)
movesDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/moves.json', lines=True)
print(movesDf)
effectivenessDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/type_effectiveness.json', lines=True)
print(effectivenessDf)


# pickle_in = open("pokemon_game_results.p", "rb")
# data = pickle.load(pickle_in)
#
#
# # 1. lineplot
# print('debug')
#
# # processing
#
# # bulbasaur
# bulbasaur_subset = {}
# for i,line in enumerate(data):
#     if line['starter'] == 'bulbasaur':
#         bulbasaur_subset[i] = line
#
# #n_games = np.arange(0, bulbasaur_subset[-1]['n_game']+1).tolist()
#
# # defeated_count = 0
# # for key,value in bulbasaur_subset.items():
# #
# # for game in n_games:
# #     defeated_count = 0
# #
#
# prova = dict((key,value) for key, value in bulbasaur_subset.items() if key == 'n_game' and value == 0)
# print(prova)
