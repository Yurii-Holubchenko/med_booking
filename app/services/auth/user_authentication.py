from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.auth.refresh_token_generator import RefreshTokenGenerator

from app.services.user.find_user import FindUser

class UserAuthentication:
  def __init__(self, email: str, password: str, db: Session):
    self.email = email
    self.password = password
    self.db = db

  async def __call__(self):
    user = await FindUser(self.email, self.password, self.db)()

    if not user:
      raise HTTPException(status_code=401, detail="User with email and password doesn't exist")

    # Access token generation
    access_token = AccessTokenEncryptor().generate({"user_id": user.id})

    # For future decryption
    # print(AccessTokenEncryptor().parse(access_token))

    # Refresh token generation
    refresh_token = RefreshTokenGenerator(user.id).generate()

    return {
      "access_token": access_token,
      "refresh_token": refresh_token
    }
