def solve_qubo(costs):
    """
    Select the action with the minimum cost.
    """

    best_action = None
    best_cost = float("inf")

    for action, cost in costs.items():
        if cost < best_cost:
            best_cost = cost
            best_action = action

    return best_action, best_cost