import pickle
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import groupby
from matplotlib.ticker import MaxNLocator


def clean_up_df(data):
    return data.replace('[', '').replace(']', '').replace("'", '')


def divide_df(data):
    return np.array(str(data).split(', '))


def create_subset(pkm_name, input_data):
    subset = []
    for i, line in input_data.iterrows():
        if line['starter'] == pkm_name:
            subset.append(line)
    return subset


def double_converter(data, max):
    floats = []
    for _, line in data.iterrows():
        tmp = [float(x) for x in line[0]]
        if max - len(tmp) > 0:
            nans = np.full(max - len(tmp), np.nan).tolist()
            tmp.extend(nans)
        floats.append(tmp)
    return floats


def simple_plot(data):
    y = np.nanmean(data, axis=0)
    x = np.arange(1, len(y) + 1)
    e = np.nanstd(data, axis=0)
    yerr0 = y - e
    yerr1 = y + e

    fig, ax = plt.subplots()
    ax.plot(x, y, color='C1')
    plt.fill_between(x, yerr0, yerr1, color='C0', alpha=0.5)
    plt.show()


def preprocessing_pie_plot(pkm_name, input_data):
    subset = create_subset(pkm_name, input_data)
    piePlot_data = {}
    for i in subset:
        list_moves = []
        str_move = i['moves_within_battle']
        tmp = divide_df(clean_up_df(str_move)).tolist()

        for j in tmp:
            if j in piePlot_data:
                # add to already existing key
                counter = piePlot_data[j] + 1
                piePlot_data[j] = counter
            else:
                # create new key, then add
                piePlot_data[j] = 1
    return piePlot_data


def pie_plot(data, name):
    plt.figure()
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title(name)
    plt.show()


def pie_plot2(dataJson, dataRes):
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    ax[0].pie(dataJson.values, labels=dataJson.index.values.tolist(), autopct='%1.1f%%')
    ax[0].set_title('Json file types')
    ax[1].pie(dataRes.values, labels=dataRes.index.values.tolist(), autopct='%1.1f%%')
    ax[1].set_title('Results file types')
    plt.show()


def bar_chart(data):
    plt.figure()
    plt.bar(data.keys(), data.values())
    plt.show()


def key_func(k):
    return k['starter_level']

def key_func_type(k):
    return k['enc_pkm_types']

def key_func_enemy_level(k):
    return k['enc_pkm_level']


# sort INFO data by 'company' key.
def createLevel(data):
    B = sorted(data, key=key_func)
    res = {}
    for key, value in groupby(B, key_func):
        sameLevList = list(value)
        damagesList = [d['damages_within_battle'] for d in sameLevList]
        myList = ''.join(damagesList).replace('[', '').replace(']', ', ').split(', ')
        doubleDamage = [float(x) for x in myList[0:-1]]
        res[key] = np.mean(doubleDamage)

def createMatrixImage(data, tipi):
    length_types = len(tipi.index.values.tolist())
    matrix = np.full((length_types,20), np.nan)
    B = sorted(data, key=key_func_type)
    counter_type = 1
    types = []
    for key, value in groupby(B, key_func_type):
        valueList = list(value)
        B2 = sorted(valueList, key=key_func_enemy_level)
        for k, v in groupby(B2, key_func_enemy_level):
            sameLevList = list(v)
            length = len(sameLevList)
            bool_wins = (length - sum(x['defeated'] for x in sameLevList)) / length
            matrix[counter_type-1, k-1] = bool_wins
        counter_type +=1
        types.append(key)
    return matrix, types

def imagePlot(data, types):
    plt.subplots(1, 1, figsize=(10, 10))
    plt.imshow(data, cmap='jet')
    plt.xticks(np.arange(0,20), np.arange(1,21))
    plt.yticks(np.arange(0, len(types)), types)
    plt.colorbar()  # add the colorbar
    plt.show()



# pokemonsDf = pd.read_json('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/pokemons.json', lines=True, encoding="utf8")
# #print(pokemonsDf)
# movesDf = pd.read_json('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/moves.json', lines=True, encoding="utf8")
# #print(movesDf)
# effectivenessDf = pd.read_json('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/json_files/type_effectiveness.json', lines=True, encoding="utf8")
# #print(effectivenessDf)
#
# # load the data
# df = pd.read_csv('C:/Users/pelleli37768/OneDrive - Università degli Studi di Padova/DOTTORATO/Corsi dottorato/Python/python_course/fourth_hw/PokemonResult.csv')
pokemonsDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/pokemons.json', lines=True,
                          encoding="utf8")

# print(pokemonsDf)
movesDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/moves.json', lines=True,
                       encoding="utf8")

# print(movesDf)
effectivenessDf = pd.read_json(
    '/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/type_effectiveness.json', lines=True,
    encoding="utf8")

# print(effectivenessDf)

# load the data
df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fourth_hw/PokemonResult.csv')

# 1. Simple plot
# ans = pd.DataFrame(df['hps_within_battle'])
# refactored_type = ans.applymap(clean_up_df).applymap(divide_df)
# max_nturn = df['nturn'].max() + 1
# d_converted = double_converter(refactored_type, max_nturn)
# new_data = np.array(d_converted)
# simple_plot(new_data)


# 2. Pie Plot
# Bulbasaur
# pieplot_data1 = preprocessing_pie_plot('bulbasaur', df)
# pie_plot(pieplot_data1, 'Bulbasaur')

#
# # Charmander
# pieplot_data2 = preprocessing_pie_plot('charmander', df)
# pie_plot(pieplot_data2, 'Charmander')

#
# # Squirtle
# pieplot_data3 = preprocessing_pie_plot('squirtle', df)
# pie_plot(pieplot_data3, 'Squirtle')

# 2.2 pie plot
tipiRes = df['enc_pkm_types'].value_counts()
tipi = pokemonsDf['types'].value_counts()
# pie_plot2(tipi, tipiRes)


# 3. Bar chart
dfDict = df.to_dict('records')
bulbasaur = list(filter(lambda starter: starter['starter'] == 'bulbasaur', dfDict))
matrix, types = createMatrixImage(bulbasaur, tipiRes)
imagePlot(matrix, types)
# b_res = createLevel(bulbasaur)
# bar_chart(b_res)
#
# charmander = list(filter(lambda starter: starter['starter'] == 'charmander', dfDict))
# c_res = createLevel(charmander)
# bar_chart(c_res)
#
# squirtle = list(filter(lambda starter: starter['starter'] == 'squirtle', dfDict))
# s_res = createLevel(squirtle)
# bar_chart(s_res)

# 4. Image chart

print('')

