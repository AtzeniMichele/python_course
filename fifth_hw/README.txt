GROUP #15

MICHELE ATZENI - Bioengineering
ELENA IDI - Bioengineering
ELISA PELLIZZARI - Bioengineering

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MAIN DESCRIPTION
The main.py is the script from which the dataset to train the ML is created. The main_final.py is the final game engine that uses the ML model. Below the description of the main_final.py:
The main() function is the main entry point of the program. It initializes the game by loading the moves, Pokémon, and effectiveness dataframes. It also loads the machine learning model and initializes the game variables.
The main() function then enters a loop where it repeatedly prompts the user to choose an action. The possible actions are to go to the Pokémon store, go to the Pokémon center, explore, or exit the game.
If the user chooses to explore, the main() function simulates a battle between the player's Pokémon and a wild Pokémon. The battle is simulated using the machine learning model that suggest if at least one of our pokemons has at least 50% of chance of winning.
After the battle, the main() function prompts the user to choose an action again. The loop continues until the user chooses to exit the game.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BATTLE DESCRIPTION
The `Battle` class inherits from the `State` class, which is a base class for all states in the game. The `Battle` class has a number of methods, including `run()`, `update()`, `__str__()`, and `repr()`.
The `run()` method is the main method of the `Battle` class. This method simulates a battle between a trainer's Pokémon and a wild Pokémon. The method takes two arguments: a list of Pokémon and a dictionary of effectiveness values. The method returns a boolean value indicating whether the trainer's Pokémon won the battle.
The `update()` method is used to update the state of the battle. This method is called after each turn in the battle.
The `__str__()` method returns a string representation of the `Battle` object.
The `repr()` method returns a more detailed representation of the `Battle` object.
The `Battle` class also defines a number of other methods, such as `choosePokemon()` and `useMove()`. These methods are used to handle the specific actions that can be taken during a battle.

The pokemon recommender system (lines 48-92) from the battle.py file:
The system uses a random forest model to predict the probability of a Pokémon winning a battle against a wild Pokémon. The system then suggests the Pokémon with the highest predicted probability of winning.
The code first creates a DataFrame for each Pokémon. The DataFrame includes the Pokémon's stats, such as its HP, attack, defense, and speed. The DataFrame also includes the Pokémon's types.
The code then uses the random forest model to predict the probability of each Pokémon winning a battle against the wild Pokémon. The model is trained on a dataset of previous battles.
The code then suggests the Pokémon with the highest predicted probability of winning. If the predicted probability is greater than 0.5, the trainer battle the wild Pokémon. Otherwise, the trainer run away from the wild Pokémon.


Some additional comments about the code:

* The code uses a number of Python libraries, such as `pandas`, `random`, and `copy`. These libraries are used to implement the battle system.
* The code uses a dictionary to store the effectiveness values for different types of Pokémon. This dictionary is used to determine how much damage is dealt in a battle.
* The code uses a loop to simulate the turns in a battle. The loop continues until one of the Pokémon is defeated.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
PREPROCESSING DESCRIPTION
Script that preprocesses a dataset of Pokémon battle results. The script first loads the dataset from a CSV file.
The script then performs the following preprocessing steps:

* It drops the `n_game`, `starter`, `nbattle`, `enc_pkm`, and `nturn` columns, as these columns are not relevant to the outcome of the battle.
* It uses a one-hot encoding to convert the `player_types` and `opponent_types` columns into binary vectors.
* It saves the preprocessed dataset to two CSV files: `RefactoredIndependentPokemonResult.csv` and `RefactoredOutcomePokemonResult.csv`.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MODEL TRAINING DESCRIPTION
Script that trains a random forest classifier to predict whether a Pokémon will be defeated in battle. The script first loads the outcome and independent variables from two CSV files. The outcome variable is whether the Pokémon was defeated in battle, and the independent variables are the Pokémon's stats and types.

The script then splits the data into a training set and a test set. The training set is used to train the random forest classifier, and the test set is used to evaluate the performance of the classifier.

The random forest classifier is trained using the `RandomForestClassifier()` class from the `sklearn.ensemble` library. The classifier is configured with a default set of parameters.

The performance of the classifier is evaluated using the `accuracy_score()` and `roc_auc_score()` functions from the `sklearn.metrics` library.

The script also saves the trained classifier to a file using the `joblib` library. The file can be loaded later to make predictions on new data.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
