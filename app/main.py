from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router

app = FastAPI()

# ✅ Health check route for Render/UptimeRobot
@app.get("/")
def root():
    return {"message": "F1 Simulator Backend is alive 🚀"}

# ✅ Register router with /predict prefix
app.include_router(predict_router, prefix="/predict")

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

