GROUP #15

MICHELE ATZENI - Bioengineering
ELENA IDI - Bioengineering
ELISA PELLIZZARI - Bioengineering

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MAIN DESCRIPTION
The code first imports a number of Python libraries, including:

* `json_handler` for loading and parsing JSON files
* `FiniteStateMachine` for representing finite state machines
* `Trainer` for representing a Pokémon trainer
* `Battle` for representing a Pokémon battle
* `pickle` for saving and loading data

The code then defines a number of functions for creating and managing Pokémon trainers, battles, and finite state machines. These functions are:

* `main()`: The main function of the program. This function creates a finite state machine, initializes it, and then runs it for a number of games.
* `create_character()`: This function creates a new Pokémon trainer.
* `battle()`: This function simulates a Pokémon battle.
* `finite_state_machine()`: This function represents a finite state machine.

The code then runs a simulation of a number of Pokémon games. In each game, the trainer starts with a randomly selected starter Pokémon and then explores the world, battling wild Pokémon and visiting Pokémon Centers. The results of each game are saved to a file.
Here are some additional details about the code:

* The code uses the `json_handler` library to load and parse JSON files that contain information about Pokémon, moves, and types.
* The code uses the `FiniteStateMachine` library to represent finite state machines. A finite state machine is a model of a system that can be in a number of different states. The states of the finite state machine in this code represent the different things that the trainer can do in the game, such as exploring the world, battling wild Pokémon, and visiting Pokémon Centers.
* The code uses the `Trainer` class to represent a Pokémon trainer. A Pokémon trainer is a character in the game that can collect Pokémon, battle wild Pokémon, and visit Pokémon Centers.
* The code uses the `Battle` class to represent a Pokémon battle. A Pokémon battle is a contest between two Pokémon trainers. The outcome of a battle is determined by the stats of the Pokémon involved and the moves that they use.

VISUALIZATION DESCRIPTION
The code first imports the following Python libraries:

* `pickle` for loading and saving data
* `matplotlib` for creating and displaying plots
* `numpy` for working with numerical data
* `statistics` for calculating statistical measures

The code then defines a number of functions for processing the data and creating the plots. These functions are:

* `processing_simple_plot()`: This function takes a starter Pokémon name and a data set as input, and it creates a line plot showing the number of wins as a function of the number of games played.
* `processing_box_plot()`: This function takes a starter Pokémon name and a data set as input, and it creates a box plot showing the distribution of the number of turns and the percentage of health remaining for each game.
* `processing_bar_chart()`: This function takes a starter Pokémon name and a data set as input, and it creates a bar chart showing the percentage of wins against each opponent Pokémon.
* `processing_m_and_std_bar_chart()`: This function takes a starter Pokémon name and a data set as input, and it creates a bar chart showing the mean and standard deviation of the percentage of wins against each opponent Pokémon.

The main part of the code then loads the data from a file, and it calls the functions above to create the plots. The plots are then displayed in the console.