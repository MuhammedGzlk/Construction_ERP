from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app import crud, schemas, models
from app.routers.auth import get_current_user

router = APIRouter(prefix="/finance", tags=["finance"])


@router.get("/purchase-orders", response_model=List[schemas.PurchaseOrder])
def list_purchase_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                         current_user: models.User = Depends(get_current_user)):
    return crud.get_purchase_orders(db, skip=skip, limit=limit)


@router.get("/invoices", response_model=List[schemas.Invoice])
def list_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                  current_user: models.User = Depends(get_current_user)):
    return crud.get_invoices(db, skip=skip, limit=limit)


@router.get("/audit-logs", response_model=List[schemas.AuditLog])
def list_audit_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return crud.get_audit_logs(db, skip=skip, limit=limit)