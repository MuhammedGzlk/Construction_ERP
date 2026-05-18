from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey, Boolean, DateTime, Text
from .database import Base

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, unique=True, nullable=False)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String)
    salary = Column(Numeric(12, 2))
    phone_number = Column(String)
    # Role tablosuyla ilişki
    role_id = Column(Integer, ForeignKey("roles.id"))
    
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    budget = Column(Numeric(15, 2))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    first_name = Column(String)
    last_name = Column(String)

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    contact_person = Column(String)
    phone = Column(String)
    email = Column(String)

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    unit = Column(String)
    unit_price = Column(Numeric(10, 2), nullable=False)

class Equipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String)
    daily_rental_cost = Column(Numeric(10, 2))
    current_project_id = Column(Integer, ForeignKey("projects.id"))

class ProjectAssignment(Base):
    __tablename__ = "project_assignments"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    role_in_project = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

class SafetyCertificate(Base):
    __tablename__ = "safety_certificates"
    id = Column(Integer, primary_key=True, index=True)
    worker_id = Column(Integer, ForeignKey("employees.id"))
    certificate_name = Column(String)
    issue_date = Column(Date)
    expiry_date = Column(Date)
    is_valid = Column(Boolean, default=True)

class IncidentReport(Base):
    __tablename__ = "incident_reports"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    worker_id = Column(Integer, ForeignKey("employees.id"))
    incident_date = Column(DateTime) # Kaza anını tam zamanlı (saatli) tutuyoruz
    description = Column(Text)
    severity_level = Column(String)
class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    order_date = Column(Date)
    total_amount = Column(Numeric(12, 2))
    status = Column(String)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("purchase_orders.id"))
    invoice_number = Column(String)
    issue_date = Column(Date)
    grand_total = Column(Numeric(12, 2))

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    table_name = Column(String)
    # Zaman serisi verisini kaybetmemek için DateTime kullanıyoruz!
    action_timestamp = Column(DateTime)