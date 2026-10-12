import pytest
from branecheck.embedding import kinematics

def test_invalid_expanding_branch_raises(params):
    # At a=3 the AdS-Schwarzschild blackening factor is positive. A nearly zero B is then incompatible with B²=adot²+f.
    with pytest.raises(ValueError):
        kinematics(params, u=0.0, a=3.0, rho=-params.lambda_brane + 1e-12)
