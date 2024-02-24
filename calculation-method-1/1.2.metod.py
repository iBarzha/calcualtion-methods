import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return 2*x - np.log(x) - 4

def iteration_method(initial_guess, tolerance, max_iterations):
    x_values = [initial_guess]
    for i in range(max_iterations):
        x_next = np.log(x_values[-1]/2 + 2)
        if abs(x_next - x_values[-1]) < tolerance:
            return x_next, i+1, x_values
        x_values.append(x_next)
    return None, max_iterations, x_values

def bisection_method(a, b, tolerance, max_iterations):
    if f(a) * f(b) > 0:
        return None, max_iterations, []

    x_values = []
    for i in range(max_iterations):
        c = (a + b) / 2
        x_values.append(c)
        if abs(f(c)) < tolerance:
            return c, i+1, x_values
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return None, max_iterations, x_values

def plot_iteration(iteration_values, method_name):
    plt.plot(range(len(iteration_values)), iteration_values, label=method_name)
    plt.xlabel('Iteration')
    plt.ylabel('Approximation')
    plt.title(f'{method_name} Iterations')
    plt.legend()
    plt.show()

def plot_function():
    x = np.linspace(0.1, 3, 100)
    y = f(x)
    plt.plot(x, y, label='2x - ln(x) - 4')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

initial_guess = 1.0
a = 0.1
b = 3.0
tolerance = 1e-6
max_iterations = 1000

solution_iteration, iterations_iteration, iteration_values = iteration_method(initial_guess, tolerance, max_iterations)
plot_iteration(iteration_values, 'Iteration')

solution_bisection, iterations_bisection, bisection_values = bisection_method(a, b, tolerance, max_iterations)
plot_iteration(bisection_values, 'Bisection')

plot_function()

integral_value, _ = quad(f, a, b)
print(f"Значение интеграла: {integral_value}")

if solution_iteration is not None:
    print(f"Метод итераций: Решение {solution_iteration} найдено за {iterations_iteration} итераций.")
else:
    print("Метод итераций не сошелся.")

if solution_bisection is not None:
    print(f"Метод бисекции: Решение {solution_bisection} найдено за {iterations_bisection} итераций.")
else:
    print("Метод бисекции не сошелся.")
