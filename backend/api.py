from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from backend.sensor_parser import parse_sensor_data
from backend.qubo_builder import build_qubo
from backend.quantum_solver import solve_qubo
from decision_translator import translate_decision
from logger import log_decision

app = FastAPI(title="Quantum Water Optimizer API")


class SensorPayload(BaseModel):
    water_level_percent: float
    tds_ppm: float
    ph: float
    turbidity: float
    tank_count: int
    locality: str
    hour: Optional[int] = None


class OptimizeResponse(BaseModel):
    action: str
    pump: bool
    softener: bool
    energy: float
    state: dict
    raw_costs: dict


@app.post("/optimize", response_model=OptimizeResponse)
def optimize(payload: SensorPayload):
    try:
        data = payload.model_dump()
        state = parse_sensor_data(data)
        raw_costs, norm_costs, bqm = build_qubo(state)
        action, energy = solve_qubo(norm_costs, bqm=bqm, method="sa")
        hardware = translate_decision(action)
        log_decision("esp8266", data, state, raw_costs, action, energy, hardware)

        return OptimizeResponse(
            action=action,
            pump=hardware.get("pump") == "ON",
            softener=hardware.get("softener") == "ON",
            energy=energy,
            state=state,
            raw_costs=raw_costs,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    return {"status": "ok"}