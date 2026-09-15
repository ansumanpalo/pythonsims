import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# -----------------------------
# Parameters
# -----------------------------
m1 = 1.0       # mass of first bob
m2 = 1.0       # mass of second bob
L1 = 1.0       # length of first rod
L2 = 1.0       # length of second rod
g = 9.81       # gravitational acceleration

# Initial conditions
theta1_0 = np.radians(120)   # first angle
theta2_0 = np.radians(120)   # second angle
omega1_0 = 0.0               # first angular velocity
omega2_0 = 0.0               # second angular velocity

y0 = [theta1_0, omega1_0, theta2_0, omega2_0]

# -----------------------------
# Equations of motion
# -----------------------------
def double_pendulum(t, y):
    theta1, omega1, theta2, omega2 = y

    delta = theta1 - theta2

    den1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta)**2

    alpha1 = (
        m2 * L1 * omega1**2 * np.sin(delta) * np.cos(delta)
        + m2 * g * np.sin(theta2) * np.cos(delta)
        + m2 * L2 * omega2**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta1)
    ) / den1

    den2 = (L2 / L1) * den1

    alpha2 = (
        -m2 * L2 * omega2**2 * np.sin(delta) * np.cos(delta)
        + (m1 + m2) * g * np.sin(theta1) * np.cos(delta)
        - (m1 + m2) * L1 * omega1**2 * np.sin(delta)
        - (m1 + m2) * g * np.sin(theta2)
    ) / den2

    return [omega1, alpha1, omega2, alpha2]


# -----------------------------
# Solve numerically
# -----------------------------
t_start = 0
t_end = 20
fps = 60

t_eval = np.linspace(t_start, t_end, t_end * fps)

solution = solve_ivp(
    double_pendulum,
    [t_start, t_end],
    y0,
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-9
)

theta1 = solution.y[0]
theta2 = solution.y[2]

# -----------------------------
# Convert angles to x,y
# -----------------------------
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)

x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

# -----------------------------
# Animation
# -----------------------------
fig, ax = plt.subplots()

ax.set_xlim(-(L1 + L2 + 0.2), L1 + L2 + 0.2)
ax.set_ylim(-(L1 + L2 + 0.2), L1 + L2 + 0.2)
ax.set_aspect("equal")
ax.grid()

line, = ax.plot([], [], "o-", lw=2)
trace, = ax.plot([], [], "-", lw=1)

trace_x = []
trace_y = []


def update(frame):
    trace_x.append(x2[frame])
    trace_y.append(y2[frame])

    line.set_data(
        [0, x1[frame], x2[frame]],
        [0, y1[frame], y2[frame]]
    )

    trace.set_data(trace_x, trace_y)

    return line, trace


animation = FuncAnimation(
    fig,
    update,
    frames=len(t_eval),
    interval=1000 / fps,
    blit=True
)

plt.show()