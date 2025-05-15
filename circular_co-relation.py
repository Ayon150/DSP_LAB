import numpy as np
import matplotlib.pyplot as plt

# Given signals
x = np.array([1, 3, -2, 4])
y = np.array([2, 3, -1, 3])
z = np.array([2, -1, 4, -2])

# Circular correlation function
def circular_correlation(a, b):
    N = len(a)  # Assuming equal lengths
    result = np.zeros(N)
    
    for m in range(N):  # Iterate through shifts
        sum_value = 0
        for n in range(N):  # Compute sum for each shift
            sum_value += a[n] * b[(n - m) % N]  # Circular indexing using modulo
        result[m] = sum_value
    
    return result

# Compute circular correlation
r_xy_circ = circular_correlation(x, y)
r_yz_circ = circular_correlation(y, z)

# Define lag values
lags = np.arange(len(x))

# Plot results
plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.stem(lags, r_xy_circ)
plt.title("Circular Correlation between x(n) and y(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(lags, r_yz_circ)
plt.title("Circular Correlation between y(n) and z(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.show()