from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

# Gizli anahtarımız (Gerçek projelerde bu rastgele, karmaşık bir metin olmalıdır)
SECRET_KEY = "super_gizli_erp_anahtari_123!@#"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # Token 1 saat sonra geçersiz olacak

# Şifreleri hash'lemek için bcrypt kullanıyoruz
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt