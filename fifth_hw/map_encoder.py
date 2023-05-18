# import pandas as pd
# import numpy as np
#
# def clean_up_df(data):
#     rep = data.replace('[', '')
#     rep = rep.replace(']', '')
#     rep = rep.replace("'", '')
#     return rep
#
# def divide_df(data):
#     return str(data).split(', ')
#
# def split_pokemon_types(data, names):
#     b = pd.DataFrame(data).applymap(clean_up_df).applymap(divide_df)
#     return pd.DataFrame(b.iloc[:, 0].to_list(), columns=names)
#
# seed = 1
#
# df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
# df = df.sample(frac=1).reset_index(drop=True)
# encoder = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/map_type.csv', delimiter=';')
#
# ## outcome
# y = df['defeated']
#
# ## independent
# x = df.loc[:, df.columns != 'defeated']
# a = pd.DataFrame(x["player_types"]).applymap(clean_up_df)
# b = pd.DataFrame(x["player_types"]).applymap(clean_up_df).applymap(divide_df)
# ans = pd.DataFrame(b.iloc[:,0].to_list(), columns=['player_type1', 'player_type2'])
#
#
# player_split = split_pokemon_types(x["player_types"], ['player_type1', 'player_type2'])
# opponent_split = split_pokemon_types(x['opponent_types'], ['opponent_type1', 'opponent_type2'])
#
# variables_to_drop = ['n_game', 'starter', 'nbattle', 'enc_pkm', 'nturn', 'player_types', 'opponent_types']
# x = x.drop(variables_to_drop, axis=1)
#
# types_df = pd.concat([player_split, opponent_split], axis = 1)
# enc_player_type1 = []
# enc_player_type2 = []
# enc_opponent_type1 = []
# enc_opponent_type2 = []
# for index, row in types_df.iterrows():
#     for j, line in encoder.iterrows():
#         if row['player_type1'] == line['PokemonType']:
#             enc_player_type1.append(line['Encoder'])
#         if row['player_type2'] == line['PokemonType']:
#             enc_player_type2.append(line['Encoder'])
#         if row['opponent_type1'] == line['PokemonType']:
#             enc_opponent_type1.append(line['Encoder'])
#         if row['opponent_type2'] == line['PokemonType']:
#             enc_opponent_type2.append(line['Encoder'])
#
#     if row['player_type1'] == None:
#         enc_player_type1.append(np.nan)
#     if row['player_type2'] == None:
#         enc_player_type2.append(np.nan)
#     if row['opponent_type1'] == None:
#         enc_opponent_type1.append(np.nan)
#     if row['opponent_type2'] == None:
#         enc_opponent_type2.append(np.nan)
#
# enc_types = pd.DataFrame({'player_type1':enc_player_type1, 'player_type2':enc_player_type2, 'opponent_type1':enc_opponent_type1, 'opponent_type2':enc_opponent_type2})
# final_x = pd.concat([x, enc_types], axis = 1)
# final_x.to_csv('RefactoredPokemonResult.csv', index=False)
# y.to_csv('RefactoredOutcomePokemonResult.csv', index=False)
#
# #TODO: hot-encoding 16 colonne per tipi
# # HOW: == ciclando su nomi tipi e creare una pd series ?


# import pandas as pd
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# import numpy as np
#
# def clean_up_df(data):
#     rep = data.replace('[', '')
#     rep = rep.replace(']', '')
#     rep = rep.replace("'", '')
#     return rep
#
# def divide_df(data):
#     return np.array(str(data).split(', '))
#
# def CustomOneHot(dfRow, encoder):
#     reshapedRow = dfRow.reshape(len(dfRow), 1)
#     encodedRow = encoder.transform(reshapedRow)
#     return np.sum(encodedRow, axis=0)
#
# def Encoding(dfColumn, encoder, labelPrefix = None, columnName = None):
#     str_enc = encoder.iloc[:, 0]
#     str_enc = str_enc.values.reshape(len(str_enc), 1)
#
#     onehot = OneHotEncoder(sparse_output=False)
#     onehot = onehot.fit(str_enc)
#
#     type = pd.DataFrame(dfColumn)
#     refactoredType = type.applymap(clean_up_df).applymap(divide_df)
#     onehot_res = refactoredType.applymap(CustomOneHot, encoder=onehot)
#
#     str_enc_labeled = np.array([labelPrefix + '_' + i for i in str_enc])
#     return pd.DataFrame(onehot_res[columnName].tolist(), columns=str_enc_labeled)
#
#
# ## Load data
# encoder = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/map_type.csv', delimiter=';')
# df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
# df = df.sample(frac=1).reset_index(drop=True)
#
# player_onehot = Encoding(df['player_types'], encoder, 'player', 'player_types')
#
#
#
# #ans3 = pd.concat([df, ans2], axis=1, join='inner')
#
#
#
#
#
#
#
#
#
# # encoder = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/map_type.csv', delimiter=';')
# # label_encoder = LabelEncoder()
# # int_enc = label_encoder.fit_transform(encoder.iloc[:,0])
# # print(int_enc)
# # int_enc = int_enc.reshape(len(int_enc), 1)
# # print(int_enc)
# # str_enc = encoder.iloc[:,0]
# # str_enc = str_enc.values.reshape(len(str_enc), 1)
# #
# # onehot = OneHotEncoder(sparse_output=False)
# # onehot = onehot.fit(str_enc)
# # onehot_res = onehot.transform(str_enc)
# # print()
# #
# # prova = np.array(['bug', 'water'])
# # prova = prova.reshape(len(prova), 1)
# # prova_res = onehot.transform(prova)
# # prova_res = np.sum(prova_res, axis = 0)
# # #np.hsplit(prova_res, len(prova_res)
# # ans = pd.DataFrame(prova_res.reshape(-1, len(prova_res)), columns=str_enc)
# #
# #
# # df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
# # df = df.sample(frac=1).reset_index(drop=True)
# #
# # type = pd.DataFrame(df['player_types'])
# # ans = type.applymap(clean_up_df).applymap(divide_df)
# # b = ans.applymap(CustomOneHot, encoder = onehot)
# #
# # str_enc_pkm = np.array(['player_'+i for i in str_enc])
# # pippo = b['player_types'].tolist()
# # ans2 = pd.DataFrame(pippo, columns = str_enc_pkm)
# # ans3 = pd.concat([df, ans2], axis=1, join='inner')
#
#
#
#
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder
# import numpy as np
#
#
# def clean_up_df(data):
#     return data.replace('[', '').replace(']', '').replace("'", '')
#
#
# def divide_df(data):
#     return np.array(str(data).split(', '))
#
#
# def custom_one_hot(df_row, encoder):
#     reshaped_row = np.array(df_row).reshape(-1, 1)
#     encoded_row = encoder.transform(reshaped_row)
#     return np.sum(encoded_row, axis=0)
#
#
# def encoding(df_column, encoder_labels, label_prefix=None, column_name=None):
#     str_enc = encoder_labels.iloc[:, 0].values.reshape(-1, 1)
#
#     one_hot = OneHotEncoder(sparse_output=False)
#     one_hot.fit(str_enc)
#
#     type_df = pd.DataFrame(df_column)
#     refactored_type = type_df.applymap(clean_up_df).applymap(divide_df)
#     one_hot_res = refactored_type.applymap(lambda x: custom_one_hot(x, one_hot))
#
#     str_enc_labeled = [label_prefix + '_' + i[0] for i in str_enc]
#     return pd.DataFrame(one_hot_res[column_name].tolist(), columns=str_enc_labeled)
#
#
# ## Load data
# encoder = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/map_type.csv', delimiter=';')
# df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
# df = df.sample(frac=1).reset_index(drop=True)
#
# ## outcome
# y = df['defeated']
#
# ## independent
# x = df.loc[:, df.columns != 'defeated']
#
# variables_to_drop = ['n_game', 'starter', 'nbattle', 'enc_pkm', 'nturn']
# x = x.drop(variables_to_drop, axis=1)
#
#
# player_one_hot = encoding(x['player_types'], encoder, 'player', 'player_types')
# opponent_one_hot = encoding(x['opponent_types'], encoder, 'opponent', 'opponent_types')
#
# x = x.drop(['player_types', 'opponent_types'], axis=1)
#
#
# print('ciao')
#
# final_x = pd.concat([x, player_one_hot, opponent_one_hot], axis=1, join='inner')
#
# final_x.to_csv('RefactoredIndependentPokemonResult.csv', index=False)
# y.to_csv('RefactoredOutcomePokemonResult.csv', index=False)
