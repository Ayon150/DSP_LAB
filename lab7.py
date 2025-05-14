import numpy as np
import matplotlib.pyplot as plt

# Given discrete signals
x = np.array([1, 3, -2, 4])
y = np.array([2, 3, -1, 3])
z = np.array([2, -1, 4, -2])

# Cross-correlation function (manual implementation)
def cross_correlation(a, b):
    len_a = len(a)
    len_b = len(b)
    result = np.zeros(len_a + len_b - 1)

    for m in range(-(len_b - 1), len_a):  # Shifting index (lag)
        sum_value = 0
        for n in range(len_a):  # Iterating through signal
            if 0 <= n - m < len_b:  # Ensure valid index
                sum_value += a[n] * b[n - m]
        result[m + (len_b - 1)] = sum_value  # Store in correct index
    return result

# Compute correlations
r_xy = cross_correlation(x, y)
r_yz = cross_correlation(y, z)

# Define lag values
lags = np.arange(-(len(y) - 1), len(x))

# Plot results
plt.figure(figsize=(12, 10))

plt.subplot(2, 1, 1)
plt.stem(lags, r_xy)
plt.title("Corrected Cross-Correlation between x(n) and y(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(lags, r_yz)
plt.title("Corrected Cross-Correlation between y(n) and z(n)")
plt.xlabel("Lag")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.show()