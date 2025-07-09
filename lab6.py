import numpy as np
import matplotlib.pyplot as plt


# Define the unit step function
def u(n):
    return np.where(n >= 0, 1, 0)


# Define impulse response h[n] = u(n) - u(n-5)
def h(n):
    return u(n+5) - u(n)


# Define input signal x[n] = u(n)
def x(n):
    return u(n)


# Define range for computation
n = np.arange(-10, 20)  # Defines a range for visualization
y = np.zeros(len(n))  # Initialize output array

# Perform manual convolution: y[n] = sum of x(k) * h(n - k)
for i in range(len(n)-5):
    sum_value = 0
    for k in range(len(n)-5):
        n_k = n[i] - n[k]
        sum_value += x(n[k]) * h(n_k)
    y[i] = sum_value
    
# Plot results
plt.figure(figsize=(10, 5))

plt.subplot(3, 1, 1)
plt.stem(n, x(n), linefmt='b-', markerfmt='bo', basefmt="k-", label='x[n]')
plt.title("Input Signal x[n]")
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, h(n), linefmt='r-', markerfmt='ro', basefmt="k-", label='h[n]')
plt.title("Impulse Response h[n]")
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(nn, y, linefmt='g-', markerfmt='go', basefmt="k-", label='y[n] = x[n] * h[n]')
plt.title("Output Signal y[n] (Manual Convolution)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()