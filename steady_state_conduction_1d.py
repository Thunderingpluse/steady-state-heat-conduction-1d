import numpy as np
import matplotlib.pyplot as plt

def solve_heat_conduction():
    print(" ")
    print("1D Steady State Heat Conduction Solver")
    
    # Inputs
    try:
        length = float(input("Enter rod length L (m): "))
        n_div = int(input("Enter number of divisions (n_div): "))
        t_left = float(input("Enter left boundary temperature T0: "))
        t_right = float(input("Enter right boundary temperature Tn: "))
        k = float(input("Enter thermal conductivity k (W/mK): "))
        g_dot = float(input("Enter volumetric heat generation g (W/m^3): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Parameters
    n_nodes = n_div + 1
    dx = length / n_div
    rhs_value = -(g_dot * dx**2) / k  # The constant on the Right Hand Side
    print("\nComputed Parameters:")
    print(f"dx = {dx:g}")
    print(f"Number of nodes = {n_nodes}")
    print(f"Internal nodes = {n_nodes - 2}\n")

    # Build Matrix A and Vector B
    A = np.zeros((n_nodes, n_nodes))
    B = np.zeros(n_nodes)

    # Boundary Conditions
    A[0, 0] = 1
    B[0] = t_left
    
    A[-1, -1] = 1
    B[-1] = t_right

    # Interior Nodes
    for i in range(1, n_nodes - 1):
        A[i, i-1] = 1
        A[i, i]   = -2
        A[i, i+1] = 1
        B[i]      = rhs_value

    # Print Equations
    print("Generated Finite Difference Equations:\n")
    eq_rhs = (g_dot * dx**2) / k
    for i in range(1, n_nodes - 1):
        left_term = f"{t_left}" if i == 1 else f"T{i-1}"
        right_term = f"{t_right}" if i == n_nodes - 2 else f"T{i+1}"
        print(f"Node {i}: -({left_term}) + 2*T{i} - ({right_term}) = {eq_rhs:.3f}")
    print("")

    # Print Matrix and Vector
    print("Matrix A and Vector B")
    for i in range(n_nodes):
        if n_nodes > 6 and 3 <= i < n_nodes - 3:
            if i == 3: print("  [" + " "*22 + "  ...  " + " "*22 + "]    [   ...  ]")
            continue
        row_str = "  ".join(f"{x:6.1f}" for x in A[i]) if n_nodes <= 6 else \
                  f"{'  '.join(f'{x:6.1f}' for x in A[i, :3])}  ...  {'  '.join(f'{x:6.1f}' for x in A[i, -3:])}"
        print(f"  [{row_str}]    [{B[i]:8.1f}]")
    print("")

    # Solve
    try:
        T = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Error: Matrix is singular.")
        return

    print("Final Results")
    for i in range(n_nodes):
        print(f"Node {i}: {T[i]:.2f} C")

    # Plotting
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 14
    x_values = np.linspace(0, length, n_nodes)
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, T, 'o-', linewidth=2, label=f'Gen={g_dot:.0e}')
    plt.title(f'Temperature Distribution (Nodes={n_nodes})', weight='bold')
    plt.xlabel('Position x (m)', weight='bold')
    plt.ylabel('Temperature (C)', weight='bold')
    plt.grid(True, linestyle='--')
    plt.show()

if __name__ == "__main__":
    solve_heat_conduction()
    