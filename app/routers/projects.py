from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas
from app.routers.auth import get_current_user
from app import models

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=List[schemas.Project])
def list_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                  current_user: models.User = Depends(get_current_user)):
    return crud.get_projects(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.create_project(db, project)