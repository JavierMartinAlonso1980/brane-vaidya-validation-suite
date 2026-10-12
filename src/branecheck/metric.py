import numpy as np

def f(params, u, r):
    return params.k + r**2 / params.L**2 - params.mu(u) / r**2

def f_r(params, u, r):
    return 2.0 * r / params.L**2 + 2.0 * params.mu(u) / r**3

def f_u(params, u, r):
    return -params.mu_prime(u) / r**2

def proper_time_residual(params, epsilon, vdot, adot, u, a):
    return -f(params, u, a) * vdot**2 + 2.0 * epsilon * vdot * adot + 1.0
