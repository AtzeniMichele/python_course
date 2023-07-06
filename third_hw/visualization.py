import pickle
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import statistics


def processing_simple_plot(pkm_name, input_data):
    subset = []
    for i, line in enumerate(input_data):
        if line['starter'] == pkm_name:
            subset.append(line)

    plot1_data = {}
    for i in subset:
        if i['n_game'] in plot1_data:
            # add to already existing key
            if not i['defeated']:
                plot1_data[i['n_game']] = plot1_data[i['n_game']] + 1
        else:
            # create new key, then add
            plot1_data[i['n_game']] = 0
            if not i['defeated']:
                plot1_data[i['n_game']] = plot1_data[i['n_game']] + 1
    return plot1_data


def processing_box_plot(pkm_name, input_data):
    subset = []
    for i, line in enumerate(input_data):
        if line['starter'] == pkm_name:
            subset.append(line)

    nturn_plot2_data = []
    hp_plot2_data = []
    for i in subset:
        nturn_plot2_data.append(i['nturn'])
        hp_plot2_data.append((i['hp_perc']))
    return nturn_plot2_data, hp_plot2_data


def processing_bar_chart(pkm_name, input_data):
    subset = []
    for i, line in enumerate(input_data):
        if line['starter'] == pkm_name:
            subset.append(line)

    plot3_data = {}
    for i in subset:
        if i['enc:pkm'] in plot3_data:
            # add to already existing key
            counter = plot3_data[i['enc:pkm']][0] + 1
            wins = plot3_data[i['enc:pkm']][1]
            if not i['defeated']:
                wins += 1
            plot3_data[i['enc:pkm']] = [counter, wins]
        else:
            # create new key, then add
            wins = 0
            if not i['defeated']:
                wins = 1
            plot3_data[i['enc:pkm']] = [1, wins]
    names = []
    percenentages = []
    for k, v in plot3_data.items():
        names.append(k)
        percenentages.append(v[1] / v[0] * 100)
    return plot3_data, names, percenentages


def processing_m_and_std_bar_chart(pkm_name, input_data):
    subset = []
    for i, line in enumerate(input_data):
        if line['starter'] == pkm_name:
            subset.append(line)

    plot3_data = {}
    for i in subset:
        if i['enc:pkm'] in plot3_data:
            # add to already existing key
            if i['hp_perc'] >= 0:
                plot3_data[i['enc:pkm']].append(i['hp_perc'])
            else:
                plot3_data[i['enc:pkm']].append(0.0)
            # print(plot3_data)
        else:
            # create new key, then add
            # print(i['enc:pkm'])
            # print(i['hp_perc'])
            # print('---------')
            if i['hp_perc'] >= 0:
                plot3_data[i['enc:pkm']] = [i['hp_perc']]
            else:
                plot3_data[i['enc:pkm']] = [0.0]

    names = []
    means = []
    stds = []
    for k, v in plot3_data.items():
        names.append(k)
        means.append(sum(v) / len(v))
        if len(v) > 1:
            stds.append(statistics.stdev(v))
        else:
            stds.append(0)
    return plot3_data, names, means, stds


def simple_plot(result, pkmName):
    wins = list(result.values())
    n_battles = list(result.keys())
    result_mean = sum(wins) / len(wins)

    plt.figure()
    plt.plot(n_battles, wins, 'o')
    plt.plot(n_battles, np.repeat(result_mean, len(n_battles)))
    plt.title('Simple plot ' + pkmName)
    plt.xlabel('# of games')
    plt.ylabel('# of wins')
    plt.show()


def box_plot(nturn_result, hp_results, pkmNameList):
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    positions = np.arange(3) + 1
    bp = ax[0].boxplot(nturn_result, positions=positions, showmeans=True)
    ax[0].set_title('Boxplot nturn')
    ax[0].set_xlabel('Pokemon')
    ax[0].set_ylabel('nturn distribution')
    ax[0].set_xticklabels(pkmNameList)

    bp = ax[1].boxplot(hp_results, positions=positions, showmeans=True)
    ax[1].set_title('Boxplot hp')
    ax[1].set_xlabel('Pokemon')
    ax[1].set_ylabel('hp distribution')
    ax[1].set_xticklabels(pkmNameList)

    plt.savefig('box_plot.png')
    plt.show()


def bar_chart(names, percentages, pkmName):
    plt.figure()
    plt.barh(names, percentages)
    plt.title('Bar chart ' + pkmName)
    plt.ylabel('Encountered pokemons')
    plt.xlabel('% of wins')
    plt.show()


def errorbar_chart(names, means,stds, pkmName):
    plt.figure()
    plt.barh(names, means, xerr=stds, alpha=0.5, capsize=5)
    plt.title('Bar chart ' + pkmName)
    plt.ylabel('Encountered pokemons')
    plt.xlabel('mean of wins')
    plt.show()


### main
pickle_in = open("pokemon_game_results2.p", "rb")
data = pickle.load(pickle_in)

# 1. lineplot

# bulbasaur
b_plot1_data = processing_simple_plot('bulbasaur', data)
simple_plot(b_plot1_data, 'bulbasaur')
# # charmander
c_plot1_data = processing_simple_plot('charmander', data)
simple_plot(c_plot1_data, 'charmander')
# # squirtle
s_plot1_data = processing_simple_plot('squirtle', data)
simple_plot(s_plot1_data, 'squirtle')

# 2. box plot
nturn_b_plot2_data, hp_b_plot2_data  = processing_box_plot('bulbasaur', data)
nturn_c_plot2_data, hp_c_plot2_data  = processing_box_plot('charmander', data)
nturn_s_plot2_data, hp_s_plot2_data  = processing_box_plot('squirtle', data)
box_plot([nturn_b_plot2_data, nturn_c_plot2_data, nturn_s_plot2_data], [hp_b_plot2_data, hp_c_plot2_data, hp_s_plot2_data], ['Bulbasaur', 'Charmander', 'Squirtle'])
print('done')

# 3. bar charts
# pt 1
b_plot3_data, b_names, b_percentages = processing_bar_chart('bulbasaur', data)
bar_chart(b_names, b_percentages, 'bulbasaur')
#
c_plot3_data, c_names, c_percentages = processing_bar_chart('charmander', data)
bar_chart(c_names, c_percentages, 'charmander')
#
s_plot3_data, s_names, s_percentages = processing_bar_chart('squirtle', data)
bar_chart(s_names, s_percentages, 'squirtle')


# pt 2
b2_plot3_data, b2_names, b2_means, b2_stds = processing_m_and_std_bar_chart('bulbasaur', data)
errorbar_chart(b2_names, b2_means, b2_stds, 'bulbasaur')

c2_plot3_data, c2_names, c2_means, c2_stds = processing_m_and_std_bar_chart('charmander', data)
errorbar_chart(c2_names, c2_means, c2_stds, 'charmander')

s2_plot3_data, s2_names, s2_means, s2_stds = processing_m_and_std_bar_chart('squirtle', data)
errorbar_chart(s2_names, s2_means, s2_stds, 'squirtle')
