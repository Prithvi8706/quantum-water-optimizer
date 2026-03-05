def translate_decision(action):
    if action == "pump_off":
        return {
            "pump": "OFF",
            "softener": "OFF",
            "valve": "BYPASS"
        }

    elif action == "pump_on":
        return {
            "pump": "ON",
            "softener": "OFF",
            "valve": "BYPASS"
        }

    elif action == "pump_softener":
        return {
            "pump": "ON",
            "softener": "ON",
            "valve": "SOFTENER_ROUTE"
        }

    else:
        return {
            "pump": "UNKNOWN",
            "softener": "UNKNOWN",
            "valve": "UNKNOWN"
        }