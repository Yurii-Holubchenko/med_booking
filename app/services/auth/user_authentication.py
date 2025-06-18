from fastapi import HTTPException
from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.auth.refresh_token_generator import RefreshTokenGenerator

from app.db.database import SessionLocal
from app.db.models import User

class UserAuthentication:
  def __init__(self, email: str, password: str):
    self.email = email
    self.password = password

  def __call__(self):
    user = self.__find_user()

    if not user:
      raise HTTPException(status_code=401, detail="User with email and password doesn't exist")

    # Access token generation
    payload = {"user_id": user.id}
    access_token = AccessTokenEncryptor().generate(payload)

    # For future decryption
    # print(AccessTokenEncryptor().parse(access_token))

    # Refresh token generation
    refresh_token = RefreshTokenGenerator(user.id).generate()

    return {
      "access_token": access_token,
      "refresh_token": refresh_token
    }

  def __find_user(self):
    db = SessionLocal()

    user = db.query(User).filter(
      User.email == self.email,
      User.encrypted_password == self.password
    ).first()

    db.close()

    return user
