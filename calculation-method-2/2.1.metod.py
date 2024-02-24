import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція, яку інтегруємо
def f(x):
    return 1 / np.sqrt(2*x**2 + 1)

# Аналітичне значення інтегралу (для порівняння)
analytical_value = spi.quad(f, 0.8, 1.6)[0]

# Метод прямокутників
def rectangle_method(f, a, b, N):
    h = (b - a) / N
    x_values = np.linspace(a, b, N)
    integral_value = h * np.sum(f(x_values))
    return integral_value

# Метод трапецій
def trapezoidal_method(f, a, b, N):
    h = (b - a) / N
    x_values = np.linspace(a, b, N + 1)
    integral_value = h * (np.sum(f(x_values)) - 0.5 * (f(a) + f(b)))
    return integral_value

# Метод Монте-Карло
def monte_carlo_method(f, a, b, N):
    x_random = np.random.uniform(a, b, N)
    integral_value = (b - a) * np.mean(f(x_random))
    return integral_value

# Задані межі інтегрування
a = 0.8
b = 1.6

# Значення N для розбиття інтервалу
N_values = [10, 20, 50, 100, 1000]

# Виведення результатів в таблиці та графіках
print(f"{'N': <6} {'Аналіт.': <15} {'Прямокутники': <15} {'Трапеції': <15} {'Монте-Карло': <15}")
print("="*75)

for N in N_values:
    rectangle_result = rectangle_method(f, a, b, N)
    trapezoidal_result = trapezoidal_method(f, a, b, N)
    monte_carlo_result = monte_carlo_method(f, a, b, N)

    print(f"{N:<6} {analytical_value:<15.6f} {rectangle_result:<15.6f} {trapezoidal_result:<15.6f} {monte_carlo_result:<15.6f}")

# Графічне представлення
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='$\\frac{1}{\sqrt{2x^2 + 1}}$')
plt.fill_between(x_vals, y_vals, alpha=0.2, color='gray', label='Площа під кривою')

plt.title('Графічне представлення інтегралу')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
