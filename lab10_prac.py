import numpy as np
import matplotlib.pyplot as plt

# sampling
fs = 1200
ts = np.linspace(0, 1, fs)

# sample signal
xs = np.sin(2 * np.pi * 5 * ts) + np.sin(2 * np.pi * 50 * ts)


# convolution code
def convolution(x, h):
  N = len(x) + len(h) - 1
  y = []

  for i in range(N):
    sum = 0
    for k in range(len(x)):
      if 0<= i-k < len(h):
        sum  += x[k] * h[i-k]
    y.append(sum)
  return y


# x = [1, 2, 3]
# y = [2, 1, 4]
# print(convolution(x, y))
# hann
def hann(N):
  return [0.5 - 0.5 * np.cos((2 * np.pi * n) / (N-1)) for n in range(N)]


#input
N = 51
fc = 10

# impulse response
center = (N-1)/2
n = np.arange(N)
h = 2 * fc * np.sinc(2 * fc * (n - center)/fs) * hann(N)
h = h / sum(h)

# noise free signal
xf = convolution(xs, h)
tf = np.arange(len(xf))/fs

# signal plotting
plt.plot(ts, xs, label="input signal", color='gray')
plt.plot(tf, xf, label='filtered signal', color='blue')
plt.legend()
plt.show()
plt.show()