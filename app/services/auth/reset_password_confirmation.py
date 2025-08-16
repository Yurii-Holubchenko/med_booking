from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.core.security import verify_password, encrypt_password
from app.services.crud.user import find_user_by_reset_password_token, set_new_password

class ResetPasswordConfirmation:
    def __init__(self, token: str, password: str, new_password: str, db: Session):
        self.token = token
        self.password = password
        self.new_password = new_password
        self.db = db

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_reset_password_token(self.token, self.db)

        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")

        if user and user.reset_password_token_expired_at < datetime.now(timezone.utc):
            raise HTTPException(status_code=400, detail="Token expired")

        if user and not verify_password(self.password, user.encrypted_password):
            raise HTTPException(status_code=400, detail="Password is incorrect")

        await set_new_password(user, encrypt_password(self.new_password), self.db)

        return {"message": f"Password was reset successfully"}
