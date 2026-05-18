from sqlalchemy.orm import Session
from sqlalchemy import text
from . import models, schemas

# Çalışanları listeleme (Tümü)
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

# ID'ye göre çalışan getirme
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

# Yeni çalışan ekleme
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# --- PROJE FONKSİYONLARI ---
def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# --- KULLANICI FONKSİYONLARI ---
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# --- TEDARİKÇİ FONKSİYONLARI ---
def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Supplier).offset(skip).limit(limit).all()


# --- MALZEME FONKSİYONLARI ---
def get_materials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Material).offset(skip).limit(limit).all()

# --- EKİPMAN FONKSİYONLARI ---
def get_equipment(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Equipment).offset(skip).limit(limit).all()

# --- HR & HSE FONKSİYONLARI ---
def get_project_assignments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProjectAssignment).offset(skip).limit(limit).all()

def get_safety_certificates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SafetyCertificate).offset(skip).limit(limit).all()

def get_incident_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.IncidentReport).offset(skip).limit(limit).all()



# --- FİNANS VE LOG FONKSİYONLARI ---
def get_purchase_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PurchaseOrder).offset(skip).limit(limit).all()

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

def get_audit_logs(db: Session, skip: int = 0, limit: int = 100):
    # Logları en yeniden eskiye sıralı getirmek mantıklı olacaktır
    return db.query(models.AuditLog).order_by(models.AuditLog.action_timestamp.desc()).offset(skip).limit(limit).all()



# --- GELİŞMİŞ RAPOR FONKSİYONLARI ---

def get_budget_analysis(db: Session):
    # Proje bütçesi ve faturaları karşılaştıran SQL
    query = text("""
        SELECT 
            p.name AS proje_adi, 
            p.budget AS toplam_butce,
            COALESCE(SUM(i.grand_total), 0) AS toplam_harcama,
            CASE 
                WHEN p.budget > 0 THEN ROUND((COALESCE(SUM(i.grand_total), 0) / p.budget) * 100, 2)
                ELSE 0 
            END AS harcama_yuzdesi
        FROM projects p
        LEFT JOIN purchase_orders po ON p.id = po.project_id
        LEFT JOIN invoices i ON po.id = i.order_id
        GROUP BY p.id, p.name, p.budget;
    """)
    # Sorguyu çalıştırıp sözlük (dictionary) formatında döndürüyoruz
    return db.execute(query).mappings().all()

def get_incident_analysis(db: Session):
    # Kaza yapan işçilerin sertifika durumunu kontrol eden SQL
    query = text("""
        SELECT 
            e.first_name || ' ' || e.last_name AS calisan,
            ir.incident_date AS kaza_tarihi,
            ir.severity_level AS siddet,
            sc.certificate_name AS sertifika,
            sc.is_valid AS sertifika_gecerli_mi
        FROM incident_reports ir
        JOIN employees e ON ir.worker_id = e.id
        LEFT JOIN safety_certificates sc ON e.id = sc.worker_id;
    """)
    return db.execute(query).mappings().all()