from config.config import (
    LOW_LEVEL_THRESHOLD,
    MEDIUM_LEVEL_THRESHOLD,
    SOFT_TDS_MAX,
    SOFTENED_TDS_MAX,
    MODERATE_TDS_MAX,
    PH_ACIDIC_MAX,
    PH_ALKALINE_MIN,
    CLEAR_TURBIDITY_MAX
)


def parse_sensor_data(data):
    state = {}

    # water availability
    if data["water_level_percent"] < LOW_LEVEL_THRESHOLD:
        state["availability"] = "low"
    elif data["water_level_percent"] < MEDIUM_LEVEL_THRESHOLD:
        state["availability"] = "medium"
    else:
        state["availability"] = "high"

    # hardness / softness classification
    tds = data["tds_ppm"]

    if tds < SOFT_TDS_MAX:
        state["softness"] = "soft"

    elif tds < SOFTENED_TDS_MAX:
        state["softness"] = "softened"

    elif tds < MODERATE_TDS_MAX:
        state["softness"] = "moderate"

    else:
        state["softness"] = "hard"

    # pH classification
    if data["ph"] < PH_ACIDIC_MAX:
        state["ph_state"] = "acidic"
    elif data["ph"] > PH_ALKALINE_MIN:
        state["ph_state"] = "alkaline"
    else:
        state["ph_state"] = "neutral"

    # turbidity classification
    if data["turbidity"] < CLEAR_TURBIDITY_MAX:
        state["turbidity_state"] = "clear"
    else:
        state["turbidity_state"] = "turbid"

    state["tank_count"] = data["tank_count"]
    state["locality"] = data["locality"]

    return state