from datetime import datetime
from typing import List
from pydantic import BaseModel

"""
 Validation of incoming payloads
"""

class RiskJustificationBaseSchema(BaseModel):
    id: str | None = None
    dateOfRequest : str
    applicationOwner: str
    cve: str
    cvssScanner: str
    hostname: str
    description: str
    riskStatement: str
    mitigationControls: str
    resolutionDetails: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListRiskJustificationResponse(BaseModel):
    status: str
    results: int
    riskjustifications: List[RiskJustificationBaseSchema]

