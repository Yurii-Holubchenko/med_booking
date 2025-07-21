from typing import Optional
from sqlalchemy.orm import Session
from app.db.models.user import User
from datetime import datetime

async def find_user_by_email(email: str, db: Session) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()

    return user

async def update_refresh_token(user: User, refresh_token: str, expired_at: datetime, db: Session) -> None:
    user.refresh_token = refresh_token
    user.refresh_token_expired_at = expired_at
    db.add(user)
    db.commit()
