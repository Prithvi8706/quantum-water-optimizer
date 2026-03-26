import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import dimod
from dwave.samplers import SimulatedAnnealingSampler

ACTION_VARS_REVERSE = {
    "x0": "pump_off",
    "x1": "pump_on",
    "x2": "pump_softener"
}


def solve_with_sa(bqm, num_reads=1000):
    """
    Uses D-Wave's SimulatedAnnealingSampler from dwave-samplers.
    Proper quantum-inspired solver — models quantum tunneling behavior.
    """
    sampler    = SimulatedAnnealingSampler()
    sampleset  = sampler.sample(bqm, num_reads=num_reads)
    best_sample = sampleset.first.sample
    best_energy = sampleset.first.energy

    chosen_var = next((v for v, val in best_sample.items() if val == 1), None)
    if chosen_var is None:
        chosen_var = "x0"

    action = ACTION_VARS_REVERSE.get(chosen_var, "pump_off")
    return action, round(best_energy, 4)


def solve_greedy(costs):
    """
    Classical greedy fallback.
    """
    best = min(costs, key=costs.get)
    return best, costs[best]


def solve_qubo(costs, bqm=None, method="sa"):
    """
    Unified solver interface.
    method: "sa" | "greedy"
    """
    if method == "sa" and bqm is not None:
        return solve_with_sa(bqm)
    return solve_greedy(costs)