import requests
import random
import time
from datetime import datetime

API_URL = "http://127.0.0.1:8000/optimize"

LOCALITIES = ["house", "college", "residential_complex", "urban_area"]

def generate_sensor_reading(scenario=None):
    if scenario == "low_water":
        return {
            "water_level_percent": random.uniform(5, 20),
            "tds_ppm": random.uniform(400, 600),
            "ph": random.uniform(6.0, 7.0),
            "turbidity": random.uniform(3, 8),
            "tank_count": random.randint(1, 5),
            "locality": random.choice(LOCALITIES),
            "hour": random.randint(7, 10),
        }
    elif scenario == "hard_water":
        return {
            "water_level_percent": random.uniform(50, 90),
            "tds_ppm": random.uniform(600, 900),
            "ph": random.uniform(7.5, 9.0),
            "turbidity": random.uniform(1, 3),
            "tank_count": random.randint(1, 5),
            "locality": random.choice(LOCALITIES),
            "hour": random.randint(12, 15),
        }
    elif scenario == "peak_demand":
        return {
            "water_level_percent": random.uniform(30, 60),
            "tds_ppm": random.uniform(200, 400),
            "ph": random.uniform(6.8, 7.4),
            "turbidity": random.uniform(0.5, 2),
            "tank_count": random.randint(2, 6),
            "locality": "college",
            "hour": random.choice([7, 8, 9, 18, 19, 20]),
        }
    else:
        # fully random
        return {
            "water_level_percent": random.uniform(5, 100),
            "tds_ppm": random.uniform(50, 900),
            "ph": random.uniform(5.5, 9.5),
            "turbidity": random.uniform(0.1, 10),
            "tank_count": random.randint(1, 6),
            "locality": random.choice(LOCALITIES),
            "hour": datetime.now().hour,
        }


def send_to_api(data):
    try:
        response = requests.post(API_URL, json=data, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"  [ERROR] Status {response.status_code}: {response.text}")
            return None
    except requests.exceptions.ConnectionError:
        print("  [ERROR] Cannot connect to API. Is the server running?")
        return None


def print_result(run, scenario, data, result):
    print(f"\n{'='*52}")
    print(f"  Run {run:02d} | Scenario: {scenario}")
    print(f"{'='*52}")
    print(f"  Sensor Input:")
    print(f"    Level      : {data['water_level_percent']:.1f}%")
    print(f"    TDS        : {data['tds_ppm']:.0f} ppm")
    print(f"    pH         : {data['ph']:.2f}")
    print(f"    Turbidity  : {data['turbidity']:.2f} NTU")
    print(f"    Tanks      : {data['tank_count']}")
    print(f"    Locality   : {data['locality']}")
    print(f"    Hour       : {data['hour']}:00")

    if result:
        print(f"\n  Optimizer Decision:")
        print(f"    Action     : {result['action']}")
        print(f"    Pump ON    : {result['pump']}")
        print(f"    Softener   : {result['softener']}")
        print(f"    Energy     : {result['energy']}")
        print(f"\n  Parsed State:")
        for k, v in result['state'].items():
            print(f"    {k:<20}: {v}")
    else:
        print("  No response from API.")


def run_simulator(runs=12, delay=2):
    scenarios = ["low_water", "hard_water", "peak_demand", "random"]

    print("="*52)
    print("  ESP8266 SIMULATOR")
    print(f"  Target : {API_URL}")
    print(f"  Runs   : {runs}")
    print("="*52)

    for i in range(1, runs + 1):
        scenario = scenarios[(i - 1) % len(scenarios)]
        data = generate_sensor_reading(scenario)
        result = send_to_api(data)
        print_result(i, scenario, data, result)
        time.sleep(delay)

    print(f"\n{'='*52}")
    print("  SIMULATION COMPLETE")
    print("="*52)


if __name__ == "__main__":
    run_simulator(runs=12, delay=2)