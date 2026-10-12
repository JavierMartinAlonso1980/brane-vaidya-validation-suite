import numpy as np

def phi_outgoing(params, u, r):
    """T_AB = Phi k_A k_B, k_A=(-1,0,0,0,0), outgoing epsilon=-1 convention."""
    return -3.0 * params.mu_prime(u) / (2.0 * params.kappa5_sq * r**3)

def null_energy_condition(params, u, r):
    return phi_outgoing(params, u, r) >= 0.0

def einstein_uu_expected(params, u, r):
    return -3.0 * params.mu_prime(u) / (2.0 * r**3)

def stress_tensor_outgoing(params, u, r):
    T = np.zeros((5, 5), dtype=float)
    T[0, 0] = phi_outgoing(params, u, r)
    return T
