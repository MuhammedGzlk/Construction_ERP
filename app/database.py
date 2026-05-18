from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı bağlantı adresi (Kullanıcı:postgres, Şifre:14022001, DB:construction_erp)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:14022001@localhost/construction_erp"

# Motoru (Engine) oluşturalım
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Her bir istek için yeni bir veritabanı oturumu oluşturacak yapı
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tablo sınıflarımızı türeteceğimiz temel sınıf
Base = declarative_base()

# Veritabanı oturumunu yöneten bağımlılık (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()