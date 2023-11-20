import numpy as np
from scipy.optimize import linprog

def nash_equilibrium_modified(a):
    num_rows, num_cols = a.shape

    for i in range(num_rows):
        for j in range(num_cols):
            row_best_response = a[i,j] >= a[:,j]
            col_best_response = a[i,j] >= a[i,:]

            if all(row_best_response) and all(col_best_response):
                value = a[i,j]
                strategy_player1 = np.zeros(num_rows)
                strategy_player2 = np.zeros(num_cols)
                strategy_player1[i] = 1
                strategy_player2[j] = 1
                return value, strategy_player1, strategy_player2

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

def test_nash_equilibrium(game_matrix, case_description, equilibrium_function):
    result = equilibrium_function(game_matrix)
    
    print(f"{case_description}:")
    print("Game Matrix:")
    print(game_matrix)
    print("Nash Equilibrium Result:")
    print("Game Value:", result[0])
    print("Player 1 Optimal Strategy:", result[1])
    print("Player 2 Optimal Strategy:", result[2])
    print("\n")

# Примеры игр для тестирования
game1 = np.array([[1, -1], [-1, 1]])
game2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
game3 = np.array([[1, 2], [0, 1]])


test_nash_equilibrium(game1, "Case 1 - Single-point Spectrum (Modified)", nash_equilibrium_modified)
test_nash_equilibrium(game2, "Case 2 - Incomplete Spectrum (Modified)", nash_equilibrium_modified)
test_nash_equilibrium(game3, "Case 3 - Complete Spectrum (Modified)", nash_equilibrium_modified)
