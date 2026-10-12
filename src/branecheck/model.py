from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class VaidyaParameters:
    kappa5_sq: float = 1.0
    L: float = 1.0
    k: int = 1
    lambda_brane: float = 6.0
    w: float = 1.0 / 3.0
    mu_final: float = 0.2
    delta_mu: float = 1.5
    tau_mu: float = 3.0

    def __post_init__(self):
        if self.k not in (-1, 0, 1):
            raise ValueError("k must be -1, 0, or 1")
        if min(self.kappa5_sq, self.L, self.lambda_brane, self.tau_mu) <= 0:
            raise ValueError("positive scales required")

    def mu(self, u):
        return self.mu_final + self.delta_mu * np.exp(-np.asarray(u) / self.tau_mu)

    def mu_prime(self, u):
        return -(self.delta_mu / self.tau_mu) * np.exp(-np.asarray(u) / self.tau_mu)

    @property
    def rs_tuned(self):
        return np.isclose(self.kappa5_sq * self.lambda_brane / 6.0, 1.0 / self.L)
