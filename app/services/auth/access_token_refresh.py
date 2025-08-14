import hashlib

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime, timezone
from app.services.crud.user import find_user_by_refresh_token
from app.services.auth.access_token_encryptor import AccessTokenEncryptor

class AccessTokenRefresh:
    def __init__(self, refresh_token: str, db: Session):
        self.refresh_token = hashlib.sha256(refresh_token.encode()).hexdigest()
        self.db = db

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_refresh_token(self.refresh_token, self.db)

        if not user:
            raise HTTPException(status_code=401, detail="Refresh token doesn't exist")

        if user and user.refresh_token_expired_at < datetime.now(timezone.utc):
            raise HTTPException(status_code=400, detail="Refresh token is expired")

        access_token = AccessTokenEncryptor().generate({"user_id": user.id})

        return {"access_token": access_token}
