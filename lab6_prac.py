import numpy as np
import matplotlib.pyplot as plt


def u(n):
    return np.where(n >= 0, 1, 0)


def h(n):
    return u(n) - u(n-5)


def x(n):
    return u(n)


n = np.arange(-5, 15)

y = np.zeros(len(n))

for i in range(len(n)):
    sum = 0
    for k in range(len(n)):
        if i-k >= 0:
            sum += x(k) * h(i-k)
    y[i] = sum

plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.stem(n, x(n))
plt.title('Input signal')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h(n))
plt.title('Input signal')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.title('Input signal')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

