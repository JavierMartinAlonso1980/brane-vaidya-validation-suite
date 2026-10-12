from dataclasses import asdict
from branecheck.model import VaidyaParameters
from branecheck.diagnostics import static_reference

def test_static_bulk_has_zero_exchange(params):
    static = VaidyaParameters(**{**asdict(params), "delta_mu": 0.0})
    assert static_reference(static) < 1e-14
