from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encrypt_password(password: str) -> str:
  return pwd_context.hash(password)

def verify_password(password: str, encrypted_password: str) -> bool:
  return pwd_context.verify(password, encrypted_password)
