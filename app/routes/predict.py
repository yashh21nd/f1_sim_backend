from fastapi import APIRouter, Query
from app.services.simulation import predict_lap_time

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.get("/lap_time")
def get_lap_time(
    driver: str = Query(..., description="Driver code (e.g. VER)"),
    year: int = Query(..., description="Race year"),
    circuit: str = Query(..., description="Circuit ID (e.g. monza)"),
    compound: str = Query("soft", description="Tyre compound (soft/medium/hard)"),
):
    result = predict_lap_time(driver, year, circuit, compound)
    return result
