import numpy as np
from scipy.integrate import solve_ivp
from .embedding import kinematics
from .metric import f_r, f_u
from .flux import direct_flux_scalar
from .extrinsic import israel_temporal_target

def rhs(params, q_factor=1.0):
    def fun(t, y):
        a, u, rho = y
        B, adot, udot = kinematics(params, u, a, rho)
        H = adot / a
        Q = q_factor * direct_flux_scalar(params, u, a, udot)
        return [adot, udot, -3.0 * H * (1.0 + params.w) * rho + Q]
    return fun

def evolve(params, y0=(3.0, 0.0, 2.0), t_end=3.0, n=160, q_factor=1.0, rtol=1e-11, atol=1e-13):
    return solve_ivp(rhs(params, q_factor), (0.0, t_end), y0, method="DOP853", rtol=rtol, atol=atol,
                     t_eval=np.linspace(0.0, t_end, n))

def acceleration_residual(params, solution, q_factor=1.0):
    residuals, scales = [], []
    for a, u, rho in solution.y.T:
        B, adot, udot = kinematics(params, u, a, rho)
        H = adot / a
        Q = q_factor * direct_flux_scalar(params, u, a, udot)
        rho_dot = -3.0 * H * (1.0 + params.w) * rho + Q
        B_dot = params.kappa5_sq * (rho_dot * a + (rho + params.lambda_brane) * adot) / 6.0
        f_dot = f_r(params, u, a) * adot + f_u(params, u, a) * udot
        a_ddot_from_spatial = (B * B_dot - 0.5 * f_dot) / adot
        a_ddot_from_temporal = (B * israel_temporal_target(params, rho, params.w * rho)
                                 - 0.5 * f_r(params, u, a) - 0.5 * f_u(params, u, a) * udot**2)
        residuals.append(a_ddot_from_spatial - a_ddot_from_temporal)
        scales.append(abs(a_ddot_from_temporal) + 1e-30)
    residuals, scales = np.array(residuals), np.array(scales)
    return {"absolute_max": float(np.max(abs(residuals))), "relative_max": float(np.max(abs(residuals) / scales))}
