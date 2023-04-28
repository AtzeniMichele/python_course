import pandas as pd
import numpy as np

def clean_up_df(data):
    rep = data.replace('[', '')
    rep = rep.replace(']', '')
    rep = rep.replace("'", '')
    return rep

def divide_df(data):
    return str(data).split(', ')

def split_pokemon_types(data, names):
    b = pd.DataFrame(data).applymap(clean_up_df).applymap(divide_df)
    return pd.DataFrame(b.iloc[:, 0].to_list(), columns=names)

seed = 1

df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
df = df.sample(frac=1).reset_index(drop=True)
encoder = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/map_type.csv', delimiter=';')

## outcome
y = df['defeated']

## independent
x = df.loc[:, df.columns != 'defeated']
a = pd.DataFrame(x["player_types"]).applymap(clean_up_df)
b = pd.DataFrame(x["player_types"]).applymap(clean_up_df).applymap(divide_df)
ans = pd.DataFrame(b.iloc[:,0].to_list(), columns=['player_type1', 'player_type2'])


player_split = split_pokemon_types(x["player_types"], ['player_type1', 'player_type2'])
opponent_split = split_pokemon_types(x['opponent_types'], ['opponent_type1', 'opponent_type2'])

variables_to_drop = ['n_game', 'starter', 'nbattle', 'enc_pkm', 'nturn', 'player_types', 'opponent_types']
x = x.drop(variables_to_drop, axis=1)

types_df = pd.concat([player_split, opponent_split], axis = 1)
enc_player_type1 = []
enc_player_type2 = []
enc_opponent_type1 = []
enc_opponent_type2 = []
for index, row in types_df.iterrows():
    for j, line in encoder.iterrows():
        if row['player_type1'] == line['PokemonType']:
            enc_player_type1.append(line['Encoder'])
        if row['player_type2'] == line['PokemonType']:
            enc_player_type2.append(line['Encoder'])
        if row['opponent_type1'] == line['PokemonType']:
            enc_opponent_type1.append(line['Encoder'])
        if row['opponent_type2'] == line['PokemonType']:
            enc_opponent_type2.append(line['Encoder'])

    if row['player_type1'] == None:
        enc_player_type1.append(np.nan)
    if row['player_type2'] == None:
        enc_player_type2.append(np.nan)
    if row['opponent_type1'] == None:
        enc_opponent_type1.append(np.nan)
    if row['opponent_type2'] == None:
        enc_opponent_type2.append(np.nan)

enc_types = pd.DataFrame({'player_type1':enc_player_type1, 'player_type2':enc_player_type2, 'opponent_type1':enc_opponent_type1, 'opponent_type2':enc_opponent_type2})
final_x = pd.concat([x, enc_types], axis = 1)
final_x.to_csv('RefactoredPokemonResult.csv', index=False)
y.to_csv('RefactoredOutcomePokemonResult.csv', index=False)