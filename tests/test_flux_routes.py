from branecheck.diagnostics import point_diagnostics

def test_direct_and_junction_flux_agree(params):
    d = point_diagnostics(params)
    assert d["NEC"]
    assert d["flux_relative_residual"] < 1e-13
    assert abs(d["spatial_israel_residual"]) < 1e-13

def test_orientation_reversal_flips_flux(params):
    d = point_diagnostics(params)
    assert abs(d["orientation_flip"] + d["Q_direct"]) < 1e-13
