import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x):
    result = 0
    for i in range(len(y_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

# Задані дані
a = 0
b = 6
h = (b - a) / 7  # Змінив кількість вузлів для збігу розмірів масивів
x_nodes = np.arange(a, b + h, h)
y_nodes = np.array([0, 67, 101, 168, 202, 310, 334, 404])

# Розрахунок значень функції у вузлах інтерполяції
y_interpolated = [lagrange_interpolation(x_nodes, y_nodes, x) for x in x_nodes]

# Побудова графіка
plt.scatter(x_nodes, y_nodes, label='Експериментальні точки')
plt.plot(x_nodes, y_interpolated, 'r', label='Поліном Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Інтерполяція поліномом Лагранжа')
plt.grid(True)
plt.show()
