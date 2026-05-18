# Construction ERP Backend

İnşaat sektörüne yönelik Gelistirmis oldugum projem **ERP (Kurumsal Kaynak Planlama)** backend API ve web panelinden olusmaktadir. FastAPI ile REST servisleri, PostgreSQL ile kalıcı veri kullanilmis olup, JWT ile kimlik doğrulama sistemleri eklenerek guvenli giris ve yetkisiz islemelrin onune gecilmistir son test ve entegrasyon adimlari yapilmistir.

---

## Özellikler

| Modül | Açıklama |
|--------|----------|
| **Kimlik doğrulama** | OAuth2 + JWT (`/auth/token`, `/auth/me`) |
| **Çalışanlar** | Personel kayıtları, roller, maaş bilgisi |
| **Projeler** | Şantiye / proje yönetimi, bütçe, tarihler |
| **Envanter** | Tedarikçi, malzeme, ekipman |
| **HR / İSG** | Proje atamaları, iş güvenliği sertifikaları, kaza raporları |
| **Finans** | Satın alma siparişleri, faturalar, denetim logları |
| **Raporlar** | Bütçe ve kaza analizi |
| **Dashboard** | Tek sayfalık web arayüzü (`/dashboard`) |

---

## Ekran görüntüleri:

### Dashboard
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-49-04" src="https://github.com/user-attachments/assets/607e4713-5389-4072-8fe8-51a19026ab60" />


### Çalışanlar
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-49-26" src="https://github.com/user-attachments/assets/d5f8fe65-6657-4a73-b836-8274b257805b" />

### Projeler
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-49-34" src="https://github.com/user-attachments/assets/b5976788-2641-46ce-8e6b-a32e0b8e4468" />


### Envanter
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-49-56" src="https://github.com/user-attachments/assets/b03bfbb7-7bd2-4971-bf93-0e45cba45b93" />


### HR / İSG
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-50-15" src="https://github.com/user-attachments/assets/3ac3fdea-78ca-4b6e-9933-c5855946da65" />

### Finans
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-50-08" src="https://github.com/user-attachments/assets/08ca33bc-572c-4bca-bf80-db67a4c90425" />

### Raporlar
<img width="1920" height="1053" alt="Screenshot from 2026-05-18 15-50-15" src="https://github.com/user-attachments/assets/28921e7c-b3f0-4dfa-a3c6-53bf4c3578ae" />


---

## Teknoloji yığını

- **Python 3.10+**
- **FastAPI** + **Uvicorn**
- **SQLAlchemy** + **PostgreSQL**
- **JWT** (python-jose) + **bcrypt** (passlib)

---

## Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/KULLANICI_ADINIZ/construction_erp_backend.git
cd construction_erp_backend
```

### 2. Sanal ortam ve bağımlılıklar

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Ortam değişkenleri

```bash
copy .env.example .env
```

`.env` dosyasını düzenleyin (`DATABASE_URL`, `SECRET_KEY`).

### 4. PostgreSQL

Veritabanı oluşturun:

```sql
CREATE DATABASE construction_erp;
```

### 5. Uygulamayı çalıştırın

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

| Adres | Açıklama |
|--------|----------|
| http://localhost:8000 | API ana sayfa |
| http://localhost:8000/dashboard | Web panel |
| http://localhost:8000/docs | Swagger UI |
| http://localhost:8000/redoc | ReDoc |

**Demo giriş (panel):** `admin` / `admin123`

---

## API özeti

| Prefix | Endpoint örnekleri |
|--------|---------------------|
| `/auth` | `POST /token`, `GET /me` |
| `/employees` | `GET /`, `GET /{id}`, `POST /` |
| `/projects` | `GET /`, `POST /` |
| `/users` | `GET /`, `POST /` |
| `/inventory` | `suppliers`, `materials`, `equipment` |
| `/hr-hse` | `assignments`, `safety-certificates`, `incident-reports` |
| `/finance` | `purchase-orders`, `invoices`, `audit-logs` |
| `/reports` | `budget-analysis`, `incident-analysis` |

Korumalı uçlar için `Authorization: Bearer <token>` başlığı gerekir.

---

## Proje yapısı

```
construction_erp_backend/
├── main.py                 # FastAPI uygulaması
├── app/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── routers/            # API modülleri
├── static/
│   └── erp_dashboard.html  # Web arayüzü
├── docs/
│   ├── README.md           # Detaylı dokümantasyon
│   └── screenshots/        # Ekran görüntüleri
├── requirements.txt
├── .env.example
└── .gitignore
```


