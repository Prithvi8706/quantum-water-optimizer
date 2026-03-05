# Quantum Water Optimizer

Quantum-assisted optimization system for intelligent water tank management in urban environments such as colleges, residential complexes, and municipal infrastructures.

## Overview

Most domestic water controllers operate using simple threshold-based logic where pumps turn ON or OFF depending only on tank level. These systems ignore several interacting factors such as water quality, demand patterns, and infrastructure scale.

When multiple variables interact (water level, quality, number of tanks, demand cycles), the number of possible system states grows rapidly. This project formulates the water control problem as an optimization problem and explores solving it using quantum-inspired and quantum optimization techniques.

The system integrates IoT sensors with a backend optimization engine to determine the most efficient pump and valve actions.

## Criteria Used in Optimization

The system evaluates multiple environmental and infrastructure parameters:

1. Water Availability (High / Medium / Low)
2. Water Softness based on TDS (Hard / Soft / Softened)
3. Number of Tanks in the System
4. Water pH Level
5. Water Turbidity
6. Time-of-Day Demand Pattern (Peak / Normal / Off-Peak)
7. Type of Locality (House / Residential Complex / College / Urban Area)

## System Architecture

Sensor Layer  
Water sensors measure level, hardness, pH, and turbidity.

IoT Layer  
ESP8266 nodes collect sensor readings and send them to the backend server.

Optimization Layer  
A Python backend constructs an optimization model (QUBO) and solves it using simulated annealing or quantum annealing.

Control Layer  
Optimal decisions are sent back to the IoT node to control pumps and softener valves.

## Technologies Used

- Python  
- D-Wave Ocean SDK  
- Dimod (Simulated Annealing)  
- ESP8266 (IoT Node)  
- FastAPI (Backend API)  
- Water Quality Sensors (TDS, pH, Turbidity, Ultrasonic)

## Repository Structure

backend/ – Optimization logic and solver  
simulation/ – Sensor simulation for testing without hardware  
config/ – System configuration parameters  
hardware/ – ESP8266 firmware (future implementation)  
docs/ – System architecture and formulation  

## Running the Simulation

Install dependencies:

pip install -r requirements.txt

Run the backend simulation:

python backend/main.py

This runs the optimizer using simulated sensor data.

## Future Work

- Integration with real quantum hardware (D-Wave QPU)  
- Distributed IoT sensor nodes for multiple tanks  
- Machine learning based demand prediction  
- Municipal scale water resource optimization  

## Author
Prithvi Raghu
