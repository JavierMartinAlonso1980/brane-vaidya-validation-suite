from .metric import f_r, f_u

def K_spatial_coefficient(B, a):
    """K_ij = coefficient * h_ij for the decreasing-r normal."""
    return -B / a

def K_tautau(a_ddot, B, fr, fu, u_dot):
    return (a_ddot + 0.5 * fr + 0.5 * fu * u_dot**2) / B

def israel_spatial_target(params, rho):
    return -params.kappa5_sq * (rho + params.lambda_brane) / 6.0

def israel_temporal_target(params, rho, p):
    return -params.kappa5_sq * (2.0 * rho + 3.0 * p - params.lambda_brane) / 6.0
