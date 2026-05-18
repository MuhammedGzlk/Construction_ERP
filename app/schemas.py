from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal
# Dosyanın en üstüne bunu mutlaka ekle:
from datetime import date, datetime

# Role Şemaları
class RoleBase(BaseModel):
    role_name: str

class RoleCreate(RoleBase):
    pass

class ProjectBase(BaseModel):
    name: str
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    budget: Optional[Decimal] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    
    class Config:
        from_attributes = True

# --- KULLANICI ŞEMALARI ---
class UserBase(BaseModel):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role_id: Optional[int] = None
    employee_id: Optional[int] = None

class UserCreate(UserBase):
    password: str  # Dışarıdan şifre düz metin gelir, veritabanına hashlenip kaydedilir.

class User(UserBase):
    id: int
    # Dikkat: Güvenlik gereği 'password_hash' alanını dışarıya (API'ye) vermiyoruz!

    class Config:
        from_attributes = True

class Role(RoleBase):
    id: int

    class Config:
        from_attributes = True # SQLAlchemy modellerini Pydantic'e dönüştürmek için

# Employee Şemaları
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    position: Optional[str] = None
    salary: Decimal
    phone_number: Optional[str] = None

class EmployeeCreate(EmployeeBase):
    pass # Yeni kayıt oluştururken id gerekmez

class Employee(EmployeeBase):
    id: int
    role_id: Optional[int] = None

    class Config:
        from_attributes = True


# --- TEDARİKÇİ ŞEMALARI ---
class SupplierBase(BaseModel):
    company_name: str
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    class Config:
        from_attributes = True

# --- MALZEME ŞEMALARI ---
class MaterialBase(BaseModel):
    name: str
    unit: Optional[str] = None
    unit_price: Decimal

class MaterialCreate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int
    class Config:
        from_attributes = True

# --- EKİPMAN ŞEMALARI ---
class EquipmentBase(BaseModel):
    name: str
    type: Optional[str] = None
    daily_rental_cost: Optional[Decimal] = None
    current_project_id: Optional[int] = None

class EquipmentCreate(EquipmentBase):
    pass

class Equipment(EquipmentBase):
    id: int
    class Config:
        from_attributes = True

# --- PROJE ATAMA ŞEMALARI ---
class ProjectAssignmentBase(BaseModel):
    employee_id: Optional[int] = None
    project_id: Optional[int] = None
    role_in_project: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class ProjectAssignment(ProjectAssignmentBase):
    id: int
    class Config:
        from_attributes = True

# --- İSG SERTİFİKA ŞEMALARI ---
class SafetyCertificateBase(BaseModel):
    worker_id: Optional[int] = None
    certificate_name: Optional[str] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None
    is_valid: Optional[bool] = True

class SafetyCertificate(SafetyCertificateBase):
    id: int
    class Config:
        from_attributes = True

# --- KAZA RAPORU ŞEMALARI ---
class IncidentReportBase(BaseModel):
    project_id: Optional[int] = None
    worker_id: Optional[int] = None
    incident_date: Optional[datetime] = None  # Zaman verisini (time) koruyoruz!
    description: Optional[str] = None
    severity_level: Optional[str] = None

class IncidentReport(IncidentReportBase):
    id: int
    class Config:
        from_attributes = True

# --- SATINALMA SİPARİŞİ ŞEMALARI ---
class PurchaseOrderBase(BaseModel):
    supplier_id: Optional[int] = None
    project_id: Optional[int] = None
    order_date: Optional[date] = None
    total_amount: Optional[Decimal] = None
    status: Optional[str] = None

class PurchaseOrder(PurchaseOrderBase):
    id: int
    class Config:
        from_attributes = True

# --- FATURA ŞEMALARI ---
class InvoiceBase(BaseModel):
    order_id: Optional[int] = None
    invoice_number: Optional[str] = None
    issue_date: Optional[date] = None
    grand_total: Optional[Decimal] = None

class Invoice(InvoiceBase):
    id: int
    class Config:
        from_attributes = True

# --- DENETİM KAYDI (AUDIT LOG) ŞEMALARI ---
class AuditLogBase(BaseModel):
    user_id: Optional[int] = None
    action: Optional[str] = None
    table_name: Optional[str] = None
    # Zaman parametresini (saat/dakika) koruyoruz
    action_timestamp: Optional[datetime] = None 

class AuditLog(AuditLogBase):
    id: int
    class Config:
        from_attributes = True
# --- GELİŞMİŞ RAPOR ŞEMALARI ---

class BudgetReport(BaseModel):
    proje_adi: str
    toplam_butce: Decimal
    toplam_harcama: Optional[Decimal] = 0
    harcama_yuzdesi: Optional[Decimal] = 0

class IncidentReportDetail(BaseModel):
    calisan: str
    kaza_tarihi: datetime
    siddet: str
    sertifika: Optional[str] = None
    sertifika_gecerli_mi: Optional[bool] = None
