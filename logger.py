import csv
import os
from datetime import datetime


LOG_FILE = "water_optimizer_log.csv"

HEADERS = [
    "timestamp",
    "tank_id",
    "water_level_percent",
    "tds_ppm",
    "ph",
    "turbidity",
    "tank_count",
    "locality",
    "hour",
    "availability",
    "softness",
    "ph_state",
    "turbidity_state",
    "time_of_day",
    "cost_pump_off",       # ← added
    "cost_pump_on",        # ← added
    "cost_pump_softener",  # ← added
    "action",
    "optimal_cost",
    "pump",
    "softener",
    "valve",
]


def init_log():
    file_exists = os.path.isfile(LOG_FILE)
    if not file_exists:
        with open(LOG_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()
        print(f"[Logger] Created new log file: {LOG_FILE}")
    else:
        print(f"[Logger] Appending to existing log file: {LOG_FILE}")


def log_decision(
    tank_id:   int,
    data:      dict,
    state:     dict,
    raw_costs: dict,  # ← added
    action:    str,
    cost:      float,
    hardware:  dict,
):
    row = {
        "timestamp":            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tank_id":              tank_id,
        "water_level_percent":  data["water_level_percent"],
        "tds_ppm":              data["tds_ppm"],
        "ph":                   data["ph"],
        "turbidity":            data["turbidity"],
        "tank_count":           data["tank_count"],
        "locality":             data["locality"],
        "hour":                 data["hour"],
        "availability":         state["availability"],
        "softness":             state["softness"],
        "ph_state":             state["ph_state"],
        "turbidity_state":      state["turbidity_state"],
        "time_of_day":          state["time_of_day"],
        "cost_pump_off":        raw_costs["pump_off"],        # ← added
        "cost_pump_on":         raw_costs["pump_on"],         # ← added
        "cost_pump_softener":   raw_costs["pump_softener"],   # ← added
        "action":               action,
        "optimal_cost":         cost,
        "pump":                 hardware["pump"],
        "softener":             hardware["softener"],
        "valve":                hardware["valve"],
    }

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(row)