import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 50)

x = np.sin(0.2 * np.pi * n) + 0.5 * np.random.randn(len(n))


def six_point_average(x):
    y_avg = np.zeros_like(x)
    for i in range(len(x)):
        if i >= 6:
            y_avg[i] = np.sum(x[i-5:i+1])/6
        else:
            y_avg[i] = sum(x[:i+1])/(i+1)
    return y_avg


def difference_filter(x):
    y_diff = np.zeros_like(x)
    for i in range(len(x)):
        if i >= 6:
            y_diff[i] = x[i]-x[i-6]
        else:
            y_diff[i] = x[i]
    return y_diff

y_avg = six_point_average(x)
y_diff = difference_filter(x)

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title('Noisy signal')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, y_avg)
plt.title('Six point averaging')
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n, y_diff)
plt.title('differnce')
plt.grid()

plt.tight_layout()
plt.show()