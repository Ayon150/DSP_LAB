import numpy as np
import matplotlib.pyplot as plt


# Define the analog signal function
def analog_signal(t):
    return 3*np.cos(200*np.pi*t) + 5*np.sin(600*np.pi*t) + 10*np.cos(1200*np.pi*t)


# Define time for continuous signal
t_cont = np.linspace(0, 0.01, 1000)  # High-resolution time vector
x_cont = analog_signal(t_cont)

# Define sampling rates
sampling_rates = [2000, 800, 1000, 1200]  # Different sampling frequencies
colors = ['r', 'g', 'b', 'm']  # Colors for different sampling rates

plt.figure(figsize=(10, 6))

# Plot the original continuous signal
plt.plot(t_cont, x_cont, 'k', label="Original Analog Signal", alpha=0.6)

# Loop through sampling rates and plot discrete samples
for i, fs in enumerate(sampling_rates):
    t_sampled = np.arange(0, 0.01, 1/fs)  # Discrete time instances based on sampling rate
    x_sampled = analog_signal(t_sampled)
    
    plt.stem(t_sampled, x_sampled, linefmt=colors[i]+'-', markerfmt=colors[i]+'o', basefmt="k-", label=f"Sampled at {fs} Hz")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Continuous vs Discrete Signal Representation")
plt.legend()
plt.grid()
plt.show()