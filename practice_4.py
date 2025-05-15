import numpy as np
import matplotlib.pyplot as plt

A = 3
f = 50
t = 1/f

n = np.linspace(0, 0.1, 1000)
x = A * np.sin(A * 100 * n)

plt.figure(figsize=(12, 8))
plt.plot()
