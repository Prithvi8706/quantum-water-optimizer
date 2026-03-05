import random


def generate_fake_data():
    data = {
        "water_level_percent": random.randint(10, 95),
        "tds_ppm": random.randint(100, 600),
        "ph": round(random.uniform(6.0, 8.5), 2),
        "turbidity": random.randint(1, 50),
        "tank_count": random.randint(1, 5),
        "locality": random.choice(["house", "complex", "college", "urban"])
    }

    return data