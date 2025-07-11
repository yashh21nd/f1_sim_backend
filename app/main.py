from fastapi import FastAPI
from app.routes import predict

app = FastAPI(
    title="F1 Pre-Race Simulation API",
    version="1.0"
)

app.include_router(predict.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the F1 Simulation API"}
