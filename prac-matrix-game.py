import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

def nash_equilibrium(a):
    num_rows, num_cols = a.shape

    c1 = np.ones(num_rows)
    A1 = -a.T
    b1 = -np.ones(num_cols)

    c2 = -np.ones(num_cols)
    A2 = a
    b2 = np.ones(num_rows)

    result1 = linprog(c1, A_ub=A1, b_ub=b1)
    result2 = linprog(c2, A_ub=A2, b_ub=b2)

    value = 1 / result1.fun
    strategy_player1 = result1.x / np.sum(result1.x)
    strategy_player2 = result2.x / np.sum(result2.x)

    return value, strategy_player1, strategy_player2

def plot_strategy_spectrum(strategies, title, player_number):
    num_strategies = len(strategies)
    x_labels = [str(i+1) for i in range(num_strategies)]
    plt.scatter(range(num_strategies), strategies, label=f'Player {player_number}', marker='o')
    plt.title(title)
    plt.xlabel("Pure Strategies")
    plt.ylabel("Strategy Probabilities")
    plt.xticks(range(num_strategies), x_labels)
    plt.legend()

def print_game_values(value, strategy_player1, strategy_player2):
    print(f"Value of the game: {value}")
    print(f"Optimal strategies for Player 1: {strategy_player1}")
    print(f"Optimal strategies for Player 2: {strategy_player2}")

game = np.array([[4, 0, 6, 2, 2, 1], 
                 [3, 8, 4, 10, 4, 4], 
                 [1, 2, 6, 5, 0, 0],
                 [6, 6, 4, 4, 10, 3], 
                 [10, 4, 6, 4, 0, 9], 
                 [10, 7, 0, 7, 9, 8]])

value, strategy_player1, strategy_player2 = nash_equilibrium(game)

print_game_values(value, strategy_player1, strategy_player2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plot_strategy_spectrum(strategy_player1, "Game: Full Spectrum of Optimal Play", 1)

plt.subplot(1, 2, 2)
plot_strategy_spectrum(strategy_player2, "Game: Full Spectrum of Optimal Play", 2)

plt.show()
