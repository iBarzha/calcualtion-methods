import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return (x**2 - 3.6*x) * np.log(1/x) - 1.3

def derivative(x):
    term1 = (2*x - 3.6) * np.log(1/x)
    term2 = - (x**2 - 3.6*x) / (x**2)
    return term1 + term2

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(0.01, 3, 100)
y_vals = (x_vals**2 - 3.6*x_vals) * np.log(1/x_vals) - 1.3

plt.plot(x_vals, y_vals, label='(x^2-3.6x)ln(1/x) - 1.3')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
