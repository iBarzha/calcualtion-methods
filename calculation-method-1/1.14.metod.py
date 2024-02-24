import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return x**x + 5*x - 1000

def derivative(x):
    return x**x * (1 + np.log(x)) + 5

initial_guess = 2.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(2, 10, 100)
y_vals = x_vals**x_vals + 5*x_vals - 1000

plt.plot(x_vals, y_vals, label='x^x + 5x - 1000')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
