import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from simulation.simulator import generate_fake_data, generate_multi_tank_data
from backend.sensor_parser import parse_sensor_data
from backend.qubo_builder import build_qubo
from backend.quantum_solver import solve_qubo
from decision_translator import translate_decision
from logger import init_log, log_decision

SOLVER_METHOD   = "sa"
DEMO_TANK_COUNT = 3
SIMULATION_RUNS = 10


def print_divider(title=""):
    width = 52
    if title:
        print(f"\n{'─'*4} {title} {'─'*(width-len(title)-6)}")
    else:
        print("─"*52)


def run_single_tank(tank_id, data, log=True):
    print_divider(f"TANK {tank_id}")

    print("  Sensor Readings:")
    for k, v in data.items():
        print(f"    {k:<26}: {v}")

    state = parse_sensor_data(data)
    print("\n  Parsed State:")
    for k, v in state.items():
        print(f"    {k:<26}: {v}")

    # ── CHANGED: unpack all three values ──
    raw_costs, norm_costs, bqm = build_qubo(state)

    # print raw costs (real interpretable values)
    print("\n  QUBO Cost Model (raw):")
    for k, v in raw_costs.items():
        print(f"    {k:<26}: {v}")

    # print normalised costs (what solver sees)
    print("\n  QUBO Cost Model (normalised):")
    for k, v in norm_costs.items():
        print(f"    {k:<26}: {v}")

    # ── CHANGED: solver uses norm_costs ──
    action, cost = solve_qubo(norm_costs, bqm=bqm, method=SOLVER_METHOD)
    print(f"\n  Optimal Action  : {action}")
    print(f"  Optimal Cost    : {cost}")

    hardware = translate_decision(action)
    print("\n  Hardware Signals:")
    for k, v in hardware.items():
        print(f"    {k:<26}: {v}")

    # ── CHANGED: log raw_costs so CSV shows real values ──
    if log:
        log_decision(tank_id, data, state, raw_costs, action, cost, hardware)
        print(f"  [Logger] Decision logged.")

    return action


def main():
    print("=" * 52)
    print("  QUANTUM-INSPIRED SMART WATER SYSTEM")
    print(f"  Solver        : {SOLVER_METHOD.upper()}")
    print(f"  Simulation Runs: {SIMULATION_RUNS}")
    print("=" * 52)

    init_log()

    for run in range(1, SIMULATION_RUNS + 1):
        print(f"\n{'='*52}")
        print(f"  RUN {run} of {SIMULATION_RUNS}")
        print(f"{'='*52}")

        multi_data     = generate_multi_tank_data(DEMO_TANK_COUNT)
        action_summary = {}

        for i, tank_data in enumerate(multi_data, start=1):
            tank_data["tank_count"] = DEMO_TANK_COUNT
            action = run_single_tank(i, tank_data, log=True)
            action_summary[f"Tank {i}"] = action

        print_divider("RUN SUMMARY")
        for tank, action in action_summary.items():
            print(f"  {tank:<10}: {action}")

    print("\n" + "="*52)
    print("  ALL RUNS COMPLETE")
    print(f"  Results saved to: water_optimizer_log.csv")
    print("="*52)


if __name__ == "__main__":
    main()