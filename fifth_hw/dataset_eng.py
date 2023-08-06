import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np


def clean_up_df(data):
    return data.replace('[', '').replace(']', '').replace("'", '')


def divide_df(data):
    return np.array(str(data).split(', '))


def custom_one_hot(df_row, encoder):
    reshaped_row = np.array(df_row).reshape(-1, 1)
    encoded_row = encoder.transform(reshaped_row)
    return np.sum(encoded_row, axis=0)


def encoding(df_column, label_prefix=None, column_name=None):
    encoder_labels = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/data/map_type.csv', delimiter=';')
    str_enc = encoder_labels.iloc[:, 0].values.reshape(-1, 1)

    one_hot = OneHotEncoder(sparse_output=False)
    one_hot.fit(str_enc)

    type_df = pd.DataFrame(df_column)
    refactored_type = type_df.applymap(clean_up_df).applymap(divide_df)
    one_hot_res = refactored_type.applymap(lambda x: custom_one_hot(x, one_hot))

    str_enc_labeled = [label_prefix + '_' + i[0] for i in str_enc]
    return pd.DataFrame(one_hot_res[column_name].tolist(), columns=str_enc_labeled)


# ## Load data
df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/data/PokemonResult.csv', delimiter=';')
df = df.sample(frac=1).reset_index(drop=True)

## outcome
y = df['defeated']

## independent
x = df.loc[:, df.columns != 'defeated']

variables_to_drop = ['n_game', 'starter', 'nbattle', 'enc_pkm', 'nturn']
x = x.drop(variables_to_drop, axis=1)


player_one_hot = encoding(x['player_types'], 'player', 'player_types')
opponent_one_hot = encoding(x['opponent_types'], 'opponent', 'opponent_types')

x = x.drop(['player_types', 'opponent_types'], axis=1)

final_x = pd.concat([x, player_one_hot, opponent_one_hot], axis=1, join='inner')

final_x.to_csv('RefactoredIndependentPokemonResult.csv', index=False)
y.to_csv('RefactoredOutcomePokemonResult.csv', index=False)