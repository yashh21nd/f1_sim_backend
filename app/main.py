from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router  # ✅ Add this

app = FastAPI()

# ✅ Register the predict routes under /predict
app.include_router(predict_router)

# ✅ Root route for Render or uptime monitoring
@app.get("/")
def read_root():
    return {"message": "F1 Simulator Backend is alive 🚀"}

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
