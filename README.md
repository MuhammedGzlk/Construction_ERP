# Construction ERP Backend

İnşaat sektörüne yönelik **ERP (Kurumsal Kaynak Planlama)** backend API ve web paneli. FastAPI ile REST servisleri, PostgreSQL ile kalıcı veri, JWT ile kimlik doğrulama.

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

Detaylı dokümantasyon ve ekran görüntüsü rehberi: **[docs/README.md](docs/README.md)**

---

## Ekran görüntüleri

Aşağıdaki görselleri `docs/screenshots/` altına ekledikten sonra burada görünür. Dosya adları ve klasör yapısı için: [docs/screenshots/README.md](docs/screenshots/README.md)

### Giriş
![Giriş ekranı](docs/screenshots/01-login/login.png)

### Dashboard
![Dashboard](docs/screenshots/02-dashboard/dashboard.png)

### Çalışanlar
![Çalışanlar](docs/screenshots/03-employees/employees.png)

### Projeler
![Projeler](docs/screenshots/04-projects/projects.png)

### Envanter
![Envanter](docs/screenshots/05-inventory/inventory.png)

### HR / İSG
![HR ve İSG](docs/screenshots/06-hr-hse/hr-hse.png)

### Finans
![Finans](docs/screenshots/07-finance/finance.png)

### Raporlar
![Raporlar](docs/screenshots/08-reports/reports.png)

### API dokümantasyonu (Swagger)
![Swagger UI](docs/screenshots/09-api-docs/swagger.png)

> Görseller henüz eklenmediyse GitHub’da kırık link görünebilir; PNG dosyalarını ilgili klasörlere koymanız yeterlidir.

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

---

## GitHub’a yükleme

Adım adım rehber: **[docs/GITHUB_PUSH.md](docs/GITHUB_PUSH.md)**

---

## Lisans

Bu proje eğitim / portföy amaçlıdır. Kullanım koşullarını kendi lisansınızla belirleyebilirsiniz.
