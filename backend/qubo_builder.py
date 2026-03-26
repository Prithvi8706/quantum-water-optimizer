import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import dimod
from config.config import (
    DEMAND_PROBABILITIES,
    SCENARIO_COST_TABLE,
    TANK_DEMAND_MULTIPLIER,
    LOCALITY_MULTIPLIER,
)

ACTION_VARS = {"pump_off": "x0", "pump_on": "x1", "pump_softener": "x2"}


def compute_expected_cost(action, time_of_day, scale):
    probs = DEMAND_PROBABILITIES[time_of_day]
    costs = SCENARIO_COST_TABLE[action]
    return round(sum(probs[s] * costs[s] for s in probs) * scale, 4)


def build_qubo(state):
    tank_scale   = TANK_DEMAND_MULTIPLIER.get(state["tank_count"], 1.0)
    locale_scale = LOCALITY_MULTIPLIER.get(state["locality"], 1.0)
    scale        = round(tank_scale * locale_scale, 4)
    time_of_day  = state["time_of_day"]

    raw_costs = {a: compute_expected_cost(a, time_of_day, scale) for a in ACTION_VARS}

    if state["availability"] == "low":
        raw_costs["pump_off"] += 10 * scale
        raw_costs["pump_on"]  -= 3  * scale
    elif state["availability"] == "high":
        raw_costs["pump_on"]  += 5  * scale
        raw_costs["pump_off"] -= 2  * scale

    if state["softness"] == "hard":
        raw_costs["pump_on"]       += 8 * scale
        raw_costs["pump_softener"] -= 6 * scale
    elif state["softness"] == "moderate":
        raw_costs["pump_on"]       += 3 * scale
        raw_costs["pump_softener"] -= 2 * scale
    elif state["softness"] == "softened":
        raw_costs["pump_softener"] += 2 * scale

    if state["turbidity_state"] == "turbid":
        raw_costs["pump_on"]       += 4 * scale
        raw_costs["pump_softener"] += 2 * scale

    if state["ph_state"] == "acidic":
        raw_costs["pump_on"]       += 3 * scale
        raw_costs["pump_softener"] += 2 * scale
    elif state["ph_state"] == "alkaline":
        raw_costs["pump_on"]       += 2 * scale
        raw_costs["pump_softener"] += 1 * scale

    raw_costs = {k: round(v, 4) for k, v in raw_costs.items()}

    # Normalise so minimum = 0
    min_cost   = min(raw_costs.values())
    norm_costs = {k: round(v - min_cost, 4) for k, v in raw_costs.items()}

    # Build dimod BQM
    linear = {ACTION_VARS[a]: norm_costs[a] for a in ACTION_VARS}
    PENALTY = max(norm_costs.values()) * 3 + 10
    quadratic = {
        ("x0", "x1"): PENALTY * 2,
        ("x0", "x2"): PENALTY * 2,
        ("x1", "x2"): PENALTY * 2,
    }
    for var in linear:
        linear[var] += PENALTY * (1 - 2)

    bqm = dimod.BinaryQuadraticModel(
        linear, quadratic, offset=PENALTY, vartype=dimod.BINARY
    )

    return raw_costs, bqm  # returns BOTH