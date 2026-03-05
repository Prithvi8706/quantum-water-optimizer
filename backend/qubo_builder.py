def build_qubo(state):

    costs = {
        "pump_off": 0,
        "pump_on": 0,
        "pump_softener": 0
    }

    # availability logic
    if state["availability"] == "low":
        costs["pump_off"] += 10

    elif state["availability"] == "high":
        costs["pump_on"] += 5

    # hardness logic
    if state["softness"] == "hard":
        costs["pump_on"] += 8
        costs["pump_softener"] -= 4

    elif state["softness"] == "softened":
        costs["pump_softener"] += 3

    elif state["softness"] == "moderate":
        costs["pump_on"] += 2

    # turbidity penalty
    if state["turbidity_state"] == "turbid":
        costs["pump_on"] += 4

    # pH penalty
    if state["ph_state"] != "neutral":
        costs["pump_on"] += 2

    return costs