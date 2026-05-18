from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, models
from app.routers.auth import get_current_user

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/budget-analysis")
def budget_analysis(db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    rows = crud.get_budget_analysis(db)
    return [dict(r) for r in rows]


@router.get("/incident-analysis")
def incident_analysis(db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    rows = crud.get_incident_analysis(db)
    return [dict(r) for r in rows]