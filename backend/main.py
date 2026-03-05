from quantum_solver import solve_qubo
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from backend.qubo_builder import build_qubo
from simulation.simulator import generate_fake_data
from backend.sensor_parser import parse_sensor_data
from decision_translator import translate_decision

def main():
    print("Quantum Water Optimization System")
    print("---------------------------------")

    # simulate sensor data
    data = generate_fake_data()

    print("Sensor Data Received:")
    for key, value in data.items():
        print(f"{key}: {value}")

    # parse system state
    state = parse_sensor_data(data)

    print("\nParsed System State:")
    for key, value in state.items():
        print(f"{key}: {value}")
        
    qubo = build_qubo(state)

    print("\nOptimization Cost Model:")
    for key, value in qubo.items():
        print(f"{key}: {value}")
    
    # Step 4: solve optimization
    action, cost = solve_qubo(qubo)

    print("\nOptimal Decision:")
    print(f"action: {action}")
    print(f"cost: {cost}")
    
    hardware_action = translate_decision(action)

    print("\nHardware Control Signals:")
    for device, state in hardware_action.items():
        print(f"{device}: {state}")

    print("\nSystem ready for optimization step.")


if __name__ == "__main__":
    main()