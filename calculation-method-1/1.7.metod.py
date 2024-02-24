import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return np.exp(x) + np.exp(-3*x) - 4

def derivative(x):
    return np.exp(x) - 3*np.exp(-3*x)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = np.exp(x_vals) + np.exp(-3*x_vals) - 4

plt.plot(x_vals, y_vals, label='e^x + e^(-3x) - 4')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
