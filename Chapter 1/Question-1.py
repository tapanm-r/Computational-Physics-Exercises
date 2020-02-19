# Simulation of Freely Falling Object
# dv / dt = - g, g = 9.8 m / s^2

import numpy as np
import matplotlib.pyplot as plt


def func(v, t, g):
    return -g

# Euler Method
def decay(v0, t0, tf, g, dt):
    v = []
    v.append(v0)

    t = []
    t.append(t0)

    while t0 < tf:
        t.append(t0 + dt)
        v_new = v0 + func(v0, t, g) * dt

        v.append(v_new)
        v0 = v_new
        t0 += dt
    
    return np.array(v), np.array(t)


if __name__ == "__main__":
    v0  = 0.0    # metres per second
    tf  = 10.0   # seconds
    g   = 9.8    # metres per sq-second

    plt.figure(1)
    # Analytical Solution: v = v0 - g * t
    t = np.linspace(0, tf, 1001, endpoint=True)
    plt.plot(t, v0 - t * g, 'k-', label="True Solution")
    
    for dt in [0.05, 0.2, 0.5]:
        v, t = decay(v0, 0, tf, g, dt)
        plt.scatter(t, v, s=5, label=f"Time Step = {dt}")

    plt.xlabel("time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Freely Falling Object")
    plt.grid()
    plt.legend()
    plt.show()