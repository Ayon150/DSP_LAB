import numpy as np
import matplotlib.pyplot as plt

# Define a sample discrete-time signal
n = np.arange(0, 50)
x = np.sin(0.2 * np.pi * n) + 0.5 * np.random.randn(len(n))  # Noisy sine wave

# 6-Point Averaging Filter
def averaging_filter(x):
    y_avg = np.zeros_like(x)
    for i in range(len(x)):
        if i >= 5:
            y_avg[i] = np.sum(x[i-5:i+1]) / 6  # Average last 6 samples
        else:
            y_avg[i] = np.sum(x[:i+1]) / (i+1)  # Partial averaging at start
    return y_avg

# 6-Point Differencing Filter
def differencing_filter(x):
    y_diff = np.zeros_like(x)
    for i in range(len(x)):
        if i >= 6:
            y_diff[i] = x[i] - x[i-6]  # Difference between current and 6 steps before
        else:
            y_diff[i] = x[i]  # No difference for first few samples
    return y_diff

# Apply filters
y_avg = averaging_filter(x)
y_diff = differencing_filter(x)

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(n, x, linefmt='b-', markerfmt='bo', basefmt="k-", label='Original Signal')
plt.title("Original Noisy Signal")
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n, y_avg, linefmt='g-', markerfmt='go', basefmt="k-", label='Averaging Filter Output')
plt.title("6-Point Averaging Filter (Smooths Signal)")
plt.legend()
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n, y_diff, linefmt='r-', markerfmt='ro', basefmt="k-", label='Differencing Filter Output')
plt.title("6-Point Differencing Filter (Detects Changes)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show() 