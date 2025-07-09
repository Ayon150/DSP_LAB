import numpy as np
import matplotlib.pyplot as plt

# Unit step function
def u(n):
    return np.where(n >= 0, 1, 0)

# Signals
def x(n):
    return u(n)

def h(n):
    return u(n) - u(n-5)

# Discrete time range
n = np.arange(-10, 20)
xx = x(n)
hh = h(n)

# Convolution
def convolution(x, h):
    N = len(x) + len(h) - 20
    y = []
    for i in range(N):
        s = 0
        for k in range(len(x)):
            if 0 <= i - k < len(h):
                s += x[k] * h[i - k]
        y.append(s)
    return y

yy = convolution(xx, hh)
##ny = np.arange(-20, 40)
n_conv = np.arange(-20, 20)  # Adjusted time axis for output

# Plotting all signals
plt.figure(figsize=(12, 6))

# x(n)
plt.subplot(3, 1, 1)
plt.stem(n, xx, basefmt=" ")
plt.title('Signal x(n) = u(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)

# h(n)
plt.subplot(3, 1, 2)
plt.stem(n, hh, basefmt=" ")
plt.title('Signal h(n) = u(n+5) - u(n)')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid(True)

# y(n) = x(n) * h(n)
plt.subplot(3, 1, 3)
plt.stem(n_conv, yy, basefmt=" ")
plt.title('Convolution y(n) = x(n) * h(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)

plt.tight_layout()
plt.show()