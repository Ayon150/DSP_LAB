import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11, 1)

# unit step signal
unit_step = np.where(n >= 0, 1, 0)

# ramp signal
ramp_signal = np.where(n >= 0, n, 0)

# exponential signal
alpha = -0.9
exponential_signal = alpha**n

# sine signal
A = 1
pi = np.pi
f = .1
phi = 0
sine_wave = A * np.sin(2 * pi * f * n + phi)

# plotting

plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.stem(n, unit_step, label='Unit_step signal')
plt.legend()
plt.title('UNIT_STEP signal')
plt.grid(True)

plt.subplot(3, 2, 2)
plt.stem(n, ramp_signal, label='Ramp_signal')
plt.legend()
plt.title('RAMP_signal')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.stem(n, exponential_signal)
plt.title('Exponential_signal')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.stem(n, sine_wave, label='Sine signal')
plt.legend()
plt.title('Sine signal')
plt.grid(True)

plt.tight_layout()
plt.show()
