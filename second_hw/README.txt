GROUP #15

MICHELE ATZENI - Bioengineering
ELENA IDI - Bioengineering
ELISA PELLIZZARI - Bioengineering

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
MAIN DESCRIPTION 

This Python code defines a simple text-based game using a Finite State Machine (FSM) to manage different game states.

Here's a breakdown of the code:

1. Import Statements:
   The code imports various modules and classes needed for the game, including:
   - Modules: `engine.story`, `engine.create_character`, `engine.actions`, `engine.battle`, `engine.exit`, and `pokemon.trainer`.
   - Classes: `FiniteStateMachine` and `Trainer`.

2. `main()` Function:
   This function serves as the entry point to the game. It initializes the Finite State Machine, adds different states, sets transitions between states, and starts the game loop. The game loop allows the player to interact with the game by choosing different actions, such as going to a Pokémon Store, a Pokémon Center, exploring, or exiting the game.

3. Finite State Machine (FSM):
   The `FiniteStateMachine` class is used to manage the different states of the game. The states include:
   - `cc`: The initial state, which appears to represent character creation (possibly for creating a new game or character).
   - `story`: The main story state, where most of the gameplay takes place.
   - `pokemonStore`: State for accessing a Pokémon Store.
   - `pokemonCenter`: State for accessing a Pokémon Center.
   - `explore`: State for exploring the game world.
   - `battle`: State for engaging in a battle with Pokémon.
   - `close`: The final state, which represents exiting the game.

4. Transitions:
   The code defines transitions between states using `machine.add_transition()` function. For example, from `cc`, the player transitions to `story` state to begin the main story. From `story`, the player can go to other states like `pokemonStore`, `pokemonCenter`, or `explore`, and then return to the `story` state.

5. Game Loop:
   The game loop allows the player to keep making choices until they choose to exit the game. The available choices are printed on the screen, and the player can input their choice using an integer.

6. Player Actions:
   Based on the player's input, different actions are executed. For example, if the player chooses to go to the Pokémon Store, they enter the `pokemonStore` state, perform actions there (which may include interacting with Pokémon or buying items), and then return to the `story` state.

7. Pokémon Battles:
   The game features a Pokémon battles. When exploring (`explore` state), if the player encounters a battle (`explore.battle` is true), they can enter the `battle` state, select Pokémon and moves, and proceed with the battle. If the player's Pokémon is defeated, they are taken to a Pokémon Center (`pokemonCenter` state) to heal their Pokémon.
