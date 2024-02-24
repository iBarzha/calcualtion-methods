import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return x * np.tanh(x) - 1

def derivative(x):
    return np.tanh(x) + x * (1 / np.cosh(x))**2

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-3, 3, 100)
y_vals = x_vals * np.tanh(x_vals) - 1

plt.plot(x_vals, y_vals, label='xtanh(x) - 1')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
