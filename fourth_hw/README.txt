GROUP #15

MICHELE ATZENI - Bioengineering
ELENA IDI - Bioengineering
ELISA PELLIZZARI - Bioengineering

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MAIN DESCRIPTION
The code first imports a number of Python libraries, including:

* `pandas` for loading and manipulating dataframes
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

* The code uses the `pandas` library to load and manipulate dataframes. This allows the code to store and access data about Pokémon, moves, and types in a structured way.
* The code uses the `json_handler` library to load and parse JSON files. This allows the code to load data about Pokémon, moves, and types from external files.
* The code uses the `FiniteStateMachine` library to represent finite state machines. A finite state machine is a model of a system that can be in a number of different states. The states of the finite state machine in this code represent the different things that the trainer can do in the game, such as exploring the world, battling wild Pokémon, and visiting Pokémon Centers.
* The code uses the `Trainer` class to represent a Pokémon trainer. A Pokémon trainer is a character in the game that can collect Pokémon, battle wild Pokémon, and visit Pokémon Centers.
* The code uses the `Battle` class to represent a Pokémon battle. A Pokémon battle is a contest between two Pokémon trainers. The outcome of a battle is determined by the stats of the Pokémon involved and the moves that they use.

VISUALIZATION DESCRIPTION
Python script that analyzes data from a Pokémon battle simulation. The script first loads the data from three JSON files: `pokemons.json`, `moves.json`, and `type_effectiveness.json`. It then loads the data from a CSV file called `PokemonResult.csv`.

The script then performs four different analyses of the data:

1. A simple plot that shows the average reduction in the percentage of the player's Pokémon's health over the course of a battle.
2. Three pie charts that show the distribution of the types of Pokémon used by the player, the enemy, and the Pokémon that defeated the enemy.
3. Three bar charts that show the average damage done by the player's Pokémon at different levels.
4. Three image charts that show the percentage of victories as a function of the enemy's type and level for each of the three starter Pokémon.


