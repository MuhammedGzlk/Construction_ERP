from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, models
from app.routers.auth import get_current_user

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/suppliers", response_model=List[schemas.Supplier])
def list_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.get_suppliers(db, skip=skip, limit=limit)


@router.get("/materials", response_model=List[schemas.Material])
def list_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.get_materials(db, skip=skip, limit=limit)


@router.get("/equipment", response_model=List[schemas.Equipment])
def list_equipment(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                   current_user: models.User = Depends(get_current_user)):
    return crud.get_equipment(db, skip=skip, limit=limit)