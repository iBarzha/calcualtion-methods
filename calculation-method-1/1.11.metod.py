import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return 1.8*x**2 - np.sin(10*x)

def derivative(x):
    return 3.6*x - 10*np.cos(10*x)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = 1.8*x_vals**2 - np.sin(10*x_vals)

plt.plot(x_vals, y_vals, label='1.8x^2 - sin(10x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
