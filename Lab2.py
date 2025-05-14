import numpy as np
import matplotlib.pyplot as plt

# Generate n values
n = np.arange(-10, 11, 1)

# Compute the sinusoidal signal for ω = π
omega = np.pi
sinusoidal_signal = np.cos(omega/4 * n)

# Plot the signal
plt.stem(n, sinusoidal_signal)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.title("Simple Sinusoidal Plot (ω = π)")
plt.grid(True)
plt.show()
