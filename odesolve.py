# odesolve.py
#
# Author: <insert name>
# Date:   <insert date>
# Description: <insert description>
#
# You should fill out the code for the functions below so that they pass the
# tests in test_odesolve.py
import math
import numpy as np


def euler(f, x, t, h):
    """Perform one step of the Euler method"""
    return x + h * f(x, t)


def rk4(f, x, t, h):
    """Perform one step of the RK$ method"""

    # 4 steps for the rk4
    k1 = f(x, t)
    k2 = f(x + (h / 2) * k1, t + (h / 2))
    k3 = f(x + (h / 2) * k2, t + (h / 2))
    k4 = f(x + h * k3, t + h)

    # final result for the rk4
    res = x + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6
    return res


def solveto(f, x1, t1, t2, hmax, method=euler):
    """Use many steps of method to get from x1,t1 to x2,t2"""
    # number of iterations
    num_iters = math.floor((t2 - t1) / hmax)

    # intial value is x1
    res = x1
    tmp = t1
    # iterations
    for i in range(0, num_iters):
        res = method(f, res, tmp, hmax)
        tmp = tmp + hmax
        
    if tmp != t2:
        #if the result is a fractional number
        #add the t to the fractional number and culculate the equation again
        #until the result is an integer
        hmax = t2 - tmp
        res = method(f, res, tmp, hmax)
    return res


def odesolve(f, X0, t, hmax, method=euler):
    """Compute the solution at different values of t"""
    t0 = t[0]
    res = []
    if isinstance(X0, list):
        X0 = X0[0]

    for t1 in t:
        cur_res = solveto(f, X0, t0, t1, hmax, method)
        res.append(cur_res)
    res = np.array(res)
    return res