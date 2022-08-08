import numpy as np
from odesolve import solveto, euler, rk4
import matplotlib.pyplot as plt


def f(x, t):
    return x


X0 = 1
t1 = 0
t2 = 1
f_value = 2.718281828459045
h_array = np.logspace(-5, -1, 100)
error0, error1 = [], []

# iterate over h to calculate error
for h in h_array:
    est_euler, est_rk4 = solveto(f, X0, t1, t2, h, euler), solveto(f, X0, t1, t2, h, rk4)
    error0.append(f_value - est_euler)
    error1.append(f_value - est_rk4)

plt.scatter(h_array, error0, label='Euler', s=5)
plt.scatter(h_array, error1, label='RK4', s=5)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("h")
plt.ylabel("error")
plt.legend()
plt.title('Comparison of errors for Euler and RK4')
plt.show()
