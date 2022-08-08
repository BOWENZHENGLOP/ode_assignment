import numpy as np
import matplotlib.pyplot as plt
from odesolve import odesolve


# Ref: code from the Section 8 of specification.pdf
# test if the odesolve is suitable for a plot
def f(X, t):
    x, y = X
    dxdt = y
    dydt = -x
    return np.array([dxdt, dydt])


x0 = 1
y0 = 0

X0 = np.array([x0, y0])
h = 0.01
t = np.linspace(0, 10, 100)

Xt = odesolve(f, X0, t, h)

plt.plot(t, Xt.T[0])
plt.plot(t, Xt.T[1])
plt.savefig('shm.pdf')
plt.show()
