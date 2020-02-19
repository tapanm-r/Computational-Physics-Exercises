# Simulation of Simultaneous Radioactive Conversion
# dN_A / dt = - N_A / tau_A
# dN_B / dt = N_A / tau_A - N_B / tau_B
# N_A and N_B approach constant values depending on tau_A and tau_B

import numpy as np
import matplotlib.pyplot as plt


def func_A(N_A, N_B, t, tau_A, tau_B):
    return N_B / tau_B - N_A / tau_A

def func_B(N_A, N_B, t, tau_A, tau_B):
    return N_A / tau_A - N_B / tau_B

# Euler Method
def decay(N_A0, N_B0, t0, tf, tau_A, tau_B, dt):
    N_A = []
    N_A.append(N_A0)

    N_B = []
    N_B.append(N_B0)

    t = []
    t.append(t0)

    while t0 < tf:
        t.append(t0 + dt)
        N_A_new = N_A0 + func_A(N_A0, N_B0, t0, tau_A, tau_B) * dt
        N_B_new = N_B0 + func_B(N_A0, N_B0, t0, tau_A, tau_B) * dt

        N_A.append(N_A_new)
        N_B.append(N_B_new)
        N_A0 = N_A_new
        N_B0 = N_B_new
        t0 += dt
    
    return np.array(N_A), np.array(N_B), np.array(t)


if __name__ == "__main__":
    N_A0  = 100.0
    N_B0  = 0.0

    tau_A   = 2.0    # seconds
    tau_B   = 1.0    # seconds

    tf = 10.0        # seconds

    plt.figure(1)
    # Analytical Solution: 
    # N_A = (N_A0 * (tau_A + tau_B * exp{-t * (1 / tau_A + 1 / tau_B)}) - N_B0 * tau_A * (-1 + exp{-t * (1 / tau_A + 1 / tau_B)})) / (tau_A + tau_B)
    # N_B = (N_B0 * (tau_B + tau_A * exp{-t * (1 / tau_A + 1 / tau_B)}) - N_A0 * tau_B * (-1 + exp{-t * (1 / tau_A + 1 / tau_B)})) / (tau_A + tau_B)
    t = np.linspace(0, tf, 1001, endpoint=True)
    N_A = (N_A0 * (tau_A + tau_B * np.exp(-t * (1 / tau_A + 1 / tau_B))) - N_B0 * tau_A * (-1 + np.exp(-t * (1 / tau_A + 1 / tau_B)))) / (tau_A + tau_B)
    N_B = (N_B0 * (tau_B + tau_A * np.exp(-t * (1 / tau_A + 1 / tau_B))) - N_A0 * tau_B * (-1 + np.exp(-t * (1 / tau_A + 1 / tau_B)))) / (tau_A + tau_B)

    plt.plot(t, N_A, 'k', label="True Solution for A")
    plt.plot(t, N_B, 'maroon', label="True Solution for B")

    for dt, col in zip([0.05, 0.2, 0.5], ['b', 'r', 'g']):
        N_A, N_B, t = decay(N_A0, N_B0, 0, tf, tau_A, tau_B, dt)
        plt.scatter(t, N_A, s=10, c=col, marker='o', label=f"For A, Time Step = {dt}")
        plt.scatter(t, N_B, s=10, c=col, marker='^', label=f"For B, Time Step = {dt}")
    
    plt.xlabel("time (s)")
    plt.ylabel("Number of Nuclei")
    plt.title("Simultaneous decay and conversion of Radioactive Nuclei")
    plt.grid()
    plt.legend(loc=1)

    fig = plt.figure(2)
    fig.suptitle("Simultaneous Radioactive Decay and Conversion")
    i = 1
    dt = 0.05
    for tau_A, tau_B in zip([0.5, 1.0, 2.0], [1.0, 1.0, 1.0]):
        N_A, N_B, t = decay(N_A0, N_B0, 0, tf, tau_A, tau_B, dt)

        plt.subplot(3, 1, i)
        plt.scatter(t, N_A, s=5, marker='o', label=f"Tau_A = {tau_A}")
        plt.scatter(t, N_B, s=5, marker='^', label=f"Tau_B = {tau_B}")
        plt.ylabel("Velocity (m/s)")
        plt.grid()
        plt.legend(loc=1)
        i += 1

    plt.xlabel("time (s)")
    plt.show()