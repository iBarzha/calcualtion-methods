import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def f(x):
    return x**3 + x**2 - 5*x + 2

def f_prime(x):
    return 3*x**2 + 2*x - 5

def iteration_method(initial_guess, tolerance, max_iterations):
    x_values = [initial_guess]
    for i in range(max_iterations):
        x_next = x_values[-1] - f(x_values[-1]) / f_prime(x_values[-1])
        if abs(x_next - x_values[-1]) < tolerance:
            return x_next, i+1, x_values
        x_values.append(x_next)
    return None, max_iterations, x_values

def plot_iteration(iteration_values, method_name):
    plt.plot(range(len(iteration_values)), iteration_values, label=method_name)
    plt.xlabel('Iteration')
    plt.ylabel('Approximation')
    plt.title(f'{method_name} Iterations')
    plt.legend()
    plt.show()

def plot_function():
    x = np.linspace(-3, 3, 100)
    y = f(x)
    plt.plot(x, y, label='x^3 + x^2 - 5x + 2')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

initial_guess = 0.0
tolerance = 1e-6
max_iterations = 1000

solution_newton, iterations_newton, newton_values = iteration_method(initial_guess, tolerance, max_iterations)
plot_iteration(newton_values, 'Newton')

plot_function()

if solution_newton is not None:
    print(f"Метод Ньютона: Решение {solution_newton} найдено за {iterations_newton} итераций.")
else:
    print("Метод Ньютона не сошелся.")
