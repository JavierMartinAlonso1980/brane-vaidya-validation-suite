import argparse, json
from dataclasses import asdict
import yaml
from branecheck.conventions import Convention
from branecheck.model import VaidyaParameters
from branecheck.diagnostics import point_diagnostics, static_reference
from branecheck.evolution import evolve, acceleration_residual

parser = argparse.ArgumentParser()
parser.add_argument("--config", default="configs/outgoing_z2.yaml")
parser.add_argument("--report", default="report.json")
args = parser.parse_args()
cfg = yaml.safe_load(open(args.config, encoding="utf-8"))
params = VaidyaParameters(**cfg["parameters"])
convention = Convention(**cfg["convention"])
point = point_diagnostics(params, **cfg["initial"])
static = VaidyaParameters(**{**asdict(params), "delta_mu": 0.0})
static_q = static_reference(static, a=cfg["initial"]["a"], rho=cfg["initial"]["rho"])
sol = evolve(params, y0=[cfg["initial"]["a"], cfg["initial"]["u"], cfg["initial"]["rho"]], **cfg["evolution"])
correct = acceleration_residual(params, sol, q_factor=1.0)
half = acceleration_residual(params, evolve(params, y0=sol.y[:,0], q_factor=0.5, **cfg["evolution"]), q_factor=0.5)
no_exchange = acceleration_residual(params, evolve(params, y0=sol.y[:,0], q_factor=0.0, **cfg["evolution"]), q_factor=0.0)
convergence = []
for rtol, n in [(1e-7, 80), (1e-9, 160), (1e-11, 320)]:
    s = evolve(params, y0=[cfg["initial"]["a"], cfg["initial"]["u"], cfg["initial"]["rho"]],
               t_end=cfg["evolution"]["t_end"], n=n, rtol=rtol, atol=rtol * 1e-2)
    convergence.append({"rtol": rtol, "n": n, **acceleration_residual(params, s, q_factor=1.0)})
report = {"convention": asdict(convention), "parameters": asdict(params), "point": point,
          "static_reference_Q_abs": static_q, "acceleration_residual": {"correct": correct, "half_Q": half, "zero_Q": no_exchange},
          "solver_convergence": convergence}
json.dump(report, open(args.report, "w", encoding="utf-8"), indent=2)
print(json.dumps(report, indent=2))
