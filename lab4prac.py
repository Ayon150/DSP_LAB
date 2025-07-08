import numpy as np
import matplotlib.pyplot as plt

# Given signal
A = 3
F = 50
T = 1/F

t_cont = np.linspace(0, .1, 1000)
x_cont = A * np.cos(2 * np.pi * F * t_cont)

# Sampled signal
f_high = 200
f_low = 75

t_high = np.arange(0, 0.1, 1/f_high)
t_low = np.arange(0, 0.1, 1/f_low)

x_high = A * np.cos(100 * np.pi * t_high)
x_low = A * np.cos(100 * np.pi * t_low)

# Ploting code

plt.figure(figsize=(10, 6))
plt.plot(t_cont, x_cont, label='Continuous signal', color='black', linestyle='-')

plt.stem(t_high, x_high, linefmt='b', basefmt='black', markerfmt='bo', label='sampled at 200hz')
plt.stem(t_low, x_low, linefmt='r', basefmt='black', markerfmt='ro', label='sampled at 75hz')

plt.title('Continuous vs Sampled signal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
