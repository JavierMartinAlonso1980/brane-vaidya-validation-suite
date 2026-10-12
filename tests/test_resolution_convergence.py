from branecheck.evolution import evolve, acceleration_residual

def test_correct_current_remains_closed_under_solver_tolerance_changes(params):
    residuals = []
    for rtol, n in [(1e-7, 80), (1e-9, 160), (1e-11, 320)]:
        sol = evolve(params, rtol=rtol, atol=rtol*1e-2, n=n)
        residuals.append(acceleration_residual(params, sol, 1.0)["absolute_max"])
    assert max(residuals) < 1e-9
