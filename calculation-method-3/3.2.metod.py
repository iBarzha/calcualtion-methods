import numpy as np
import matplotlib.pyplot as plt

# Задані дані
x_data = np.array([0, 1, 1.5, 2.5, 3, 4.5, 5, 6])
y_data = np.array([0, 67, 101, 168, 202, 310, 334, 404])

# Обчислення коефіцієнтів лінійної регресії методом найменших квадратів
A = np.vstack([x_data**2, np.ones(len(x_data))]).T
a, b = np.linalg.lstsq(A, y_data, rcond=None)[0]

# Побудова графіку
plt.scatter(x_data, y_data, label='Експериментальні точки')
plt.plot(x_data, a*x_data**2 + b, 'r', label=f'Регресія: y = {a:.2f}x^2 + {b:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Лінійна регресія методом найменших квадратів')
plt.grid(True)
plt.show()
