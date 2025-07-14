from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes.predict import router as predict_router

app = FastAPI()

# ✅ Health check for Render, UptimeRobot, etc.
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return JSONResponse(content={"message": "F1 Simulator Backend is alive 🚀"})

# ✅ Handle /robots.txt to avoid 404s from crawlers
@app.get("/robots.txt", include_in_schema=False)
def robots_txt():
    return (
        "User-agent: *\n"
        "Disallow:\n"
    )

# ✅ Register /predict routes
app.include_router(predict_router, prefix="/predict")

# ✅ CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

