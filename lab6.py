import numpy as np
import matplotlib.pyplot as plt

# Define the unit step function
def u(n):
    return np.where(n >= 0, 1, 0)

# Define impulse response h[n] = u(n) - u(n-5)
def h(n):
    return u(n) - u(n - 5)

# Define input signal x[n] = u(n)
def x(n):
    return u(n)

# Define range for computation
n = np.arange(-5, 15)  # Defines a range for visualization

# Perform convolution manually
y = np.zeros(len(n))  # Initialize output array
for i in range(len(n)):  # Loop over each value of n
    sum_value = 0
    for k in range(len(n)):  # Perform summation
        if i - k >= 0:  # Ensure valid indexing
            sum_value += x(k) * h(i - k)
    y[i] = sum_value  # Store computed value

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
plt.stem(n, y, linefmt='g-', markerfmt='go', basefmt="k-", label='y[n] = x[n] * h[n]')
plt.title("Output Signal y[n] (Manual Convolution)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()