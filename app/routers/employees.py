from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas
from app.routers.auth import get_current_user
from app import models

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=List[schemas.Employee])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.get_employees(db, skip=skip, limit=limit)


@router.get("/{employee_id}", response_model=schemas.Employee)
def get_employee(employee_id: int, db: Session = Depends(get_db),
                 current_user: models.User = Depends(get_current_user)):
    emp = crud.get_employee(db, employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Çalışan bulunamadı")
    return emp


@router.post("/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return crud.create_employee(db, employee)