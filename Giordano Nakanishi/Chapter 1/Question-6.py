# Simulation of Population growth
# dN / dt = a * N - b * N^2

import numpy as np
import matplotlib.pyplot as plt


def func(N, t, a, b):
    return a * N - b * N * N

# Euler Method
def popgrowth(N0, t0, tf, a, b, dt):
    N = []
    N.append(N0)

    t = []
    t.append(t0)

    while t0 < tf:
        t.append(t0 + dt)
        N_new = N0 + func(N0, t, a, b) * dt

        N.append(N_new)
        N0 = N_new
        t0 += dt
    
    return np.array(N), np.array(t)


if __name__ == "__main__":
    N0  = 1000.0
    tf  = 5.0   # seconds
    a   = 1.0   # Birth-rate

    plt.figure(1)
    b = 0.0    # Death-rate
    # Analytical Solution: N = N0 * exp{a * t}
    t = np.linspace(0, tf, 1001, endpoint=True)
    plt.plot(t, N0 * np.exp(a * t), 'k-', label="True Solution")
    
    for dt in [0.01, 0.05, 0.2]:
        N, t = popgrowth(N0, 0, tf, a, b, dt)
        plt.scatter(t, N, s=5, label=f"Time Step = {dt}")
    
    plt.xlabel("time (year)")
    plt.ylabel("Population")
    plt.title("Population Growth with '0' death rate")
    plt.grid()
    plt.legend(loc=2)
    
    fig = plt.figure(2)
    fig.suptitle("Population Growth, N_0 = 1000")
    dt = 0.01    # Death-rate
    # Analytical Solution: N = a * N0 * exp{a * t} / (a - b * N0 * (1 - exp{a * t}))
    t = np.linspace(0, tf, 1001, endpoint=True)
    
    i = 1
    for b in [0.01, 0.02, 0.05]:
        N, t = popgrowth(N0, 0, tf, a, b, dt)
        plt.subplot(1, 3, i)
        plt.plot(t, a * N0 * np.exp(a * t) / (a - b * N0 * (1 - np.exp(a * t))), 'k-', label=f"True Solution, b = {b}")
        plt.scatter(t, N, s=5, label=f"Time Step = {dt}")
        plt.xlabel("time (year)")
        plt.ylabel("Population")
        plt.grid()
        plt.legend(loc=1)
        i += 1

    plt.show()