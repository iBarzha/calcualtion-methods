import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return 10*x - np.exp(-x)

def derivative(x):
    return 10 + np.exp(-x)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = 10*x_vals - np.exp(-x_vals)

plt.plot(x_vals, y_vals, label='10x - e^(-x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
