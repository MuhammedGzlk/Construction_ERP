from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, models
from app.routers.auth import get_current_user

router = APIRouter(prefix="/hr-hse", tags=["hr_hse"])


@router.get("/assignments", response_model=List[schemas.ProjectAssignment])
def list_assignments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                     current_user: models.User = Depends(get_current_user)):
    return crud.get_project_assignments(db, skip=skip, limit=limit)


@router.get("/safety-certificates", response_model=List[schemas.SafetyCertificate])
def list_certificates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    return crud.get_safety_certificates(db, skip=skip, limit=limit)


@router.get("/incident-reports", response_model=List[schemas.IncidentReport])
def list_incidents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.get_incident_reports(db, skip=skip, limit=limit)