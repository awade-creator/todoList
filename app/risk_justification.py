from datetime import datetime
from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()



@router.get('/')
"""
    Function operations:
        - Search
        - Result Limits
        - Pagination
"""
def get_risk_justifications(db: Session = Depends(get_db), 
                            limit: int = 10, 
                            page: int = 1, 
                            search: str = ''):
    skip = (page - 1) * limit

    risk_justifications = db.query(models.Note).filter(
        models.RiskJustification.hostname.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success',
            'results': len(risk_justifications), 
            'risk_justifications': risk_justifications}
    
    
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_note(payload: schemas.RiskJustificationBaseSchema, db: Session = Depends(get_db)):
    new_risk_justification = models.RiskJustification(**payload.dict())
    db.add(new_risk_justification)
    db.commit()
    db.refresh(new_risk_justification)
    return {"status": "success", "risk_justification": new_risk_justification}


@router.patch("/{risk_justificationId}")
def update_risk_justification(risk_justificationId: str):
    return f"update risk justification item with id: {risk_justificationId}"

@router.get('/{risk_justificationId}')
def get_risk_justification(risk_justificationId: str, db: Session = Depends(get_db)):
    note = db.query(models.RiskJustification).filter(models.RiskJustification.id == RiskJustificationId).first()
    if not risk_justification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No risk justification with this id: {id} found")
    return {"status": "success", "risk_justification": risk_justification}

@router.delete('/{risk_justificationId}')
def delete_risk_justification(risk_justificationId: str):
    return f"delete risk justification item with id {risk_justificationId}"