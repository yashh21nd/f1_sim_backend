from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router

app = FastAPI()

# ✅ Root route for Render health checks or uptime monitoring
@app.get("/")
def read_root():
    return {"message": "✅ F1 Simulator Backend is alive and running!"}

# ✅ Register all prediction-related routes under /predict
app.include_router(predict_router, prefix="/predict")

# ✅ Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with your frontend domain for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
