import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return np.cos(x**2-2)/(3*x+1) - (x**2-1.5)

def derivative(x):
    numerator = -2*x*np.sin(x**2-2) - np.cos(x**2-2)*(3*x+1)
    denominator = (3*x+1)**2
    return numerator / denominator - 2*x

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(-2, 2, 100)
y_vals = np.cos(x_vals**2-2)/(3*x_vals+1) - (x_vals**2-1.5)

plt.plot(x_vals, y_vals, label='cos(x^2-2)/(3x+1) - (x^2-1.5)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
