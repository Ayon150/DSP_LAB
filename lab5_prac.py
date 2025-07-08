import numpy as np
import matplotlib.pyplot as plt


# Continuous signal
def signal(t):
    return 3*np.cos(200*np.pi*t) + 5*np.sin(600*np.pi*t) + 10*np.cos(1200*np.pi*t)


t_cont = np.linspace(0, 0.01, 1000)
x_cont = signal(t_cont)

# discreate signal
sampling_rates = [100, 1200, 600, 2000]
colours = ['b', 'g', 'r', 'm']

# ploting code
plt.figure(figsize=(10, 6))
plt.plot(t_cont, x_cont, label='Continuous signal')
for i, freq in enumerate(sampling_rates):
    t_dis = np.arange(0, 0.01, 1/freq)
    x_dis = signal(t_dis)
    plt.stem(t_dis, x_dis, linefmt=colours[i], basefmt='black', markerfmt=colours[i]+'o', label=f'sampled at {freq} hz')

plt.grid(True)
plt.legend()
plt.show()
