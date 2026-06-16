from fastapi import FastAPI
from app.routes.health_routes import router as health_router
from app.routes.ticket_routes import router as ticket_router
from app.routes.model_routes import router as model_router
from app.routes.analytics_routes import router as analytics_router
from app.routes.kb_routes import router as kb_router
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Support Triage API"}
app.include_router(health_router)
app.include_router(ticket_router)
app.include_router(model_router)
app.include_router(analytics_router)
app.include_router(kb_router)
