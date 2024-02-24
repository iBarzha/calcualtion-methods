import numpy as np
import matplotlib.pyplot as plt

# Задані дані
x_data = np.array([0, 1, 1.5, 2.5, 3, 4.5, 5, 6])
y_data = np.array([0, 67, 101, 168, 202, 310, 334, 404])

# Обчислення коефіцієнтів лінійної регресії методом найменших квадратів
A = np.vstack([x_data, np.ones(len(x_data))]).T
m, c = np.linalg.lstsq(A, y_data, rcond=None)[0]

# Побудова графіку
plt.scatter(x_data, y_data, label='Експериментальні точки')
plt.plot(x_data, m*x_data + c, 'r', label=f'Лінійна регресія: y = {m:.2f}x + {c:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Лінійна регресія методом найменших квадратів')
plt.grid(True)
plt.show()
