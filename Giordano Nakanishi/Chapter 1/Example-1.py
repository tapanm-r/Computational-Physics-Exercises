# Simulation of Radioactive Decay
# dN / dt = - N / tau, N_0 = 100, tau = 1 second

import numpy as np
import matplotlib.pyplot as plt


def func(N, t, tau):
    return - (N / tau)

# Euler Method
def decay(N0, t0, tf, tau, dt):
    N = []
    N.append(N0)

    t = []
    t.append(t0)

    while t0 < tf:
        t.append(t0 + dt)
        N_new = N0 + func(N0, t, tau) * dt

        N.append(N_new)
        N0 = N_new
        t0 += dt
    
    return np.array(N), np.array(t)


if __name__ == "__main__":
    N0  = 100.0
    tf  = 5.0   # seconds
    tau = 1.0   # seconds

    plt.figure(1)
    # Analytical Solution: N = N0 * exp{-t / tau}
    t = np.linspace(0, tf, 1001, endpoint=True)
    plt.plot(t, N0 * np.exp(-t / tau), 'k-', label="True Solution")
    
    for dt in [0.05, 0.2, 0.5]:
        N, t = decay(N0, 0, tf, tau, dt)
        plt.scatter(t, N, s=5, label=f"Time Step = {dt}")

    plt.xlabel("time (s)")
    plt.ylabel("Number of Nuclei")
    plt.title("Decay of Radioactive Nuclei")
    plt.grid()
    plt.legend()
    plt.show()