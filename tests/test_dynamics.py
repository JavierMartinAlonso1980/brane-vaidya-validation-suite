from branecheck.evolution import evolve, acceleration_residual

def test_correct_flux_closes_acceleration(params):
    sol = evolve(params)
    assert acceleration_residual(params, sol, 1.0)["relative_max"] < 1e-10

def test_wrong_flux_is_detected(params):
    sol0 = evolve(params, q_factor=0.0)
    solh = evolve(params, q_factor=0.5)
    assert acceleration_residual(params, sol0, 0.0)["relative_max"] > 1e-3
    assert acceleration_residual(params, solh, 0.5)["relative_max"] > 1e-5
