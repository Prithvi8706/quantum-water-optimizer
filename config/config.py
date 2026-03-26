# Water level thresholds (%)
LOW_LEVEL_THRESHOLD = 30
MEDIUM_LEVEL_THRESHOLD = 70

# TDS thresholds (ppm)
SOFT_TDS_MAX = 120
SOFTENED_TDS_MAX = 200
MODERATE_TDS_MAX = 300

# pH thresholds
PH_ACIDIC_MAX = 6.5
PH_ALKALINE_MIN = 7.5

# Turbidity thresholds (NTU)
CLEAR_TURBIDITY_MAX = 5

# Time-of-day hour ranges
PEAK_HOURS = list(range(6, 10)) + list(range(18, 22))   # 6-9am, 6-9pm
OFF_PEAK_HOURS = list(range(0, 5)) + list(range(23, 24)) # midnight-5am, 11pm

# Demand scenario probabilities by time-of-day
DEMAND_PROBABILITIES = {
    "peak":     {"low": 0.1, "medium": 0.3, "high": 0.6},
    "normal":   {"low": 0.3, "medium": 0.5, "high": 0.2},
    "off_peak": {"low": 0.7, "medium": 0.2, "high": 0.1},
}

# Cost weights per action per demand scenario
# Format: cost_table[action][demand_level] = cost
SCENARIO_COST_TABLE = {
    "pump_off": {
        "low":    0,
        "medium": 6,
        "high":   15,
    },
    "pump_on": {
        "low":    4,
        "medium": 2,
        "high":   0,
    },
    "pump_softener": {
        "low":    5,
        "medium": 3,
        "high":   1,
    },
}

# Tank scaling — more tanks = higher demand weight
TANK_DEMAND_MULTIPLIER = {
    1: 1.0,
    2: 1.2,
    3: 1.5,
    4: 1.8,
    5: 2.0,
}

# Locality scaling — larger locality = higher base demand
LOCALITY_MULTIPLIER = {
    "house":   1.0,
    "complex": 1.3,
    "college": 1.7,
    "urban":   2.0,
}