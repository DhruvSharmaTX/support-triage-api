from fastapi import FastAPI
from app.routes.health_routes import router as health_router
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Support Triage API"}
app.include_router(health_router)
