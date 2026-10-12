from branecheck.embedding import coordinate_vdot
from branecheck.metric import proper_time_residual

def test_proper_time_normalisation_for_both_null_conventions(params):
    u, a, adot = 0.0, 3.0, 0.4
    for epsilon in (-1, 1):
        vdot = coordinate_vdot(epsilon, 9.0, adot)
        # supply f=9 explicitly through the defining quadratic
        assert abs(-9.0 * vdot**2 + 2.0 * epsilon * vdot * adot + 1.0) < 1e-13
