# Quantum Water Optimizer

Quantum-assisted optimization system for intelligent water tank management in urban environments such as colleges, residential complexes, and municipal infrastructures.

## Overview

Most domestic water management systems already account for several interacting factors such as water quality, pH levels, turbidity, demand cycles, and infrastructure scale. However, the challenge lies in determining the most optimal control decision when all these variables interact simultaneously.

This project addresses that challenge using quantum-inspired optimization. By formulating the water control problem as a Quadratic Unconstrained Binary Optimization (QUBO) model, the system leverages quantum phenomena such as superposition — evaluating all possible pump and valve states simultaneously — to identify the most cost-effective control action. This approach finds the global minimum energy solution rather than relying on classical greedy or threshold-based decision logic.

The system integrates IoT sensor data with a backend optimization engine to determine the most efficient pump and valve actions across multi-tank urban infrastructure.

## How It Works

Sensor data (water level, pH, TDS, turbidity, tank count, locality) is parsed into a system state and encoded as a Binary Quadratic Model (BQM). The optimizer runs 1000 annealing reads using D-Wave's SimulatedAnnealingSampler and selects the minimum energy action — pump off, pump on, or pump with softener. Decisions are logged to CSV across multi-tank simulation runs.

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

**Sensor Layer**
Water sensors measure level, hardness, pH, and turbidity.

**IoT Layer**
ESP8266 nodes collect sensor readings and send them to the backend server.

**Optimization Layer**
A Python backend constructs a Binary Quadratic Model (BQM) and solves it using D-Wave's SimulatedAnnealingSampler with 1000 annealing reads per decision cycle.

**Control Layer**
Optimal decisions are sent back to the IoT node to control pumps and softener valves. All decisions are logged to CSV for analysis.

## Technologies Used

- Python
- D-Wave Ocean SDK
- Dimod — Binary Quadratic Model (BQM)
- D-Wave SimulatedAnnealingSampler (dwave-samplers)
- FastAPI (Backend API)
- ESP8266 (IoT Node — future hardware integration)
- Water Quality Sensors (TDS, pH, Turbidity, Ultrasonic)

## Repository Structure

    backend/      – Optimization logic and solver
    simulation/   – Sensor simulation for testing without hardware
    config/       – System configuration parameters
    hardware/     – ESP8266 firmware (future implementation)
    docs/         – System architecture and formulation

## Running the Simulation

Install dependencies:

    pip install -r requirements.txt

Run the backend simulation:

    python backend/main.py

This runs the optimizer using simulated sensor data across multiple tanks and logs decisions to water_optimizer_log.csv.

## Sample Output

    ====================================================
      QUANTUM-INSPIRED SMART WATER SYSTEM
      Solver        : SA
      Simulation Runs: 10
    ====================================================

    ──── TANK 1 ────────────────────────────────────────
      Sensor Readings:
        water_level_percent       : 23
        tds_ppm                   : 430
        ph                        : 7.1
        turbidity                 : 12
        tank_count                : 3
        locality                  : college

      Optimal Action  : pump_softener
      Optimal Cost    : -4.0

      Hardware Signals:
        pump                      : ON
        softener                  : ON
        valve                     : SOFTENER_ROUTE

## Future Work

- Migration from SimulatedAnnealingSampler to DWaveSampler for execution on D-Wave Advantage QPU via Leap cloud service
- Distributed IoT sensor nodes for multiple tanks
- Time-of-day demand pattern integration
- Locality-based cost weighting
- Municipal scale water resource optimization
- FastAPI endpoint for live sensor integration

## Author

Prithvi Raghu