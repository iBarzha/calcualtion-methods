import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

def equation(x):
    return 1/np.tan(x) - 1/x + x/2

def derivative(x):
    return -1/(np.sin(x)**2) + 1/(x**2) + 1/2

initial_guess = 1.0
tolerance = 1e-6
max_iterations = 1000

solution_newton = newton(equation, initial_guess, fprime=derivative, tol=tolerance, maxiter=max_iterations)

x_vals = np.linspace(0.01, 5, 100)
y_vals = 1/np.tan(x_vals) - 1/x_vals + x_vals/2

plt.plot(x_vals, y_vals, label='cot(x) - 1/x + x/2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

print(f"Метод Ньютона: Решение {solution_newton}")
