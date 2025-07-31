from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.services.auth.access_token_encryptor import AccessTokenEncryptor
from app.services.auth.refresh_token_encryptor import RefreshTokenEncryptor

from app.services.crud.user import find_user_by_email
from app.core.security import verify_password

class Authentication:
    def __init__(self, email: str, password: str, db: Session):
        self.email = email
        self.password = password
        self.db = db

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_email(self.email, self.db)

        if user.confirmation_token:
            raise HTTPException(status_code=403, detail="Email is not confirmed")

        if not user or not verify_password(self.password, user.encrypted_password):
            raise HTTPException(status_code=401, detail="User with email and password doesn't exist")

        # Access token generation
        access_token = AccessTokenEncryptor().generate({"user_id": user.id})

        # For future decryption
        # print(AccessTokenEncryptor().parse(access_token))

        # Refresh token generation
        refresh_token = await RefreshTokenEncryptor(user, self.db).generate()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
