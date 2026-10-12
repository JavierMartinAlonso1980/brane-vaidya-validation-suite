import numpy as np
from .metric import f

def B_from_rho(params, a, rho):
    return params.kappa5_sq * (rho + params.lambda_brane) * a / 6.0

def kinematics(params, u, a, rho, tol=1e-13):
    B = B_from_rho(params, a, rho)
    radicand = B**2 - f(params, u, a)
    if radicand < -tol:
        raise ValueError(f"Invalid expanding branch: B²-f={radicand:g}")
    adot = np.sqrt(max(radicand, 0.0))
    udot = 1.0 / (B + adot)
    return B, adot, udot

def normal_contravariant_outgoing(u_dot, a_dot, f_value):
    # n_A=(a_dot,-u_dot); g^{AB} n_B for ds²=-fdu²-2dudr
    return np.array([u_dot, -a_dot - f_value * u_dot])

def normal_check(u_dot, a_dot, f_value):
    n_cov = np.array([a_dot, -u_dot])
    n_contra = normal_contravariant_outgoing(u_dot, a_dot, f_value)
    U = np.array([u_dot, a_dot])
    return float(n_cov @ n_contra), float(n_cov @ U)


def coordinate_vdot(epsilon, f_value, adot):
    """Future-directed algebraic branch solving -f vdot²+2 epsilon vdot adot=-1.

    This is a normalization check only. It does not by itself establish that the epsilon=±1
    metrics are the same physical flux solution.
    """
    if f_value <= 0:
        raise ValueError("reference test requires f>0")
    return (epsilon * adot + np.sqrt(adot**2 + f_value)) / f_value
