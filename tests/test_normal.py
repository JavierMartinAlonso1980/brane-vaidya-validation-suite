from branecheck.diagnostics import point_diagnostics

def test_normal_is_unit_and_orthogonal(params):
    d = point_diagnostics(params)
    assert abs(d["normal_norm"] - 1.0) < 1e-13
    assert abs(d["normal_orthogonality"]) < 1e-13
