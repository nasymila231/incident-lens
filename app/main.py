from fastapi import FastAPI
from app.schemas.incidents import IncidentCreate

incidents = []

app = FastAPI(
    title="OpsPilot API",
    version="0.1.0",
)

@app.post("/api/v1/incidents")
def create_incident(incident: IncidentCreate):
    new_incident = {
        "id": len(incidents) + 1,
        "status": "open",
        **incident.model_dump(),
    }

    incidents.append(new_incident)
    return new_incident

@app.get("/api/v1/incidents")
def get_incidents():
    return incidents

@app.get("/health")
def health_check():
    return {"status": "ok"}
