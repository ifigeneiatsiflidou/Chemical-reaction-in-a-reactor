# Exercise: Chemical Reaction in a Reactor

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE function: dC̃/dτ = 1 - (1 + β) * C̃
def deriv(y, t, beta):              # return derivative of y(as C̃)
    return 1.0 - (1.0 + beta) * y

# - - - Main program - - -

# - - - solve the initial value problem numerically
# input initial condition
yinit = 0.0

# construct time interval to solve equation
time_interval = [0.0, 6.0]
ntime = 100
time = np.linspace(time_interval[0], time_interval[1], ntime)

plt.figure(figsize=(10, 6))

# integrate ODE
b0 = 0
sol_b0 = odeint(deriv, yinit, time, args=(b0,))
sol_b0_anal = 1.0 / (1.0 + b0) * (1.0 - np.exp(-(1.0 + b0)*time))
plt.plot(time, sol_b0, 'b-', label='Numerical β=0')
plt.plot(time, sol_b0_anal, 'b.', label='Analytical β=0')
print("Final point for β=0: ", sol_b0[ntime-1])

b1 = 0.2
sol_b1 = odeint(deriv, yinit, time, args=(b1,))
sol_b1_anal = 1.0 / (1.0 + b1) * (1.0 - np.exp(-(1.0 + b1)*time))
plt.plot(time, sol_b1, 'r-', label='Numerical β=0.2')
plt.plot(time, sol_b1_anal, 'r.', label='Analytical β=0.2')
print("Final point for β=0.2: ", sol_b1[ntime-1])

# - - - prepare graph
plt.xlabel('τ')
plt.ylabel('C̃')
plt.title('Linear Chemical Reaction')

plt.legend()
plt.tight_layout()
plt.show()
