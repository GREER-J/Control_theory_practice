import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

"""
# RFunction that returns dy / dt


def model(y, t):
    k = 0.3
    dydt = -k * y
    return dydt


# initial condition
y0 = 5

start = 0
finish = 20
number_of_time_points = 40  # Default is 50

# Time points
t = np.linspace(start, finish, number_of_time_points)

# Solve ODE
y = odeint(model, y0, t)

# Plot results
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("y(t)")
plt.show()
"""
# second example


def model(y, t, k):
    dydt = -k * y
    return dydt


# initial condition
y0 = 5

start = 0
finish = 20
number_of_time_points = 40  # Default is 50

# Time points
t = np.linspace(start, finish, number_of_time_points)

# Solve ODE
k = 0.1
# comma is becuase a tuple expects multiple values
y1 = odeint(model, y0, t, args=(k,))
k = 0.2
y2 = odeint(model, y0, t, args=(k,))
k = 0.5
y3 = odeint(model, y0, t, args=(k,))

# Plot results
plt.plot(t, y1, 'r-', linewidth=2, label='k=0.1')
plt.plot(t, y2, 'b--', linewidth=2, label='k=0.2')
plt.plot(t, y3, 'g:', linewidth=2, label='k=0.5')
plt.title("Y vs K ODE prac")
plt.xlabel("Time (s)")
plt.ylabel("y(t)")
plt.legend(loc='best')
plt.show()
