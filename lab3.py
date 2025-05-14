import numpy as np
import matplotlib.pyplot as plt

# Define parameters
A = 3  # Amplitude
f = 50  # Frequency (since ω = 100π → f = 100π / (2π) = 50 Hz)
T = 1 / f  # Period of the signal

# Define continuous-time signal
t_cont = np.linspace(0, 0.1, 1000)  # Fine grid for smooth plot
x_cont = A * np.cos(100 * np.pi * t_cont)  # Continuous signal

# Define sampling rates
Fs_high = 200  # Sampling at 200 Hz
Fs_low = 75  # Sampling at 75 Hz

# Sampled time vectors
t_high = np.arange(0, 0.1, 1/Fs_high)  # Sampling at 200 Hz
t_low = np.arange(0, 0.1, 1/Fs_low)  # Sampling at 75 Hz

# Compute discrete signals
x_high = A * np.cos(100 * np.pi * t_high)  # Sampled at 200 Hz
x_low = A * np.cos(100 * np.pi * t_low)  # Sampled at 75 Hz

# Plot signals
plt.figure(figsize=(10, 6))

# Plot continuous-time signal
plt.plot(t_cont, x_cont, label="Continuous Signal", color="black", linestyle="-")

# Plot sampled signals
plt.stem(t_high, x_high, linefmt="b", markerfmt="bo", basefmt="black", label="Sampled at 200 Hz")
plt.stem(t_low, x_low, linefmt="r", markerfmt="ro", basefmt="black", label="Sampled at 75 Hz")

# Labels and legend
plt.title("Continuous vs Sampled Signals")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Show plot
plt.show()