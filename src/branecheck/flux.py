from .bulk_stress import phi_outgoing
from .metric import f_u

def direct_flux_scalar(params, u, a, u_dot):
    """Q_E = 2 T_AB n^A U^B for declared Z2/decreasing-r convention."""
    return 2.0 * phi_outgoing(params, u, a) * u_dot**2

def junction_flux_scalar(params, u, a, u_dot):
    """FRW reduction of independently declared temporal/spatial Israel equations."""
    return 3.0 * f_u(params, u, a) * u_dot**2 / (params.kappa5_sq * a)

def reversed_normal_flux(params, u, a, u_dot):
    return -direct_flux_scalar(params, u, a, u_dot)
