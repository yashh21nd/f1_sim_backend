from fastapi import APIRouter, Query
from app.services.simulation import predict_lap_time, simulate_race_pace  # ✅ import added

router = APIRouter(tags=["Prediction"])

@router.get("/lap_time")
def get_lap_time(
    driver: str = Query(..., description="Driver code (e.g. VER)"),
    year: int = Query(..., description="Race year"),
    circuit: str = Query(..., description="Circuit ID (e.g. monza)"),
    compound: str = Query("soft", description="Tyre compound (soft/medium/hard)"),
):
    result = predict_lap_time(driver, year, circuit, compound)
    return result


# ✅ NEW: /predict/race_pace route
@router.get("/race_pace")
def get_race_pace(
    driver: str = Query(..., description="Driver code (e.g. VER)"),
    year: int = Query(..., description="Race year"),
    circuit: str = Query(..., description="Circuit ID (e.g. monza)"),
    compound: str = Query("soft", description="Tyre compound (soft/medium/hard)"),
    laps: int = Query(50, description="Number of laps to simulate"),
):
    result = simulate_race_pace(driver, year, circuit, compound, laps)
    return result
