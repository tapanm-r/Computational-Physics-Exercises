# Simulation of velocity depended frictional force on an accelerating body
# dv / dt = a - b*v, a = 10, b = 1
# v approaches constant value at long times called 'Terminal velocity'

import numpy as np
import matplotlib.pyplot as plt


def func(v, t, a, b):
    return a - b * v

# Euler Method
def decay(v0, t0, tf, a, b, dt):
    v = []
    v.append(v0)

    t = []
    t.append(t0)

    while t0 < tf:
        t.append(t0 + dt)
        v_new = v0 + func(v0, t, a, b) * dt

        v.append(v_new)
        v0 = v_new
        t0 += dt
    
    return np.array(v), np.array(t)


if __name__ == "__main__":
    v0  = 0.0    # metres per second
    tf  = 10.0   # seconds
    a   = 10.0   # metres per sq-second
    b   = 1.0    # per second

    plt.figure(1)
    # Analytical Solution: v = v0 * exp{-b * t} + (a / b) * (1 - exp{-b * t})
    t = np.linspace(0, tf, 1001, endpoint=True)
    plt.plot(t, v0 * np.exp(-b * t) + a * (1 - np.exp(-b * t)) / b, 'k-', label="True Solution")
    
    for dt in [0.05, 0.2, 0.5]:
        v, t = decay(v0, 0, tf, a, b, dt)
        plt.scatter(t, v, s=5, label=f"Time Step = {dt}")

    plt.xlabel("time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Freely Falling Object with Air drag")
    plt.grid()
    plt.legend(loc=5)
    plt.show()