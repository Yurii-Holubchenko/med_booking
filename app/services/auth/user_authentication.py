from fastapi import HTTPException

from app.db.database import db_connection
from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.auth.refresh_token_generator import RefreshTokenGenerator

from app.services.user.find_user import FindUser

class UserAuthentication:
  def __init__(self, email: str, password: str):
    self.email = email
    self.password = password

  async def __call__(self):
    db = next(db_connection())
    user = await FindUser(self.email, self.password, db)()

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
