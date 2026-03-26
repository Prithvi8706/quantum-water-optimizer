def translate_decision(action: str) -> dict:
    """
    Maps optimizer action to physical relay/valve control signals.
    """
    signals = {
        "pump_off": {
            "pump":     "OFF",
            "softener": "OFF",
            "valve":    "BYPASS",
            "lcd_msg":  "Pump OFF",
        },
        "pump_on": {
            "pump":     "ON",
            "softener": "OFF",
            "valve":    "BYPASS",
            "lcd_msg":  "Pumping Normal",
        },
        "pump_softener": {
            "pump":     "ON",
            "softener": "ON",
            "valve":    "SOFTENER_ROUTE",
            "lcd_msg":  "Pumping via Softener",
        },
    }

    return signals.get(
        action,
        {
            "pump":     "UNKNOWN",
            "softener": "UNKNOWN",
            "valve":    "UNKNOWN",
            "lcd_msg":  "ERROR",
        },
    )