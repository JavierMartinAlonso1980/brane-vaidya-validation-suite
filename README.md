# Brane–Vaidya validation suite

A convention-fixed computational test suite for a Z2-symmetric FRW brane in an outgoing AdS5–Vaidya bulk.

**Scope:** implementation validation only. It checks a declared metric, null-dust stress tensor, brane embedding,
Israel conditions, direct normal–tangential stress projection, static reference, normal-orientation reversal, and numerical sensitivity.
It does **not** claim a new physical law, an MVC transition, an EPR–ER mechanism, or a UV completion.

## Run

```bash
python -m venv .venv
# Git Bash on Windows:
source .venv/Scripts/activate
pip install -e ".[test]" --no-build-isolation
pytest -q
python run_suite.py --config configs/outgoing_z2.yaml --report report.json
```

The machine-readable report is a diagnostic artifact. Its tolerances are numerical choices, not physical constants.

## Conventions

- Signature: `-++++`.
- Outgoing Eddington–Finkelstein metric: `ds² = -f du² - 2 du dr + r² dΩ₃²`.
- `Q_E > 0` means injection into the brane.
- The normal points towards decreasing `r` in the reference convention.
- One-sided Z2 Israel convention: `K_{μν}=-(κ₅²/2)(S_{μν}-(S/3)h_{μν})`.

## Limits

The outgoing positive-energy null-dust solution is a local exterior model. If extended to a horizon, it is white-hole-like;
it is not a complete semiclassical evaporating-black-hole model. Asymmetric branes, a dynamical activation gate, and full bulk–brane stability are outside this suite.

## What the suite does not yet compute

The current Z2 implementation uses the one-sided FRW reduction of the Israel condition; it does not yet compute separate `K_plus` and `K_minus` from two asymmetric bulk patches. The `epsilon=±1` test checks only proper-time normalization in both null-coordinate conventions, not full coordinate equivalence of physical flux solutions. These are deliberate next steps.
