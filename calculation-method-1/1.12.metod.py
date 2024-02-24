import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return 3*x - np.cos(x) - 1

def derivative(x):
    return 3 + np.sin(x)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = 3*x_vals - np.cos(x_vals) - 1

plt.plot(x_vals, y_vals, label='3x - cos(x) - 1')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
