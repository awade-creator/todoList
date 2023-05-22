from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE

class RiskJustification(Base):
    __tablename__ = 'riskjustifications'
    id = Column(GUID, primary_key=True,default=GUID_DEFAULT_SQLITE)
    dateOfRequest = Column(String, nullable=False)
    applicationOwner = Column(String, nullable=False)
    cve = Column(String, nullable=False)
    cvssScanner = Column(String, nullable=False)
    hostname = Column(String, nullable=False)
    description = Column(String, nullable=False)
    riskStatement = Column(String, nullable=False)
    mitigationControls = Column(String, nullable=False)
    resolutionDetails = Column(String)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False,
                       server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), nullable=False,
                       server_default=func.now())
    
    
    
    