import random
from datetime import datetime


def generate_fake_data(hour: int = None) -> dict:
    """
    Simulates sensor readings for one tank/location.
    If hour is None, uses current system hour.
    """
    if hour is None:
        hour = datetime.now().hour

    data = {
        "water_level_percent": random.randint(10, 95),
        "tds_ppm":             random.randint(100, 600),
        "ph":                  round(random.uniform(5.5, 9.0), 2),
        "turbidity":           random.randint(1, 50),
        "tank_count":          random.randint(1, 5),
        "locality":            random.choice(
                                   ["house", "complex", "college", "urban"]
                               ),
        "hour":                hour,
    }
    return data


def generate_multi_tank_data(tank_count: int, hour: int = None) -> list[dict]:
    """
    Generates independent sensor readings for each tank.
    """
    return [generate_fake_data(hour=hour) for _ in range(tank_count)]