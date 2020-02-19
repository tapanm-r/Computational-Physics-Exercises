# Seconnd-order Runge-Kutta method for the Harmonic oscillator
# d2x/dt2 = -Ay, m = 1, A = 1

import matplotlib.pyplot as plt
import numpy as np

y0 = 0.2
v0 = 0.0

dt = 0.01

t = 0

ys = []
Es = []
ys.append(y0)
E = 0.5 * v0 ** 2 + 0.5 * y0 ** 2
Es.append(E)

while t <= 40:
    y1 = y0 + 0.5 * v0 * dt
    v1 = v0 - 0.5 * y0 * dt

    ynew = y0 + v1 * dt
    vnew = v0 - y1 * dt

    E = 0.5 * vnew ** 2 + 0.5 * ynew ** 2

    ys.append(ynew)
    Es.append(E)

    v0 = vnew
    y0 = ynew

    t += dt

ax1 = plt.subplot(211)
plt.plot(np.linspace(0, 40, 4001, endpoint=True), ys, 'r')
plt.ylabel("Amplitude")
plt.grid()
plt.title("Euler method for Harmonic Oscillator")

plt.subplot(212)
plt.plot(np.linspace(0, 40, 4001, endpoint=True), Es, 'b')
plt.xlabel("Time")
plt.ylabel("Energy")
plt.ylim((0.00, 0.03))
plt.grid()

plt.setp(ax1.get_xticklabels(), visible=False)
plt.show()