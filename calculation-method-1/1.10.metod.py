import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return x + np.sqrt(x) + np.power(x, 1/3) + np.power(x, 1/4) - 5

def derivative(x):
    return 1 + 0.5/np.sqrt(x) + (1/3)*np.power(x, -2/3) + (1/4)*np.power(x, -3/4)

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(0.01, 10, 100)
y_vals = x_vals + np.sqrt(x_vals) + np.power(x_vals, 1/3) + np.power(x_vals, 1/4) - 5

plt.plot(x_vals, y_vals, label='x + sqrt(x) + x^(1/3) + x^(1/4) - 5')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
