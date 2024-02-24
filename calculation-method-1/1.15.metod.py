import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return np.log(x+1)/(x-1) - 2*x

def derivative(x):
    return (1/(x-1) - np.log(x+1)/((x-1)**2)) - 2

initial_guess = 2.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(1.1, 5, 100)
y_vals = np.log(x_vals+1)/(x_vals-1) - 2*x_vals

plt.plot(x_vals, y_vals, label='ln(x+1)/(x-1) - 2x')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
