import pickle
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clean_up_df(data):
    return data.replace('[', '').replace(']', '').replace("'", '')


def divide_df(data):
    return np.array(str(data).split(', '))

def double_converter(data, max):
    floats = []
    for _ ,line in data.iterrows():
        tmp = [float(x) for x in line[0]]
        if max - len(tmp) > 0:
            zeros = np.zeros(max - len(tmp)).tolist()
            tmp.extend(zeros)
        floats.append(tmp)
    return floats

def simple_plot(data):
    y = np.mean(data, axis = 0)
    x = np.arange(1,len(y)+1)
    e = np.std(data, axis=0)
    yerr0 = y - e
    yerr1 = y + e

    fig, ax = plt.subplots()
    ax.plot(x, y, color='C1')
    plt.fill_between(x, yerr0, yerr1, color='C0', alpha=0.5)
    plt.show()

pokemonsDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/pokemons.json', lines=True)
print(pokemonsDf)
movesDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/moves.json', lines=True)
print(movesDf)
effectivenessDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/type_effectiveness.json', lines=True)
print(effectivenessDf)

# load the data
df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fourth_hw/PokemonResult.csv')
ans = pd.DataFrame(df['hps_within_battle'])
refactored_type = ans.applymap(clean_up_df).applymap(divide_df)
max_nturn = df['nturn'].max()
d_converted = double_converter(refactored_type, max_nturn)
new_data = np.array(d_converted)

# 1. Simple plot
simple_plot(new_data)

# 3. Bar chart
# TODO add pokemon level to the saved results

