import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return x**2 - np.sin(5*x)

def derivative(x):
    return 2*x - 5*np.cos(5*x)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = x_vals**2 - np.sin(5*x_vals)

plt.plot(x_vals, y_vals, label='x^2 - sin(5x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
