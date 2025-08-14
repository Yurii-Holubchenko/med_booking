from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.crud.user import find_user_by_confirmation_token, reset_confirmation_token
from datetime import datetime, timezone

class Confirmation:
    def __init__(self, token: str, db: Session):
        self.token = token
        self.db = db

    async def __call__(self) -> dict[str, str]:
        user = await find_user_by_confirmation_token(self.token, self.db)

        if not user:
            raise HTTPException(status_code=400, detail="Invalid token")

        if user and user.confirmation_token_expired_at < datetime.now(timezone.utc):
            raise HTTPException(status_code=400, detail="Token expired")

        await reset_confirmation_token(user, self.db)

        return {"message": f"Email {user.email} confirmed successfully"}
