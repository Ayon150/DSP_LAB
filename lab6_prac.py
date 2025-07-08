import numpy as np
import matplotlib.pyplot as plt


def u(n):
    return np.where(n >= 0, 1, 0)


def x(n):
    return u(n)


def h(n):
    return u(n)-u(n-5)


n = np.arange(-10, 20)
y = np.zeros(len(n))

for i in range(len(n)):
    sum_value = 0
    for k in range(len(n)):
        n_k = n[i] - n[k]
        sum_value += x(n[i])*h(n_k)
    y[i]=sum_value

print(y)