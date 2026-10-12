import numpy as np
from .metric import f
from .embedding import kinematics, normal_check
from .bulk_stress import null_energy_condition
from .flux import direct_flux_scalar, junction_flux_scalar, reversed_normal_flux
from .extrinsic import K_spatial_coefficient, israel_spatial_target

def static_reference(params, a=3.0, rho=2.0):
    # delta_mu=0 gives mu'=0 and a zero null-dust flux.
    _, adot, udot = kinematics(params, 0.0, a, rho)
    return abs(direct_flux_scalar(params, 0.0, a, udot))

def point_diagnostics(params, u=0.0, a=3.0, rho=2.0):
    B, adot, udot = kinematics(params, u, a, rho)
    fv = f(params, u, a)
    qA = direct_flux_scalar(params, u, a, udot)
    qB = junction_flux_scalar(params, u, a, udot)
    n_norm, n_orth = normal_check(udot, adot, fv)
    return {
        "B": B, "adot": adot, "udot": udot, "f": fv,
        "normal_norm": n_norm, "normal_orthogonality": n_orth,
        "NEC": bool(null_energy_condition(params, u, a)),
        "Q_direct": qA, "Q_junction": qB,
        "flux_relative_residual": abs(qA-qB) / max(1.0, abs(qA), abs(qB)),
        "spatial_israel_residual": K_spatial_coefficient(B, a) - israel_spatial_target(params, rho),
        "orientation_flip": reversed_normal_flux(params, u, a, udot),
    }
