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
        if line[0][0]=='':
            tmp = [100.0]
        else:
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


def preprocessing_pie_plot(pkm_name, input_data):
    subset = []
    for i, line in input_data.iterrows():
        if line['starter'] == pkm_name:
            subset.append(line)

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

def pie_plot(data):
    fig = plt.figure()
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.show()
    return plt

pokemonsDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/pokemons.json', lines=True, encoding="utf8")
#print(pokemonsDf)
movesDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/moves.json', lines=True, encoding="utf8")
#print(movesDf)
effectivenessDf = pd.read_json('/Users/micheleatzeni/Desktop/python course/fourth_hw/json_files/type_effectiveness.json', lines=True, encoding="utf8")
#print(effectivenessDf)

# load the data
df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fourth_hw/PokemonResult.csv')


# 1. Simple plot
ans = pd.DataFrame(df['hps_within_battle'])
refactored_type = ans.applymap(clean_up_df).applymap(divide_df)
max_nturn = df['nturn'].max()
d_converted = double_converter(refactored_type, max_nturn)
new_data = np.array(d_converted)
simple_plot(new_data)


# 2. Pie Plot
# Bulbasaur
pieplot_data1 = preprocessing_pie_plot('bulbasaur', df)
plt = pie_plot(pieplot_data1)
plt.title('Bulbasaur')

# Charmander
pieplot_data2 = preprocessing_pie_plot('charmander', df)
plt = pie_plot(pieplot_data2)
plt.title('Charmander')

# Squirtle
pieplot_data3 = preprocessing_pie_plot('squirtle', df)
plt = pie_plot(pieplot_data3)
plt.title('Squirtle')


# 3. Bar chart
