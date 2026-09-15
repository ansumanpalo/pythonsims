import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from scipy.integrate import solve_ivp


# -----------------------------
# Definitions
# -----------------------------

# ||||||||||Parameters||||||||||
m = 1 # kg
l = 1 # m
g = 9.81 # m/s^2
b = 0.1 # 

#||Time and Initial Conditions||
theta_0 = math.radians(180) # rad
theta_dot_0 = -0.01 # rad/s
t_start = 0 # seconds
t_end = 10 # seconds

# ||||||Animation Related||||||
fps = 60

# -----------------------------
# Equations of Motion
# -----------------------------
def simple_damped_pendulum(t, x) -> list[float]:
    theta, theta_dot = x
    theta_ddot = -1.0 * (math.sin(theta)*g/l + theta_dot*b/(m*l**2))
    return [theta_dot, theta_ddot]

# -----------------------------
# Solver
# -----------------------------
t_vals = np.linspace(t_start, t_end, (t_end-t_start)*fps)
solution = solve_ivp(
    simple_damped_pendulum, 
    [t_start, t_end],
    [theta_0, theta_dot_0],
    t_eval=t_vals,
    method="RK45", 
    rtol=1e-9,
    atol=1e-9
)

# -----------------------------
# Static Plots
# -----------------------------
def static_plots(solution):
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))

    # Plot the time solutions
    axs[0].plot(solution.t, solution.y[0])
    axs[0].plot(solution.t, solution.y[1])
    axs[0].grid()

    # Plot the phase portrait
    axs[1].plot(solution.y[0], solution.y[1])
    axs[1].grid()

    plt.tight_layout()
    plt.show()


def animations(solution):
    theta_vals, theta_dot_vals = solution.y
    time_vals = solution.t

    # Extract Cartesian values
    x_vals = np.sin(theta_vals) * l
    y_vals = -np.cos(theta_vals) * l

    fig, (pend_ax, phase_ax) = plt.subplots(1, 2, figsize=(12, 6))

    # Set pendulum subplot and add pendulum elements
    pend_ax.set_xlim(-l*1.2, l*1.2)
    pend_ax.set_ylim(-l*1.2, l*1.2)
    pend_ax.set_aspect("equal")
    pend_ax.grid()
    pend_rod, = pend_ax.plot([], [], lw=2, color='black', zorder=2)
    pend_bob = patches.Circle((0, -l), 0.05, color='blue', zorder=3)
    pend_ax.add_patch(pend_bob) 

    # Set Phase Portrait subplot and elements
    phase_ax.grid()
    phase_line, = phase_ax.plot(theta_vals, theta_dot_vals, color='gray', zorder=2)
    phase_pos = phase_ax.scatter([0], [0], s=100, color='blue', zorder=3)

    def init():
        pend_rod.set_data([0, 0], [0, -l])
        pend_bob.set_center((0, -l))

        phase_pos.set_offsets([0, 0])
        return pend_rod, pend_bob, phase_pos

    def update(frame):
        pend_rod.set_data([0, x_vals[frame]], [0, y_vals[frame]])
        pend_bob.set_center((x_vals[frame], y_vals[frame]))
        phase_pos.set_offsets([theta_vals[frame], theta_dot_vals[frame]])
        return pend_rod, pend_bob, phase_pos

    animation = FuncAnimation(
        fig, #9880345894
        update,
        init_func=init,
        frames=len(t_vals),
        interval=1000 / fps,
        blit=True
    )

    plt.tight_layout()
    plt.show()


# animations(solution)
static_plots(solution)