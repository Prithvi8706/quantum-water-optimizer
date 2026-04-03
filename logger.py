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
    "cost_pump_off",
    "cost_pump_on",
    "cost_pump_softener",
    "action",
    "optimal_cost",
    "pump",
    "softener",
    "valve",
]


def init_log():
    with open(LOG_FILE, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writeheader()
    print(f"[Logger] Log file reset: {LOG_FILE}")


def log_decision(
    tank_id:   int,
    data:      dict,
    state:     dict,
    raw_costs: dict,
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
        "cost_pump_off":        raw_costs["pump_off"],
        "cost_pump_on":         raw_costs["pump_on"],
        "cost_pump_softener":   raw_costs["pump_softener"],
        "action":               action,
        "optimal_cost":         cost,
        "pump":                 hardware["pump"],
        "softener":             hardware["softener"],
        "valve":                hardware["valve"],
    }

    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(row)