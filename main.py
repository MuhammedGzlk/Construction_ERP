from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import employees, projects, users, inventory, hr_hse, finance_logs, reports, auth
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Construction ERP API")

# CORS — tarayıcının aynı makineden (dashboard) istek atabilmesi için gerekli
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Üretimde spesifik domain listesi kullan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(projects.router)
app.include_router(users.router)
app.include_router(inventory.router)
app.include_router(hr_hse.router)
app.include_router(finance_logs.router)
app.include_router(reports.router)


@app.get("/")
def home():
    return {"mesaj": "ERP Sistemi Çalışıyor!"}


@app.get("/dashboard")
def dashboard():
    return FileResponse("static/erp_dashboard.html")