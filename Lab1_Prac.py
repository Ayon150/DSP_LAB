import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)

# unit step signal
unit_step = np.where(n >= 0, 1, 0)

# ramp signal
ramp = np.where(n >= 0, n, 0)

# exponential signal
a = -0.9
exp = a**n

# sine wave
A = 1
pi = np.pi
f = .1
phi = 0
sin_wave = A*np.sin((2 * pi * f * n) + phi)

# cos wave
cos_wave = A * np.cos((2 * pi * f * n) + phi)

# ploting code
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.stem(n, unit_step)
plt.title('Unit step signal')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(n, ramp)
plt.title('Ramp signal')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(n, exp)
plt.title('Exponential signal')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(n, sin_wave)
plt.title('Sine wave')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.stem(n, sin_wave)
plt.title('Sine wave')
plt.grid(True)

plt.tight_layout()
plt.show()
