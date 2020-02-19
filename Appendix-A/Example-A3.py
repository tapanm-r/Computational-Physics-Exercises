# Verlet Method for the Harmonic Oscillator
# d2x/dt2 = -Ay, m = 1, A = 1

import matplotlib.pyplot as plt
import numpy as np

y0 = 0.2
v0 = 0.0

dt = 0.01

t = 0

ys = []
vs = []
Es = []
ys.append(y0)
vs.append(v0)
y1 = y0 + v0 * dt
ys.append(y1)
E = 0.5 * v0 ** 2 + 0.5 * y0 ** 2
Es.append(E)

while t <= 40:
    ynew = 2 * ys[-1] - ys[-2] - ys[-1] * (dt ** 2)
    vnew = 0.5 * (ynew - ys[-2]) / dt

    E = 0.5 * vnew ** 2 + 0.5 * ys[-1] ** 2

    ys.append(ynew)
    vs.append(vnew)
    Es.append(E)

    t += dt

plt.figure(1)
ax1 = plt.subplot(211)
plt.plot(np.arange(0,len(ys)) * dt, ys, 'r')
plt.ylabel("Amplitude")
plt.grid()
plt.title("Euler method for Harmonic Oscillator")

plt.subplot(212)
plt.plot(np.arange(0,len(Es)) * dt, Es, 'b')
plt.xlabel("Time")
plt.ylabel("Energy")
plt.ylim((0.00, 0.03))
plt.grid()

plt.setp(ax1.get_xticklabels(), visible=False)

plt.figure(2)
ax2 = plt.subplot(111)
plt.plot(ys[:-1], vs, 'b')
plt.grid()
plt.xlabel("Displacement")
plt.ylabel("Velocity")
plt.title("Phase space Diagram")
ax2.set_aspect(aspect='equal')

plt.show()