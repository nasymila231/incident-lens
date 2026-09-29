from typing import Literal

from pydantic import BaseModel, Field

class IncidentCreate(BaseModel):
    title: str
    source: str
    severity: Literal["low", "medium", "high", "critical"]
    raw_log: str = Field(min_length=1)

class IncidentResponse(IncidentCreate):
    id: int
    status: str
