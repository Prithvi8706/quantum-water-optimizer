from datetime import datetime
from config.config import (
    LOW_LEVEL_THRESHOLD,
    MEDIUM_LEVEL_THRESHOLD,
    SOFT_TDS_MAX,
    SOFTENED_TDS_MAX,
    MODERATE_TDS_MAX,
    PH_ACIDIC_MAX,
    PH_ALKALINE_MIN,
    CLEAR_TURBIDITY_MAX,
    PEAK_HOURS,
    OFF_PEAK_HOURS,
)


def classify_time_of_day(hour: int) -> str:
    if hour in PEAK_HOURS:
        return "peak"
    elif hour in OFF_PEAK_HOURS:
        return "off_peak"
    else:
        return "normal"


def parse_sensor_data(data: dict) -> dict:
    state = {}

    # 1. Availability
    level = data["water_level_percent"]
    if level < LOW_LEVEL_THRESHOLD:
        state["availability"] = "low"
    elif level < MEDIUM_LEVEL_THRESHOLD:
        state["availability"] = "medium"
    else:
        state["availability"] = "high"

    # 2. Softness (TDS proxy for hardness)
    tds = data["tds_ppm"]
    if tds < SOFT_TDS_MAX:
        state["softness"] = "soft"
    elif tds < SOFTENED_TDS_MAX:
        state["softness"] = "softened"
    elif tds < MODERATE_TDS_MAX:
        state["softness"] = "moderate"
    else:
        state["softness"] = "hard"

    # 3. pH
    ph = data["ph"]
    if ph < PH_ACIDIC_MAX:
        state["ph_state"] = "acidic"
    elif ph > PH_ALKALINE_MIN:
        state["ph_state"] = "alkaline"
    else:
        state["ph_state"] = "neutral"

    # 4. Turbidity
    if data["turbidity"] < CLEAR_TURBIDITY_MAX:
        state["turbidity_state"] = "clear"
    else:
        state["turbidity_state"] = "turbid"

    # 5. Time-of-day
    hour = data.get("hour", datetime.now().hour)
    state["time_of_day"] = classify_time_of_day(hour)

    # 6. Tank count
    state["tank_count"] = data["tank_count"]

    # 7. Locality
    state["locality"] = data["locality"]

    return state